
import streamlit as st
from textgen_module import generate_product_description
from imagegen_module import generate_image
from feedback_summary_module import summarize_feedback

# Token actualizado
API_TOKEN = "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"

# Configuración de la página
st.set_page_config(
    page_title="AI Snack Content Generator",
    page_icon="🍿",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("🍿 LeadGen IA Generativa – Versión Robusta")
st.write("Explora cómo la IA puede acelerar lanzamientos de productos mediante generación de descripciones, feedback e imágenes.")

# Selección de módulo
modulo = st.sidebar.selectbox(
    "Selecciona módulo",
    ("Descripción de producto", "Resumen de feedback", "Generador de imagen")
)

# Módulo: Descripción de producto
if modulo == "Descripción de producto":
    st.header("📝 Generador de Descripción")
    nombre = st.text_input("Nombre del producto", value="Barra de Quinoa con Cacao")
    categoria = st.text_input("Categoría del producto", value="snack saludable")
    atributos = st.text_input("Características o ingredientes", value="quinoa, cacao, miel")

    if st.button("Generar descripción"):
        try:
            descripcion = generate_product_description(nombre, categoria, atributos, API_TOKEN)
            st.success("Descripción generada:")
            st.write(descripcion)
        except Exception as e:
            st.error(f"Error generando descripción: {e}")

# Módulo: Resumen de feedback
elif modulo == "Resumen de feedback":
    st.header("💬 Resumen de Feedback")
    comentarios = st.text_area("Ingresa comentarios de clientes (uno por línea):")

    if st.button("Generar resumen"):
        try:
            resumen = summarize_feedback(comentarios, API_TOKEN)
            st.success("Resumen generado:")
            st.write(resumen)
        except Exception as e:
            st.error(f"Error analizando feedback: {e}")

# Módulo: Generador de imagen
elif modulo == "Generador de imagen":
    st.header("🖼 Generador de Imágenes Promocionales")
    prompt = st.text_input("Describe la imagen que deseas generar", value="Snack saludable con fondo natural y estilo publicitario")

    if st.button("Generar imagen"):
        try:
            imagen_url = generate_image(prompt, API_TOKEN)
            if imagen_url:
                st.image(imagen_url, caption="Imagen generada con IA")
            else:
                st.warning("No se pudo generar la imagen.")
        except Exception as e:
            st.error(f"Error generando imagen: {e}")
