import replicate

def generate_product_image(prompt, api_token):
    # Inicializa cliente de Replicate con tu token seguro
    client = replicate.Client(api_token=api_token)

    # Ejecuta el modelo SDXL para generar una imagen
    output = client.run(
        "stability-ai/sdxl",  # sin hash: usa la versión activa por defecto
        input={"prompt": prompt}
    )

    return output[0]  # URL de la imagen generada

