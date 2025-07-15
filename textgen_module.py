import requests
import json

# Modelo en español fine-tuned para generación instructiva
MODEL_URL = "https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-summarize-news-es"

def generate_product_description(nombre, categoria, caracteristicas, api_token):
    prompt = (
        f"Genera una descripción creativa, persuasiva y en español para un producto llamado '{nombre}', "
        f"de la categoría '{categoria}', con estas características: {caracteristicas}."
    )

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "do_sample": True,
            "temperature": 0.9
        }
    }

    try:
        response = requests.post(MODEL_URL, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            result = response.json()
            return result[0]["generated_text"]
        else:
            raise Exception(f"Error API ({response.status_code}): {response.text}")

    except Exception as e:
        raise Exception(f"No se pudo generar la descripción. Detalle técnico: {e}")
