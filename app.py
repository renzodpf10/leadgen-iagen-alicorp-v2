import streamlit as st
from textgen_module import generate_product_description
from imagegen_module import generate_product_image
from feedback_summary_module import summarize_feedback

# (Opcional) Token si usas modelos con autenticación
# api_token = st.secrets["api_token"]
api_token = None  # Usamos modelos gratuitos sin autenticación

st.set_page_config(page_title="Generador IA - Alicorp", layout="centered")

st.title("🤖 Gen AI para productos saludables de Alicorp")

tabs = st.tabs(["📝 Descripción", "💬 Feedback"])

# --- Pestaña 1: Descripción del producto ---
with tabs[0]:
    st.header("📝 Generación de descripción de producto")
    nombre = st.text_input("Nombre del producto")
    categoria = st.text_input("Categoría")
    caracteristicas = st.text_area("Características (separadas por comas)")
    if st.button("Generar descripción"):
        try:
            descripcion = generate_product_description(nombre, categoria, caracteristicas, api_token)
            st.success("Descripción generada:")
            st.write(descripcion)
        except Exception as e:
            st.error(f"Error generando descripción: {e}")

# --- Pestaña 2: Imagen ---
#with tabs[1]:
#    st.header("🎨 Generación de imagen del producto")
 #   prompt = st.text_input("Describe visualmente cómo quieres que sea la imagen")
  #  if st.button("Generar imagen"):
   #     try:
    #        image = generate_product_image(prompt, api_token)
     #       st.image(image, caption="Imagen generada por IA", use_column_width=True)
      #  except Exception as e:
       #     st.error(f"Error generando imagen: {e}")

# --- Pestaña 3: Feedback ---
with tabs[2]:
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
