import requests

def generate_product_description(nombre, categoria, caracteristicas, api_token):
    if not api_token:
        raise ValueError("API token es requerido para usar la API de Hugging Face.")

    # Preparar el prompt
    prompt = (
        f"Genera una descripción breve, creativa y persuasiva en español para un producto llamado '{nombre}', "
        f"de la categoría '{categoria}', con estas características: {caracteristicas}."
    )

    # Llamada a Hugging Face Inference API
    API_URL = "https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-summarize-news"
    headers = {"Authorization": f"Bearer {api_token}"}
    payload = {"inputs": prompt, "parameters": {"max_length": 100, "do_sample": True}}

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        raise Exception(f"Error API ({response.status_code}): {response.text}")
