from transformers import pipeline

# Modelo instructivo en español (mejorado)
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_product_description(nombre, categoria, caracteristicas, api_token=None):
    prompt = (
        f"Genera una descripción creativa y persuasiva en español para un producto llamado '{nombre}', "
        f"de la categoría '{categoria}', con estas características: {caracteristicas}."
    )
    output = generator(prompt, max_new_tokens=100)[0]['generated_text']
    return output
