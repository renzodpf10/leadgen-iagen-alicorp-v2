from transformers import pipeline, set_seed

# Cargar pipeline de generación de texto más creativo
text_generator = pipeline("text-generation", model="gpt2")
set_seed(42)

def generate_product_description(nombre, categoria, caracteristicas, api_token=None):
    prompt = (
        f"Imagina un producto innovador llamado {nombre}, "
        f"de la categoría {categoria}, con las siguientes características: {caracteristicas}. "
        f"Escribe una descripción creativa y persuasiva para presentarlo al público."
    )
    output = text_generator(prompt, max_length=150, do_sample=True, temperature=0.9, num_return_sequences=1)
    return output[0]["generated_text"]
