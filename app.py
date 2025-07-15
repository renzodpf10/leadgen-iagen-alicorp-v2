
import streamlit as st
from textgen_module import generate_product_description
from imagegen_module import generate_product_image
from feedback_summary_module import summarize_feedback

# Obtener el token de los secretos
api_token = st.secrets["api_token"]

# Interfaz
st.set_page_config(page_title="LeadGen IA Gen – Versión Robusta", layout="wide")
st.title("🧠 LeadGen IA Gen – Versión Robusta")

tabs = st.tabs(["Descripciones", "Imágenes", "Feedback clientes"])

# --- Pestaña 1: Descripciones ---
with tabs[0]:
    st.header("📝 Generación automática de descripciones")
    nombre = st.text_input("Nombre del producto", "")
    categoria = st.text_input("Categoría del producto", "")
    caracteristicas = st.text_area("Características del producto (separadas por comas)", "")
    if st.button("Generar descripción"):
        try:
            descripcion = generate_product_description(nombre, categoria, caracteristicas, api_token)
            st.success("Descripción generada:")
            st.write(descripcion)
        except Exception as e:
            st.error(f"Error generando descripción: {e}")

# --- Pestaña 2: Imágenes ---
with tabs[1]:
    st.header("🧿 Generación automática de imágenes")
    prompt = st.text_input("Ingresa el prompt para la imagen", "")
    if st.button("Generar imagen"):
        try:
            image_url = generate_product_image(prompt, api_token)
            st.image(image_url, caption="Imagen generada", use_column_width=True)
        except Exception as e:
            st.error(f"Error generando imagen: {e}")

# --- Pestaña 3: Feedback ---
with tabs[2]:
    st.header("💬 Análisis de feedback de clientes")
    feedback_input = st.text_area("Pega aquí el feedback de los clientes (uno por línea)")
    if st.button("Analizar feedback"):
        try:
            resumen = summarize_feedback(feedback_input, api_token)
            st.success("Resumen de feedback:")
            st.write(resumen)
        except Exception as e:
            st.error(f"Error analizando feedback: {e}")
