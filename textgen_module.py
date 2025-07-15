import requests

# Endpoint del modelo (instructivo, español, gratuito)
API_URL = "https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-summarize-news"

def generate_product_description(nombre, categoria, caracteristicas, api_token):
    headers = {"Authorization": f"Bearer {api_token}"}

    prompt = (
        f"Genera una descripción creativa, breve y persuasiva en español para un producto llamado '{nombre}', "
        f"que pertenece a la categoría '{categoria}', con estas características: {caracteristicas}."
    )

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 100,
            "temperature": 0.7,
            "do_sample": True
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

    if isinstance(result, dict) and result.get("error"):
        raise ValueError(f"Error en la API: {result['error']}")

    return result[0]["generated_text"]
