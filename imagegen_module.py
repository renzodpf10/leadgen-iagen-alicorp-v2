import replicate

def generate_product_image(prompt, replicate_token):
    try:
        # Inicializar cliente Replicate con tu token
        client = replicate.Client(api_token=replicate_token)

        # Usar modelo SDXL Turbo
        output = client.run(
            "stability-ai/sdxl:4e47e5c5b3f6975f5090f32e6a90e0ffad0ba46e5887c0610f82d60a5efb372d",
            input={"prompt": prompt}
        )

        return output[0]  # Devuelve la URL de la imagen generada
    except Exception as e:
        raise Exception(f"Error generando imagen: {e}")
