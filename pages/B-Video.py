import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st

# 1. SIEMPRE PRIMERO: Configuración de la página
st.set_page_config(
    page_title="Teorías del Aprendizaje Motor",
    page_icon="🧠",
    layout="wide"
)

# 2. Estilos CSS (opcional, para ajustar el alineamiento vertical)
st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] {
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Encabezado con Logo y Título
col_img, col_title = st.columns([0.2,2])

with col_img:
    # Ajusta el width según cómo se vea mejor en tu pantalla
    st.image("https://raw.githubusercontent.com/Jmontoyaor/motor-control-theories-web/main/Fotos/Brain.png", width=120)

# --- Título Principal ---
with col_title:
    st.title("Teorías del Aprendizaje Motor")

st.markdown("""
Bienvenido al entorno interactivo para el estudio del control motor. Esta sección presenta las teorías fundamentales
que explican la organización del movimiento humano bajo la perspectiva de sistemas complejos y estándares de la APTA.
""")

st.write("---")

# --- Sidebar ---
st.sidebar.image(
    "https://raw.githubusercontent.com/Jmontoyaor/motor-control-theories-web/main/Fotos/Autonoma.png",
    use_container_width=True
)


# --- Estilos CSS Personalizados ---
custom_css = """
<style>
    .stApp {
        background-color: #066BA4;
        color: #E0E0E0;
        font-family: 'Courier New', monospace;
    }

    /* Títulos principales con línea amarilla debajo */
    h1 {
        color: #00BFFF;
        border-bottom: 3px solid #FDE55D;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    /* Subtítulos de sección con línea amarilla debajo */
    h2 {
        color: #00BFFF;
        border-bottom: 2px solid #FDE55D;
        padding-bottom: 5px;
        margin-bottom: 15px;
    }

    h3 {
        color: #00BFFF;
    }

    .main .block-container {
        padding-top: 0.5rem;
        padding-bottom: 2rem;
        background-color: #1B1D2B;
        border-radius: 10px;
    }

    section[data-testid="stSidebar"] {
        background-color: #FDE55D;
        border-radius: 10px;
    }

    section[data-testid="stSidebar"] * {
        color:#416cf2 !important;
    }

    .resultado-final {
        color: #FFD700;
        background-color: #2c3e50;
        border: 1px solid #FFD700;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
        font-size: 1.1rem;
        height: 100px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .nota-info {
        color: #98FB98;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
# --- Sección de Video ---
st.header("Recursos Audiovisuales")

col_vid, col_text = st.columns([1.5, 1])

with col_vid:
    # Definimos el ID y la URL de previsualización (preview)
    video_id = "1u50OLkB9clQCqGTqYebvI20-AyJZF5ps"
    # OJO: Usamos '/preview', no '/view' ni 'export=download'
    embed_url = f"https://drive.google.com/file/d/{video_id}/preview"

    # Usamos st.markdown para renderizar el iframe dentro de tu borde amarillo
    # 'allow="autoplay"' permite que el reproductor de Google funcione correctamente
    st.markdown(f"""
        <div style="border: 2px solid #FDE55D; border-radius: 10px; padding: 10px;">
            <iframe
                src="{embed_url}"
                width="100%"
                height="300"
                frameborder="0"
                allow="autoplay; fullscreen"
                style="border-radius: 5px;">
            </iframe>
        </div>
    """, unsafe_allow_html=True)

with col_text:
    st.subheader("Análisis del Video")
    st.write("""
    En este recurso podrás observar la aplicación práctica de:
    * **Feedforward:** Preparación del movimiento.
    * **Feedback:** Ajustes en tiempo real.
    * **Affordances:** Relación sujeto-entorno.
    """)

    # Botón para abrir externamente
    original_url = f"https://drive.google.com/file/d/{video_id}/view?usp=sharing"
    st.link_button("Abrir en Google Drive", original_url)

st.write("---")