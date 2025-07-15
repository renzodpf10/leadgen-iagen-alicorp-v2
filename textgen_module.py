from transformers import pipeline

# Modelo que sí entiende instrucciones y genera en español
text_generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_product_description(nombre, categoria, caracteristicas, api_token=None):
    prompt = (
        f"Escribe una descripción atractiva en español para un producto llamado '{nombre}', "
        f"de la categoría '{categoria}', con estas características: {caracteristicas}."
    )
    output = text_generator(prompt, max_length=150, do_sample=True, temperature=0.9)
    return output[0]["generated_text"]
