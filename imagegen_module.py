import requests

def generate_product_image(prompt, api_token):
    url = "https://openrouter.ai/api/v1/images/generations"
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "HTTP-Referer": "https://leadgen-iagen-alicorp-v2.streamlit.app",  # ¡Este debe coincidir con tu app!
        "Content-Type": "application/json"
    }

    data = {
        "model": "stabilityai/sdxl-turbo",
        "prompt": prompt,
        "num_images": 1,
        "size": "512x512"
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()["data"][0]["url"]
    else:
        raise Exception(f"Error generando imagen: {response.status_code} - {response.text}")
