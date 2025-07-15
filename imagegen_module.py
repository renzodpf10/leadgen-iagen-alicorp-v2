import requests

def generate_product_image(prompt, stability_token):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    headers = {
        "Authorization": f"Bearer {stability_token}",
        "Content-Type": "application/json"
    }

    data = {
        "text_prompts": [
            {
                "text": prompt
            }
        ],
        "cfg_scale": 7,
        "height": 512,
        "width": 512,
        "samples": 1,
        "steps": 30
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        image_data = response.json()
        image_url = image_data["artifacts"][0]["url"]
        return image_url
    else:
        raise Exception(f"Error generando imagen: {response.status_code} - {response.text}")


