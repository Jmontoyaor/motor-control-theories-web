
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
    st.image("https://raw.githubusercontent.com/Jmontoyaor/motor-control-theories-web/main/Fotos/Fondo.png", width=120)


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


st.header("Cuadro Comparativo de Teorías")

# Definición del CSS para la tabla con líneas amarillas
table_style = """
<style>
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 0.9em;
        font-family: 'Courier New', monospace;
        color: #E0E0E0;
    }
    .custom-table th {
        background-color: #066BA4;
        color: #FDE55D; /* Amarillo */
        text-align: left;
        padding: 12px 15px;
        border-bottom: 3px solid #FDE55D; /* Línea gruesa amarilla */
    }
    .custom-table td {
        padding: 12px 15px;
        border-bottom: 1px solid #FDE55D; /* Línea fina amarilla */
        vertical-align: top;
    }
    .custom-table tr:hover {
        background-color: #2c3e50;
    }
    .feature-col {
        font-weight: bold;
        color: #00BFFF;
        width: 15%;
    }
</style>

<table class="custom-table">
    <thead>
        <tr>
            <th>Característica</th>
            <th>Teoría de Asa Abierta</th>
            <th>Teoría de Asa Cerrada</th>
            <th>Teoría Medioambiental (Ecológica)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="feature-col">Autores</td>
            <td>Richard Schmidt refiere que, en este
sistema, una vez iniciado el movimiento, los procesos de la respuesta llevan a cabo la acción con o sin éxito, pero sin tiempo para generar procesos de feedback. Esta teoría tiene un feedforward donde se debe analizar el objetivo que se tiene planeado para ejecutar como tal la acción, esta teoría no tiene una retroalimentación, no depende totalmente de los estímulos sensoriales.
</td>
            <td>Jack Adams creó un modelo
explicativo de los procesos para el
aprendizaje de las habilidades motrices; Para este autor el papel de la práctica intencional y el conocimiento de los resultados obtenidos, son las claves de un aprendizaje motor sin errores. Existe una retroalimentación, donde hay un inicio y un fin, pero no procesa, no avanza y vuelve al inicio. Esta teoría explica de una buena manera los movimientos que son lentos y regulares.
</td>
            <td>James Gibson explora la forma en que
nuestros sistemas motores nos permiten interactuar más efectivamente con el medio ambiente a fin de tener un comportamiento orientado al objetivo. Su investigación se centró en cómo detectamos la información del entorno pertinente para nuestras acciones y cómo la utilizamos para controlar nuestros movimientos


</td>
        </tr>
        <tr>
            <td class="feature-col">Papel del Cerebro</td>
            <td>Es un ejecutor de órdenes rígidas.</td>
            <td>Es un comparador que corrige errores.</td>
            <td>Es un buscador de información en el entorno.</td>
        </tr>
        <tr>
            <td class="feature-col">Uso de Sensación</td>
            <td>Solo antes de empezar el movimiento.</td>
            <td>Durante todo el movimiento para corregirDurante todo el movimiento para corregir.</td>
            <td> Como guía continúa basada en lo que el entorno permite.</td>
        </tr>
        <tr>
            <td class="feature-col">Velocidad</td>
            <td>Muy rápido (movimientos explosivos).</td>
            <td>Lenta y controlada (movimientos finos).</td>
            <td>Variable según la interacción con el medio.</td>
        </tr>
        <tr>
            <td class="feature-col">Principal Ventaja</td>
            <td>No requiere atención ni tiempo de procesamiento.</td>
            <td>Máxima precisión y corrección de errores.</td>
            <td>Adaptabilidad natural al mundo real sin cómputos complejos.</td>
        </tr>
        <tr>
            <td class="feature-col">Diferencias</td>
            <td>Ejecución de acto motores aprendidos, relativamente automatizados No es imprescindible la información sensorial durante el movimiento La respuesta es preprogramada, antes de que la reacción sea disparada

</td>
            <td>Aprendizaje de tareas motoras nuevas La retroalimentación sensorial es fundamental: pues brinda información visual, vestibular y auditiva para guiar el movimiento hacia el resultado apropiado

</td>
            <td>El ambiente se vuelve ese factor fundamental que determinará la viabilidad de las conductas motrices, por lo que el aprendizaje motor no solo se basará en factores intrínsecos sino también en base a las experiencias y el objetivo que se tenga en la realización de una actividad.</td>
        </tr>
        <tr>
            <td class="feature-col">Limitación</td>
            <td>No puede corregir si algo sale mal.</td>
            <td>Es muy lento para acciones rápidas.</td>
            <td>Menos importancia a los procesos cognitivos internos.</td>
        </tr>
    </tbody>
</table>
"""

st.markdown(table_style, unsafe_allow_html=True)

st.write("---")

