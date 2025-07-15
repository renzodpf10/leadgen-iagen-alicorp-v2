
import requests
import os

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
API_TOKEN = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def generate_product_description(prompt: str) -> str:
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        generated_text = response.json()[0]["generated_text"]
        return generated_text
    else:
        return f"Error {response.status_code}: {response.text}"
