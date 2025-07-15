from transformers import pipeline, set_seed

# Pipeline con modelo gratuito multilingüe (incluye español)
text_generator = pipeline("text-generation", model="tiiuae/falcon-rw-1b")
set_seed(42)

def generate_product_description(nombre, categoria, caracteristicas, api_token=None):
    prompt = (
        f"Escribe una descripción creativa, atractiva y persuasiva en español para promocionar "
        f"un producto llamado '{nombre}', que pertenece a la categoría '{categoria}', "
        f"con estas características: {caracteristicas}."
    )
    output = text_generator(
        prompt,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.9,
        num_return_sequences=1
    )
    return output[0]["generated_text"]
