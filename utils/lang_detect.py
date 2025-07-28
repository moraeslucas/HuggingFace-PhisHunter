from langdetect import detect, DetectorFactory

# Garante resultados consistentes
DetectorFactory.seed = 0

def detect_language(text):
    try:
        lang = detect(text)
        return lang
    except Exception:
        return "unknown"
