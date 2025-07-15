import requests

def generate_product_description(nombre, categoria, caracteristicas, api_token):
    prompt = (
        f"Genera una descripción breve, persuasiva y en español para un producto llamado '{nombre}', "
        f"que pertenece a la categoría '{categoria}' y tiene las siguientes características: {caracteristicas}."
    )

    api_url = "https://api-inference.huggingface.co/models/tiiuae/falcon-rw-1b"
    headers = {"Authorization": f"Bearer {api_token}"}

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "do_sample": True,
            "temperature": 0.7
        }
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        else:
            return "Error: No se obtuvo un texto generado válido."
    else:
        return f"No se pudo generar la descripción. Detalle técnico: Error API ({response.status_code}): {res_
