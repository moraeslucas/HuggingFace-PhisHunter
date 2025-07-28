import requests
import os

# Insira sua API Key do VirusTotal aqui ou defina a variável de ambiente VT_API_KEY
VT_API_KEY = os.getenv("VT_API_KEY", "02f4bfdb0435f5235201013bd18fe7d5b0793f5fd37952eedec138b0560cdd68")

VT_BASE_URL = "https://www.virustotal.com/api/v3"

def check_url_virustotal(url):
    headers = {
        "x-apikey": VT_API_KEY
    }
    # Primeiro, enviar a URL para análise
    response = requests.post(f"{VT_BASE_URL}/urls", headers=headers, data={"url": url})
    if response.status_code == 200:
        analysis_id = response.json()["data"]["id"]
        # Buscar o resultado da análise
        analysis_url = f"{VT_BASE_URL}/analyses/{analysis_id}"
        analysis_response = requests.get(analysis_url, headers=headers)
        if analysis_response.status_code == 200:
            stats = analysis_response.json()["data"]["attributes"]["stats"]
            # Exemplo: {'harmless': 70, 'malicious': 1, 'suspicious': 0, ...}
            return stats
        else:
            return {"error": f"Erro ao buscar análise: {analysis_response.status_code}"}
    else:
        return {"error": f"Erro ao enviar URL: {response.status_code}"}
        