from transformers import pipeline, set_seed

# Pipeline con modelo gratuito en español
text_generator = pipeline("text-generation", model="datificate/gpt2-small-spanish")
set_seed(42)

def generate_product_description(nombre, categoria, caracteristicas, api_token=None):
    prompt = (
        f"Imagina un producto innovador llamado {nombre}, "
        f"de la categoría {categoria}, con estas características: {caracteristicas}. "
        f"Escribe una descripción creativa, atractiva y persuasiva en español para promocionarlo."
    )
    output = text_generator(prompt, max_new_tokens=100, do_sample=True, temperature=0.9, num_return_sequences=1)
    return output[0]["generated_text"]
