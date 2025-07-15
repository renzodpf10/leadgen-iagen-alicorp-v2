from transformers import pipeline, set_seed

# Usar un modelo de texto más robusto y actualizado
text_generator = pipeline("text-generation", model="gpt2", tokenizer="gpt2")
set_seed(42)

def generate_product_description(nombre, categoria, caracteristicas, api_token=None):
    prompt = (
        f"Imagina un producto innovador llamado '{nombre}', "
        f"de la categoría '{categoria}', con las siguientes características: {caracteristicas}. "
        f"Escribe una descripción creativa y persuasiva para presentarlo al público."
    )

    output = text_generator(
        prompt,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.9,
        pad_token_id=50256  # <- Fix crítico para gpt2
    )
    return output[0]["generated_text"]
