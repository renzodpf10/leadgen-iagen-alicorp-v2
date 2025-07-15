import replicate

# Configura tu modelo y versión
REPLICATE_MODEL_ID = "stability-ai/sdxl"
REPLICATE_MODEL_VERSION = "db21e45d55d56b8cfa6507cd8e6c6c7b95f33b7b4eb6fc1c27c9423b6f1c1844"

def generate_product_image(prompt, replicate_token):
    try:
        output = replicate.run(
            f"{REPLICATE_MODEL_ID}:{REPLICATE_MODEL_VERSION}",
            input={"prompt": prompt},
            api_token=replicate_token
        )
        return output[0]  # URL de la imagen
    except Exception as e:
        raise Exception(f"Error generando imagen: {e}")

