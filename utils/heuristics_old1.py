import re
import yaml
import spacy
import yake
from langdetect import detect

# Carregar regras heurísticas a partir de ficheiro YAML
def load_rules(filepath="rules.yaml"):
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# Aplicar regras com base no idioma
def apply_heuristics(email_text, rules):
    reasons = []
    lower = email_text.lower()
    lang = detect(lower)

    for category, keywords in rules.get("keywords", {}).items():
        # Aplica regras globais (sem idioma)
        for kw in keywords.get("global", []):
            if kw in lower:
                reasons.append(f"Contains keyword '{kw}' related to {category} (global)")
                break

        # Aplica regras específicas do idioma
        for kw in keywords.get(lang, []):
            if kw in lower:
                reasons.append(f"Contains keyword '{kw}' related to {category} ({lang})")
                break

    # Heurística de links
    urls = re.findall(r"http[s]?://\S+", email_text)
    if urls:
        reasons.append(f"Contains suspicious link(s): {', '.join(urls)}")

    return reasons, lang

# Extrair palavras-chave com YAKE (para info complementar)
def extract_keywords(email_text, lang="en"):
    extractor = yake.KeywordExtractor(lan=lang, top=5)
    keywords = extractor.extract_keywords(email_text)
    return [kw for kw, score in keywords]

# Explicação combinada
def explain_email(email_text, rules):
    reasons, lang = apply_heuristics(email_text, rules)
    return reasons
