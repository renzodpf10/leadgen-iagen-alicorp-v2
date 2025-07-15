api_token = "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"


import requests
import os

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}

def summarize_feedback(comentarios: str) -> str:
    response = requests.post(API_URL, headers=headers, json={"inputs": comentarios})
    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and "summary_text" in result[0]:
            return result[0]["summary_text"]
        else:
            return "⚠️ No se pudo generar un resumen válido."
    else:
        return f"⚠️ Error en la API: {response.status_code} - {response.text}"
