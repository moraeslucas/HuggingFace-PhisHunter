---
title: PhishHunter
emoji: 🕵️‍♂️
colorFrom: blue
colorTo: indigo
sdk: gradio
app_file: app.py
pinned: false
sdk_version: 5.38.2
---

# PhishHunter 

PhishHunter is an open-source NLP-based email classification tool that detects phishing attempts and explains why an email might be suspicious.

Part of the "Natural Language Processing & Language Models" project at [Porto Business School](https://www.pbs.up.pt/en/) in which we explored different library versions/requirements, etc.

Special thanks to hipotuga :relaxed:

## 🔧 Technologies Used

- [Hugging Face Transformers](https://huggingface.co/)
- [Gradio](https://gradio.app/)
- [NLTK](https://www.nltk.org/)
- [YAKE](https://github.com/LIAAD/yake)
- [LangDetect](https://pypi.org/project/langdetect/)
- [extract-msg](https://pypi.org/project/extract-msg/)
- [Python](https://www.python.org/)

## 🚀 Getting Started

1. Clone the repository or download the project folder:
   ```bash
   git clone https://github.com/SEU_UTILIZADOR/phishhunter.git
   cd phishhunter
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate    # Windows
   # As an alternative:
   source venv/bin/activate  # Linux/macOS
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   python app_improved.py
   ```

## 📦 Features

- Classify email text using a fine-tuned BERT model
- Heuristic-based rules per language (via `rules.yaml`)
- Language detection for multilingual support
- Keyword extraction
- URL verification via VirusTotal API
- Gradio-based interface for easy use

## 📜 License

This project is licensed under the MIT License.
