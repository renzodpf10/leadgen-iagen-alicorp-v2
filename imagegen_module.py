import requests
import os

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
HEADERS = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

def generate_image(prompt: str):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})

    if response.status_code == 200:
        return response.content  # Imagen en bytes
    else:
        raise ValueError(f"Error al generar imagen: {response.status_code} - {response.text}")
