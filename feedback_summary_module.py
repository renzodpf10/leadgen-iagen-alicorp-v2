
import requests

def summarize_feedback(comments: str, api_token: str) -> str:
    url = "https://api-inference.huggingface.co/models/google/flan-t5-small"
    headers = {"Authorization": f"Bearer {api_token}"}
    prompt = f"Resume los siguientes comentarios de clientes en insights breves y útiles:\n{comments}"

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        if isinstance(result, list) and 'generated_text' in result[0]:
            return result[0]['generated_text']
        else:
            return "No se pudo generar el resumen."
    except Exception as e:
        return f"Error generando resumen: {str(e)}"
