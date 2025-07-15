import requests

def generate_product_image(prompt, stability_token):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-v1-5/text-to-image"

    headers = {
        "Authorization": f"Bearer {stability_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "cfg_scale": 7,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 512,
        "width": 512,
        "samples": 1,
        "steps": 30,
        "text_prompts": [
            {
                "text": prompt,
                "weight": 1
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Error generando imagen: {response.status_code} - {response.text}")

    data = response.json()
    image_base64 = data["artifacts"][0]["base64"]

    # Devolver imagen en formato compatible con Streamlit
    return f"data:image/png;base64,{image_base64}"
