
import streamlit as st
import os

from textgen_module import generate_product_description as generate_description
from imagegen_module import generate_image
from feedback_summary_module import summarize_feedback

st.set_page_config(page_title="LeadGen IA Gen – Versión Robusta")

st.title("📦 LeadGen IA Gen – Versión Robusta")

tabs = st.tabs(["Descripciones", "Imágenes", "Feedback clientes"])

with tabs[0]:
    st.header("🧠 Generación automática de descripciones")
    product_name = st.text_input("Nombre del producto")
    product_category = st.text_input("Categoría del producto")
    product_features = st.text_area("Características del producto (separadas por comas)")

    if st.button("Generar descripción"):
        if product_name and product_category and product_features:
            try:
                description = generate_description(product_name, product_category, product_features)
                st.success("Descripción generada:")
                st.write(description)
            except Exception as e:
                st.error(f"Error generando descripción: {e}")
        else:
            st.warning("Por favor completa todos los campos.")

with tabs[1]:
    st.header("🎨 Generación automática de imágenes")
    image_prompt = st.text_input("Describe la imagen que deseas generar")

    if st.button("Generar imagen"):
        if image_prompt:
            try:
                image_url = generate_image(image_prompt)
                st.image(image_url, caption="Imagen generada", use_column_width=True)
            except Exception as e:
                st.error(f"Error generando imagen: {e}")
        else:
            st.warning("Por favor ingresa una descripción para la imagen.")

with tabs[2]:
    st.header("💬 Resumen de feedback de clientes")
    feedback_text = st.text_area("Pega aquí comentarios de clientes (uno por línea)")

    if st.button("Generar resumen"):
        if feedback_text:
            try:
                summary = summarize_feedback(feedback_text)
                st.success("Resumen generado:")
                st.write(summary)
            except Exception as e:
                st.error(f"Error generando resumen de feedback: {e}")
        else:
            st.warning("Por favor ingresa al menos un comentario.")
