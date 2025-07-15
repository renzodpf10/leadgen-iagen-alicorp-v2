from transformers import pipeline

# Cargar pipeline de generación de texto con un modelo preentrenado (como Flan-T5)
text_generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_product_description(nombre, categoria, caracteristicas, api_token=None):
    prompt = (
        f"Escribe una descripción atractiva para un producto llamado '{nombre}', "
        f"de la categoría '{categoria}', con las siguientes características: {caracteristicas}."
    )
    result = text_generator(prompt, max_length=200, do_sample=True)[0]["generated_text"]
    return result
