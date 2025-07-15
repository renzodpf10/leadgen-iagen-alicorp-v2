
import requests

def summarize_feedback(comments: str, api_token: str) -> str:
    url = "https://api-inference.huggingface.co/models/google/flan-t5-small"
    headers = {"Authorization": f"Bearer {api_token}"}
    payload = {"inputs": f"Resume los siguientes comentarios de clientes en insights breves y útiles:\n{comments}"}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result[0]["generated_text"]
    else:
        raise ValueError(f"Error en la API: {response.status_code} - {response.text}")
