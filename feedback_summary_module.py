import requests

def summarize_feedback(feedback_text, api_token="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"):
    """
    Envía el feedback de los clientes a una API de resumen de texto de HuggingFace.

    Parámetros:
    - feedback_text: texto con los comentarios de los clientes, separados por líneas.
    - api_token: tu token de acceso de HuggingFace (por defecto se pasa uno por seguridad).

    Retorna:
    - Texto con el resumen del feedback.
    """
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {api_token}"}
    payload = {"inputs": feedback_text}

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result[0]["summary_text"]
    else:
        raise Exception(f"Error en la API: {response.status_code} - {response.text}")