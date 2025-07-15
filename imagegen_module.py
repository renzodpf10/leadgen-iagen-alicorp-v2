
import requests
import base64
import os

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
HF_API_KEY = os.getenv("HF_API_KEY")  # Asegúrate de configurar esta variable en el entorno

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def generate_image(prompt: str):
    payload = {
        "inputs": prompt,
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        image_bytes = response.content
        encoded_image = base64.b64encode(image_bytes).decode("utf-8")
        return encoded_image
    else:
        raise ValueError(f"Error generando imagen: {response.status_code} - {response.text}")
