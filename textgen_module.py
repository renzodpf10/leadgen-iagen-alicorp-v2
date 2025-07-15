
from transformers import pipeline

# Cargar pipeline de generación de texto con un modelo preentrenado (como Flan-T5)
text_generator = pipeline("text2text-generation", model="google/flan-t5-base")
