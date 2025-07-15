import streamlit as st
from textgen_module import generate_product_description
from feedback_summary_module import summarize_feedback

# Cargar tokens desde secrets
api_token = st.secrets["api_token"]               # HuggingFace
openrouter_token = st.secrets["openrouter_token"] # OpenRouter

st.set_page_config(page_title="Generador IA - Alicorp", layout="centered")
st.title("🤖 Gen AI para productos de Alicorp")

# Pestañas
tabs = st.tabs(["📝 Descripción", "💬 Feedback"])

# --- Pestaña 1: Generación de descripción ---
with tabs[0]:
    st.header("📝 Generación de descripción de producto")
    nombre = st.text_input("Nombre del producto")
    categoria = st.text_input("Categoría")
    caracteristicas = st.text_area("Características (separadas por comas)")

    if st.button("Generar descripción"):
        try:
            descripcion = generate_product_description(nombre, categoria, caracteristicas, openrouter_token)
            st.success("Descripción generada:")
            st.write(descripcion)
        except Exception as e:
            st.error(f"Error generando descripción: {e}")

# --- Pestaña 2: Feedback ---
with tabs[1]:
    st.header("💬 Análisis de feedback de clientes")
    feedback_input = st.text_area("Pega aquí el feedback de los clientes (uno por línea)")

    if st.button("Analizar feedback"):
        try:
            feedback_list = feedback_input.strip().split("\n")
            resumen = summarize_feedback(feedback_list, api_token)
            st.success("Resumen de feedback:")
            st.write(resumen)
        except Exception as e:
            st.error(f"Error analizando feedback: {e}")


