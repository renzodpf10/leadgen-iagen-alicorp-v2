# 🧠 LeadGen IA Gen – Versión Robusta

App web ligera creada con Streamlit + modelos preentrenados de IA Generativa para acelerar el lanzamiento de nuevos productos (snacks saludables).

---

## 🎯 Objetivo

Demostrar cómo la IA Generativa puede:

1. Automatizar la creación de descripciones de producto.
2. Generar imágenes promocionales atractivas.
3. Resumir de forma rápida comentarios iniciales de clientes.

---

## 🛠 ¿Qué tecnologías usamos?

- **Streamlit:** Framework para apps web ligeras.
- **Transformers - HuggingFace:** Para generación de texto multilingüe (modelo `flan-t5-small`).
- **Diffusers - HuggingFace:** Para generación de imágenes desde texto (modelo `Stable Diffusion`).
- **Torch:** Backend de inferencia.

---

## ⚙️ Funcionalidades

| Módulo                      | Descripción                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| ✍️ Generador de Descripciones | A partir de nombre, ingredientes y beneficios. IA genera copy publicitario. |
| 💬 Resumen de Feedback       | Recibe múltiples opiniones y genera insight clave en segundos.              |
| 🖼 Generador de Imágenes     | Prompt en español → Imagen atractiva (Stable Diffusion).                     |

---

## 🚀 Cómo usar

1. Sube este repo a tu cuenta de GitHub.
2. Conéctalo a [streamlit.io/cloud](https://streamlit.io/cloud).
3. ¡Ejecuta la app directamente desde la web!

---

## 📌 Requisitos

En `requirements.txt` encontrarás las librerías necesarias para que funcione correctamente en Streamlit Cloud.

---

## 📬 Autor

Desarrollado por Renzo Del Pozo Fernández para proceso de selección **Alicorp – Lead Gen AI**.
