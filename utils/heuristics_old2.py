
import re
import yaml
import yake
import spacy
from langdetect import detect

# Carregar regras heurísticas com pesos
def load_rules(filepath="rules_weighted.yaml"):
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# Aplicar regras com base no idioma e calcular score
def apply_heuristics(email_text, rules):
    reasons = []
    total_score = 0.0
    lower = email_text.lower()
    lang = detect(lower)

    for category, keywords in rules.get("keywords", {}).items():
        # Global keywords
        for entry in keywords.get("global", []):
            pattern = entry["term"]
            weight = entry.get("weight", 1.0)
            if re.search(pattern, lower, re.IGNORECASE):
                reasons.append(f"[{category}] Matched '{pattern}' (global, weight={weight})")
                total_score += weight

        # Language-specific keywords
        for entry in keywords.get(lang, []):
            pattern = entry["term"]
            weight = entry.get("weight", 1.0)
            if re.search(pattern, lower, re.IGNORECASE):
                reasons.append(f"[{category}] Matched '{pattern}' ({lang}, weight={weight})")
                total_score += weight

    # Heurística de links
    urls = re.findall(r"http[s]?://\S+", email_text)
    if urls:
        reasons.append(f"Contains suspicious link(s): {', '.join(urls)}")
        total_score += 1.0  # peso fixo para presença de links

    return reasons, total_score, lang

# Extração de palavras-chave com YAKE
def extract_keywords(email_text, lang="en"):
    extractor = yake.KeywordExtractor(lan=lang, top=5)
    keywords = extractor.extract_keywords(email_text)
    return [kw for kw, score in keywords]

# Explicação combinada
def explain_email(email_text, rules):
    reasons, score, lang = apply_heuristics(email_text, rules)
    return reasons, score
