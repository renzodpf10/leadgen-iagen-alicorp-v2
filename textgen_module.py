from transformers import pipeline, set_seed

# Modelo gratuito en español
text_generator = pipeline("text-generation", model="datificate/gpt2-small-spanish")
set_seed(42)

def generate_product_description(nombre, categoria, caracteristicas, api_token=None):
    prompt = (
        f"Producto: {nombre}\n"
        f"Categoría: {categoria}\n"
        f"Características: {caracteristicas}\n\n"
        f"Descripción en español:"
    )
    output = text_generator(
        prompt,
        max_new_tokens=60,
        do_sample=True,
        temperature=0.7,
        num_return_sequences=1
    )
    return output[0]["generated_text"]
