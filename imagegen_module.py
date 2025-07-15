
import requests

def generate_product_image(prompt, api_token):
    api_url = "https://api-inference.huggingface.co/models/prompthero/openjourney"
    headers = {"Authorization": f"Bearer {api_token}"}
    payload = {"inputs": prompt}

    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Error generando imagen: {response.status_code} - {response.text}")
