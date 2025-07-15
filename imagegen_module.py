import requests

def generate_product_image(prompt, api_token):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-512-v2-1/text-to-image"
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    data = {
        "text_prompts": [{"text": prompt}],
        "cfg_scale": 7,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 512,
        "width": 512,
        "samples": 1,
        "steps": 30
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        image_bytes = response.json()['artifacts'][0]['base64']
        image_url = f"data:image/png;base64,{image_bytes}"
        return image_url
    else:
        raise Exception(f"Error generando imagen: {response.status_code} - {response.text}")

