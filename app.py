import streamlit as st
from transformers import pipeline
from diffusers import StableDiffusionPipeline
import torch

# --------------------------
# Configuración de la página
# --------------------------
st.set_page_config(
    page_title="AI Snack Content Generator",
    page_icon="🍿",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("🍿 LeadGen IA Generativa – Versión Robusta")
st.write("Explora cómo la IA puede acelerar lanzamientos de productos mediante generación de descripciones, feedback e imágenes.")

# --------------------------
# Inicializar modelos
# --------------------------
@st.cache_resource
def load_text_generator():
    return pipeline("text2text-generation", model="google/flan-t5-small")

@st.cache_resource
def load_image_generator():
    return StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16
    ).to("cuda" if torch.cuda.is_available() else "cpu")

text_generator = load_text_generator()
image_generator = load_image_generator()

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
        resultado = text_generator(prompt, max_length=100)[0]['generated_text']
        st.success("Descripción generada:")
        st.write(resultado)

# --------------------------
# Módulo: Resumen de feedback
# --------------------------
elif modulo == "Resumen de feedback":
    st.header("💬 Resumen de Feedback")
    comentarios = st.text_area("Ingresa comentarios de clientes (uno por línea):")

    if st.button("Generar resumen"):
        prompt = f"Resume los siguientes comentarios de clientes en insights breves y útiles:\n{comentarios}"
        resultado = text_generator(prompt, max_length=150)[0]['generated_text']
        st.success("Resumen:")
        st.write(resultado)

# --------------------------
# Módulo: Generador de imagen
# --------------------------
#elif modulo == "Generador de imagen":
 #   st.header("🖼 Generador de Imágenes Promocionales")
  #  prompt = st.text_input("Describe la imagen que deseas generar", value="Snack saludable con fondo natural y estilo publicitario")

   # if st.button("Generar imagen"):
    #    with st.spinner("Generando imagen con IA..."):
     #       image = image_generator(prompt).images[0]
      #      st.image(image, caption="Imagen generada con IA")
