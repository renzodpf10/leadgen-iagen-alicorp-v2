from transformers import pipeline

# Cargar pipeline de generación de texto con un modelo preentrenado (como Flan-T5)
text_generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_product_description(prompt):
    result = text_generator(prompt, max_length=100, do_sample=True)[0]["generated_text"]
    return result
