
import streamlit as st
import os
from textgen_module import generate_product_description as generate_description
from imagegen_module import generate_image
from feedback_summary_module import summarize_feedback

st.set_page_config(page_title="LeadGen IA Gen – Versión Robusta", layout="wide")

st.title("🧠 LeadGen IA Gen – Versión Robusta")

tabs = st.tabs(["Descripciones", "Imágenes", "Feedback clientes"])

with tabs[0]:
    st.header("🧠 Generación automática de descripciones")
    product_name = st.text_input("Nombre del producto")
    product_category = st.text_input("Categoría del producto")
    product_features = st.text_area("Características del producto (separadas por comas)")

    if st.button("Generar descripción"):
        with st.spinner("Generando descripción..."):
            try:
                prompt = f"Nombre del producto: {product_name}\nCategoría: {product_category}\nCaracterísticas: {product_features}"
                description = generate_description(prompt)
                st.success("Descripción generada:")
                st.write(description)
            except Exception as e:
                st.error(f"Error generando descripción: {e}")

with tabs[1]:
    st.header("🖼 Generación automática de imágenes")
    prompt = st.text_input("Ingresa el prompt para la imagen")
    if st.button("Generar imagen"):
        with st.spinner("Generando imagen..."):
            try:
                image = generate_image(prompt)
                st.image(image, caption="Imagen generada")
            except Exception as e:
                st.error(f"Error generando imagen: {e}")

with tabs[2]:
    st.header("💬 Análisis de feedback de clientes")
    feedback_input = st.text_area("Pega aquí el feedback de los clientes (uno por línea)")
    if st.button("Analizar feedback"):
        with st.spinner("Analizando feedback..."):
            try:
                feedback_list = feedback_input.strip().split("\n")
                summary = summarize_feedback(feedback_list)
                st.success("Resumen de feedback:")
                st.write(summary)
            except Exception as e:
                st.error(f"Error analizando feedback: {e}")
