from transformers import pipeline

# Cargar pipeline con modelo Flan-T5 para tareas instructivas
text_generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_product_description(nombre, categoria, caracteristicas, api_token=None):
    prompt = (
        f"Escribe una descripción creativa y atractiva para un producto llamado '{nombre}', "
        f"que pertenece a la categoría '{categoria}', con las siguientes características: {caracteristicas}."
    )
    output = text_generator(prompt, max_length=200, do_sample=True, temperature=0.9)
    return output[0]["generated_text"]
