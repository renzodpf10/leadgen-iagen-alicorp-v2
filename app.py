
import streamlit as st
import os
from textgen_module import generate_product_description as generate_description
from imagegen_module import generate_image
from feedback_summary_module import summarize_feedback

st.set_page_config(page_title="LeadGen IA Gen – Versión Robusta", layout="centered")

st.title("🧠 LeadGen IA Gen – Versión Robusta")
st.markdown("App de IA Generativa para acelerar el lanzamiento de snacks saludables – Caso Alicorp")

st.sidebar.header("Opciones")
section = st.sidebar.radio("Selecciona una función:", ("1. Generar Descripción", "2. Generar Imagen", "3. Resumir Feedback"))

if section == "1. Generar Descripción":
    st.header("📝 Generación automática de descripciones de producto")
    prompt = st.text_area("Describe el producto o proporciona un prompt base", height=150)
    if st.button("Generar descripción"):
        if prompt.strip():
            with st.spinner("Generando descripción..."):
                description = generate_description(prompt)
            st.success("Descripción generada:")
            st.write(description)
        else:
            st.warning("Por favor ingresa un prompt.")

elif section == "2. Generar Imagen":
    st.header("🖼️ Generación de imagen a partir de prompt")
    prompt = st.text_area("Describe la imagen deseada para el producto", height=150)
    if st.button("Generar imagen"):
        if prompt.strip():
            with st.spinner("Generando imagen..."):
                image_path = generate_image(prompt)
            st.image(image_path, caption="Imagen generada", use_column_width=True)
        else:
            st.warning("Por favor ingresa un prompt.")

elif section == "3. Resumir Feedback":
    st.header("💬 Resumen de comentarios o feedback inicial de clientes")
    feedback = st.text_area("Pega aquí comentarios o feedback de clientes", height=200)
    if st.button("Resumir feedback"):
        if feedback.strip():
            with st.spinner("Generando resumen..."):
                summary = summarize_feedback(feedback)
            st.success("Resumen generado:")
            st.write(summary)
        else:
            st.warning("Por favor ingresa el feedback.")
