# 🧠 Lead Gen AI – Solución con Gen AI para Alicorp

Esta solución responde al reto de acelerar el lanzamiento comercial de nuevos productos saludables (snacks) mediante el uso de Inteligencia Artificial Generativa (IAGen), resolviendo los siguientes casos de uso:

1. 📝 **Generación automática de descripciones de producto**
2. 🖼️ (No implementado) Generación visual de imágenes promocionales
3. 💬 **Análisis automatizado de comentarios de usuarios en canales digitales**

---

## 🚀 ¿Qué hace esta aplicación?

Esta es una web app ligera, construida en **Streamlit**, que permite al equipo de marketing o producto:

- Generar descripciones breves y persuasivas para nuevos productos usando un modelo de lenguaje.
- Analizar automáticamente el sentimiento de múltiples comentarios de clientes.
- (opcional) Extensible a imagen si se integra Replicate o Stability.ai correctamente.

---

## 🧩 Estructura de módulos

- `app.py`: interfaz principal en Streamlit.
- `textgen_module.py`: generación de descripciones usando OpenRouter.
- `feedback_summary_module.py`: análisis de feedback con modelo de sentimiento de Hugging Face.
- `requirements.txt`: dependencias necesarias.
- `.streamlit/secrets.toml`: archivo local con tus API keys (NO se sube a GitHub).

---

## 🛠️ Requisitos previos

- Python 3.9 o superior
- Git
- API Key de [OpenRouter](https://openrouter.ai/) (para generación de texto)
- API Key de [HuggingFace](https://huggingface.co/) (opcional si quieres cambiar de modelo para feedback)

---

## 📦 Instalación paso a paso

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/leadgen-iagen-alicorp-v2.git
cd leadgen-iagen-alicorp-v2
```

### 2. Crea un entorno virtual (opcional pero recomendado)

```bash
python -m venv env
source env/bin/activate    # Mac/Linux
env\Scripts\activate.bat   # Windows
```

### 3. Instala dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura tus API Keys

Crea un archivo oculto `.streamlit/secrets.toml` en la raíz del proyecto:

```toml
# .streamlit/secrets.toml

api_token = "TU_TOKEN_DE_HUGGINGFACE"
openrouter_token = "TU_TOKEN_DE_OPENROUTER"
```

### 5. Ejecuta la aplicación

```bash
streamlit run app.py
```

Verás un link local en tu navegador como:  
`http://localhost:8501`

---

## ✅ Casos de uso cubiertos

| Caso de uso | Descripción                                                                 |
|-------------|-----------------------------------------------------------------------------|
| #1          | Generación automática de descripciones atractivas y persuasivas             |
| #2          | ❌ No implementado (fallos con APIs externas para generación de imagen)     |
| #3          | Clasificación de sentimiento de comentarios de usuarios (positivo/negativo) |

---

## 🔍 Modelos utilizados

| Módulo | Modelo | Plataforma |
|--------|--------|------------|
| Copie | `mistralai/mistral-7b-instruct` | OpenRouter |
| Feedback | `finiteautomata/beto-sentiment-analysis` | Hugging Face |

---

## 🧠 Extensiones posibles

- Integrar generación de imágenes con **Replicate** o **Stability AI** (requiere ajuste de versión/token)
- Exportar resultados como CSV o PDF
- Añadir botón para publicar directamente en CMS o redes sociales

---

## 📎 Créditos

Desarrollado por: Renzo Del Pozo Fernández  
Tecnologías: Streamlit · Transformers · OpenRouter · Hugging Face  
Fecha: Julio 2025
