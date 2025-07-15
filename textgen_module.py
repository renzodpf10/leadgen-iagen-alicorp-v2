from transformers import pipeline

text_generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_product_description(nombre, categoria, caracteristicas, api_token=None):
    prompt = (
        f"INSTRUCCIÓN: Genera una descripción publicitaria en español.\n\n"
        f"Producto: {nombre}\n"
        f"Categoría: {categoria}\n"
        f"Características: {caracteristicas}\n\n"
        f"RESPUESTA:"
    )
    output = text_generator(prompt, max_length=200, do_sample=True, temperature=0.9)
    return output[0]["generated_text"].replace(prompt, "").strip()
