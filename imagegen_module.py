import replicate

def generate_product_image(prompt, replicate_token):
    # Define el modelo de texto-a-imagen de Replicate (Stable Diffusion Turbo o SDXL)
    model = "stability-ai/sdxl"

    try:
        output = replicate.run(
            f"{model}:latest",
            input={"prompt": prompt},
            api_token=replicate_token
        )
        return output[0]  # URL de la imagen generada
    except Exception as e:
        raise Exception(f"Error generando imagen: {e}")

