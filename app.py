
import streamlit as st
import os
from textgen_module import generate_product_description as generate_description
from imagegen_module import generate_image
from feedback_summary_module import summarize_feedback

st.set_page_config(page_title="LeadGen IA Gen – Versión Robusta")

st.title("🚀 LeadGen IA Generativa – Versión Robusta")

tab1, tab2, tab3 = st.tabs(["1. Descripciones", "2. Imágenes", "3. Feedback clientes"])

with tab1:
    st.header("🧠 Generación automática de descripciones")
    product_name = st.text_input("Nombre del producto")
    product_category = st.text_input("Categoría del producto")
    product_features = st.text_area("Características del producto (separadas por comas)")

    if st.button("Generar descripción"):
        description = generate_description(product_name, product_category, product_features)
        st.success("Descripción generada:")
        st.write(description)

with tab2:
    st.header("🎨 Generación de imágenes promocionales")
    prompt = st.text_input("Prompt de imagen promocional")

    if st.button("Generar imagen"):
        image = generate_image(prompt)
        st.image(image, caption="Imagen generada", use_column_width=True)

with tab3:
    st.header("💬 Resumen de feedback de clientes")
    feedback_text = st.text_area("Pega aquí los comentarios o feedback")

    if st.button("Resumir feedback"):
        summary = summarize_feedback(feedback_text)
        st.success("Resumen del feedback:")
        st.write(summary)
