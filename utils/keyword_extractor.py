import yake

# Extrai palavras-chave com YAKE
def extract_keywords(text, lang="en", max_keywords=5):
    try:
        extractor = yake.KeywordExtractor(lan=lang, top=max_keywords)
        keywords = extractor.extract_keywords(text)
        return [kw for kw, _ in keywords]
    except Exception:
        return []
