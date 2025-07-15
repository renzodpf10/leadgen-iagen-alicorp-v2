import streamlit as st
import os
from textgen_module import generate_description
from imagegen_module import generate_image
from feedback_summary_module import summarize_feedback

# --------------------------
# Configuración de la página
# --------------------------
st.set_page_config(
    page_title="AI Snack Content Generator",
    page_icon="🍿",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("🍿 LeadGen IA Generativa – Versión API HuggingFace")
st.write("Explora cómo la IA puede acelerar lanzamientos de productos mediante generación de descripciones, feedback e imágenes.")

# --------------------------
# API Key (verifica que esté configurada como variable de entorno)
# --------------------------
if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
    st.warning("No se encontró la API Key de Hugging Face. Por favor configura la variable de entorno HUGGINGFACEHUB_API_TOKEN.")

# --------------------------
# Barra lateral
# --------------------------
modulo = st.sidebar.selectbox(
    "Selecciona módulo",
    ("Descripción de producto", "Resumen de feedback", "Generador de imagen")
)

# --------------------------
# Módulo: Descripción de producto
# --------------------------
if modulo == "Descripción de producto":
    st.header("📝 Generador de Descripción")
    nombre = st.text_input("Nombre del producto", value="Barra de Quinoa con Cacao")
    ingredientes = st.text_input("Ingredientes clave", value="quinoa, cacao, miel")
    beneficio = st.text_input("Beneficio principal", value="energía saludable")
    tono = st.selectbox("Tono", ["amigable", "informativo", "profesional"])

    if st.button("Generar descripción"):
        prompt = f"Redacta una descripción {tono} para un producto llamado '{nombre}' con ingredientes {ingredientes} que brinda {beneficio}."
        resultado = generate_description(prompt)
        st.success("Descripción generada:")
        st.write(resultado)

# --------------------------
# Módulo: Resumen de feedback
# --------------------------
elif modulo == "Resumen de feedback":
    st.header("💬 Resumen de Feedback")
    comentarios = st.text_area("Ingresa comentarios de clientes (uno por línea):")

    if st.button("Generar resumen"):
        resultado = summarize_feedback(comentarios)
        st.success("Resumen:")
        st.write(resultado)

# --------------------------
# Módulo: Generador de imagen
# --------------------------
elif modulo == "Generador de imagen":
    st.header("🖼 Generador de Imágenes Promocionales")
    prompt = st.text_input("Describe la imagen que deseas generar", value="Snack saludable con fondo natural y estilo publicitario")

    if st.button("Generar imagen"):
        with st.spinner("Generando imagen con IA..."):
            image = generate_image(prompt)
            st.image(image, caption="Imagen generada con IA")
