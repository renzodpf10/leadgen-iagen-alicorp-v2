import replicate

def generate_product_image(prompt, api_token):
    # Inicializa cliente de Replicate con tu token seguro
    client = replicate.Client(api_token=api_token)

    # Ejecuta el modelo SDXL para generar una imagen a partir del prompt
    output = client.run(
        "stability-ai/sdxl:fb0dbe8cbefaa35e6a3a77c0f6b7f20b6c3f21e8d65ebde023fddccf77f4c3e8",
        input={"prompt": prompt}
    )

    # Devuelve la URL de la imagen generada
    return output[0]

