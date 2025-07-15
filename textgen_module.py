import requests

API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-rw-1b"

def generate_product_description(nombre, categoria, caracteristicas, api_token=None):
    headers = {"Authorization": f"Bearer {api_token}"} if api_token else {}

    prompt = (
        f"Escribe una descripción breve, creativa y en español para un snack saludable "
        f"llamado '{nombre}', de la categoría '{categoria}', con estas características: {caracteristicas}."
    )

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "do_sample": True,
            "temperature": 0.8
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        result = response.json()
        if isinstance(result, list) and 'generated_text' in result[0]:
            return result[0]['generated_text']
        elif isinstance(result, dict) and 'error' in result:
            raise ValueError(f"Error de modelo: {result['error']}")
        else:
            raise ValueError("Respuesta inesperada del modelo.")
    except Exception as e:
        raise ValueError(f"No se pudo generar la descripción. Detalle técnico: {e}")
