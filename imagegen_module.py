import replicate

def generate_product_image(prompt, api_token):
    client = replicate.Client(api_token=api_token)

    output = client.run(
        "stability-ai/sdxl:db21e45e5d44b85e016e067b8fdfd1be65c6edecb17ee4f9c3c65b0d8305a456",
        input={"prompt": prompt}
    )

    return output[0]  # URL de imagen generada
