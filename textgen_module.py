import os
import requests
import streamlit as st

def generate_product_description(nombre, categoria, caracteristicas, api_token=None):
    # Usa la clave secreta si no se pasó directamente
    api_key = api_token or st.secrets["openrouter_token"]

    prompt = (
        f"Genera una descripción de producto en español para un producto llamado '{nombre}', "
        f"de la categoría '{categoria}', con estas características: {caracteristicas}. "
        f"Debe ser atractiva y persuasiva."
    )

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "huggingfaceh4/zephyr-7b-beta",
            "messages": [
                {"role": "system", "content": "Eres un experto en marketing de productos saludables. Responde solo en español."},
                {"role": "user", "content": prompt}
            ]
        },
        timeout=30
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error API ({response.status_code}): {response.text}")
