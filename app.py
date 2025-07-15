
import streamlit as st
import os
from textgen_module import generate_product_description as generate_description
from imagegen_module import generate_image
from feedback_summary_module import summarize_feedback

st.set_page_config(page_title="LeadGen IA Gen – Versión Robusta", layout="wide")

st.title("🚀 LeadGen IA Gen – Versión Robusta")
st.markdown("App de IA Generativa para acelerar el lanzamiento de snacks saludables – Caso Alicorp")

tabs = st.tabs(["1. Generar descripción", "2. Generar imagen", "3. Resumir feedback"])

with tabs[0]:
    st.header("📝 Generación automática de descripciones de producto")
    product_name = st.text_input("Nombre del producto")
    ingredients = st.text_area("Ingredientes o componentes")
    benefits = st.text_area("Beneficios clave")
    tone = st.selectbox("Tono", ["Creativo", "Emocional", "Informativo"])
    model = st.selectbox("Modelo de lenguaje", ["google/flan-t5-base", "google/flan-t5-large"])
    if st.button("Generar descripción"):
        if product_name and ingredients and benefits:
            description = generate_description(product_name, ingredients, benefits, tone, model)
            st.success("Descripción generada:")
            st.write(description)
        else:
            st.warning("Por favor completa todos los campos.")

with tabs[1]:
    st.header("🖼️ Generación de imagen promocional")
    prompt = st.text_input("Prompt para generar imagen", value="A vibrant promotional photo of a healthy snack made of quinoa and mango")
    negative_prompt = st.text_input("Negative prompt (opcional)", value="blurry, low quality")
    model = st.selectbox("Modelo de difusión", ["stabilityai/stable-diffusion-2-1"])
    if st.button("Generar imagen"):
        if prompt:
            image_url = generate_image(prompt, negative_prompt, model)
            if image_url:
                st.image(image_url, caption="Imagen generada")
            else:
                st.error("Error generando la imagen.")
        else:
            st.warning("Por favor ingresa un prompt.")

with tabs[2]:
    st.header("🗣️ Resumen de feedback de clientes")
    feedback_text = st.text_area("Comentarios o feedback recibido")
    if st.button("Resumir feedback"):
        if feedback_text:
            summary = summarize_feedback(feedback_text)
            st.success("Resumen generado:")
            st.write(summary)
        else:
            st.warning("Por favor ingresa algún feedback.")
