import streamlit as st
from textgen_module import text_generator
from imagegen_module import load_image_generator

# -------------------------
# Título
# -------------------------
st.title("🍟 LeadGen IA Generativa – Versión Robusta")
st.markdown("Explora cómo la IA puede acelerar lanzamientos de productos mediante generación de descripciones, feedback e imágenes.")

# -------------------------
# Selector de módulo
# -------------------------
modulo = st.sidebar.selectbox("Selecciona módulo", ["Generador de contenido", "Resumen de feedback", "Generador de imagen"])

# -------------------------
# Módulo: Generador de contenido
# -------------------------
if modulo == "Generador de contenido":
    st.header("📝 Generador de Contenido de Producto")
    descripcion_producto = st.text_input("Ingresa el tipo de snack saludable y sus ingredientes:")

    if st.button("Generar contenido"):
        prompt = f"Genera una descripción creativa y persuasiva para un nuevo producto de snack saludable: {descripcion_producto}"
        resultado = text_generator(prompt, max_length=150)[0]['generated_text']
        st.success("Contenido generado:")
        st.write(resultado)

# -------------------------
# Módulo: Resumen de feedback
# -------------------------
elif modulo == "Resumen de feedback":
    st.header("🗣️ Resumen de Feedback")
    comentarios = st.text_area("Ingresa comentarios de clientes (uno por línea):")

    if st.button("Generar resumen"):
        prompt = f"Resume los siguientes comentarios de clientes en insights breves y útiles:\n{comentarios}"
        resultado = text_generator(prompt, max_length=150)[0]['generated_text']
        st.success("Resumen:")
        st.write(resultado)

# -------------------------
# Módulo: Generador de imagen
# -------------------------
elif modulo == "Generador de imagen":
    st.header("🖼️ Generador de Imágenes Promocionales")
    prompt = st.text_input("Describe la imagen que deseas generar", value="Snack saludable con fondo natural y estilo publicitario")

    if st.button("Generar imagen"):
        with st.spinner("Generando imagen con IA..."):
            image = load_image_generator(prompt)
            st.image(image, caption="Imagen generada con IA")
