
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import gradio as gr
from utils.heuristics import load_rules, explain_email, extract_keywords
from langdetect import detect
from pathlib import Path
import re
from utils.virustotal import check_url_virustotal
import extract_msg

# Modelo
model_name = "ElSlay/BERT-Phishing-Email-Model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Heurísticas
rules = load_rules("rules.yaml")

# Classificação com BERT
def classify_email(email_text):
    inputs = tokenizer(email_text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1).detach().numpy()[0]
    labels = ["Legitimate", "Phishing"]
    prediction = labels[probs.argmax()]
    confidence = probs.max()
    return prediction, confidence

# Análise completa do email
def analyze_email(file_input=None, text_input=None):
    email_text = None

    if text_input:
        email_text = text_input
    elif file_input:
        path = file_input.name if hasattr(file_input, "name") else file_input
        if path.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                email_text = f.read()
        elif path.endswith(".msg"):
            msg = extract_msg.Message(path)
            email_text = f"{msg.subject or ''}\n{msg.body or ''}"
        else:
            return "Unsupported file type."
    else:
        return "No input provided."

    if not email_text:
        return "Could not extract text from file."

    # Classificação
    label, confidence = classify_email(email_text)

    # Heurística
    explanations, score = explain_email(email_text, rules)

    # Keywords
    lang = detect(email_text)
    keywords = extract_keywords(email_text, lang)
    keywords_text = "Top keywords: " + ", ".join(keywords)

    # Explicação heurística
    explanation_text = "📌 Explanation:\n• " + "\n• ".join(explanations)

    # Verificação VirusTotal
    urls = re.findall(r"http[s]?://\S+", email_text)
    vt_results = []
    for url in urls:
        stats = check_url_virustotal(url)
        if "error" in stats:
            vt_results.append(f"URL: {url} | VT: {stats['error']}")
        else:
            vt_results.append(f"URL: {url} | Malicious: {stats.get('malicious', 0)}, Suspicious: {stats.get('suspicious', 0)}, Harmless: {stats.get('harmless', 0)}")
    vt_text = "\n".join(vt_results) if vt_results else "No URLs found."

    return f"Classification: {label} ({confidence:.2%})\n\n{explanation_text}\n\nScore: {score}\n\n{keywords_text}\n\nVirusTotal Results:\n{vt_text}"

# Carregar exemplos
def update_text_from_example(example_name):
    return example_emails[example_name]

def load_example_files():
    examples_path = Path("examples")
    files = sorted(examples_path.glob("*.txt"))
    return {file.name: file.read_text(encoding="utf-8") for file in files}

example_emails = load_example_files()

# Interface Gradio
with gr.Blocks() as demo:
    gr.Markdown("## 🛡️ PhishHunter – Email Phishing Detector")

    with gr.Row():
        dropdown = gr.Dropdown(
            choices=list(example_emails.keys()),
            label="Load Example Email",
            info="Select a sample email to test",
        )
        textbox = gr.Textbox(lines=15, label="Paste or load email content")
        filebox = gr.File(label="Upload email (.txt or .msg)", file_types=[".txt", ".msg"])

    dropdown.change(fn=update_text_from_example, inputs=dropdown, outputs=textbox)

    output = gr.Textbox(label="Classification & Explanation")

    btn = gr.Button("Analyze")
    btn.click(fn=analyze_email, inputs=[filebox, textbox], outputs=output)

if __name__ == "__main__":
    demo.launch()
