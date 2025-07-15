import requests

def generate_product_description(nombre, categoria, caracteristicas, api_token):
    prompt = (
        f"Genera una descripción breve, creativa y persuasiva en español para un producto llamado '{nombre}', "
        f"de la categoría '{categoria}', con estas características: {caracteristicas}."
    )

    headers = {
        "Authorization": f"Bearer {api_token}",
        "HTTP-Referer": "https://ali-genai-demo.streamlit.app",  # Cambia si tienes otro dominio
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        generated_text = response.json()["choices"][0]["message"]["content"]
        return generated_text

    except requests.exceptions.RequestException as e:
        return f"Error API ({response.status_code}): {response.text}"
