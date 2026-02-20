
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

# Imagen en el sidebar
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

st.write("---")
# --- 1. TEORÍA DE LA ASA ABIERTA ---
st.header("1. TEORÍA DE LA ASA ABIERTA")

# Creamos las columnas FUERA del expander
col1, col2 = st.columns([2, 1])

with col1:
    # El expander solo envuelve el texto técnico
    with st.expander("Ver Fundamentos de la Teoría de Asa Abierta", expanded=False):
        st.subheader("Análisis de la Asa Abierta ")
        st.markdown("""
        La teoría de asa abierta consiste en realizar una acción o actividad de forma rápida y precisa, sin pensar en lo que se está haciendo o se va a hacer.

        Esta teoría cuenta con un enfoque de control llamado FeedForward el cual prepara al cuerpo para adaptarse a las alteraciones del entorno y responder a estos cambios de forma adecuada minimizando el error. Pero al ser movimientos ejecutados rápidamente y sin pensar, si ocurre algún cambio espontáneo en el entorno resultará en un error en la ejecución.
        Al contrario del Feedback, que corrige las alteraciones del movimiento, en asa abierta es algo aprendido y no hay que pensar constantemente en qué se está haciendo para corregir la acción.


        **Puntos Clave:**
        * **Independencia de la Retroalimentación:**  El controlador no utiliza información de retorno (feedback) para verificar si se alcanzó el objetivo deseado. La señal de entrada se envía y el sistema actúa basándose únicamente en esa instrucción previa.

        * **Simplicidad y Eficiencia::** Sistemas valorados por su bajo costo y simplicidad, ideales para procesos bien definidos donde la relación entre entrada y estado resultante es predecible.

        * **Vulnerabilidad a Perturbaciones:** El sistema no puede corregir errores ni compensar disturbios externos. Si ocurre una falla o cambio en el entorno, el controlador no tiene forma de detectarlo y continuará operando desajustado.

        **Relación con la APTA y el Movimiento como Sistema Complejo:**
        Desde la perspectiva de la APTA (American Physical Therapy Association) y el estudio del movimiento humano, la teoría de lazo abierto se asocia con el control anticipatorio (feedforward) y los programas motores preestablecidos:

        * 	Movimiento como Sistema Complejo: El movimiento no es solo una respuesta mecánica, sino una propiedad emergente. El control de lazo abierto explica movimientos demasiado rápidos para que el sistema sensorial procese la retroalimentación y modifique la acción en tiempo real (pestañeo, golpe balístico).

        *	Programación Motora: En fisioterapia, el cerebro envía un “paquete” de instrucciones a los músculos. Si el movimiento es de lazo abierto, el cuerpo ejecuta la acción sin esperar a sentir dónde está el miembro en el espacio hasta que el movimiento termina.

         """)



with col2:
    # Esta columna no se despliega, siempre está visible
    st.markdown("### Ejemplos visuales")

    # --- Primer GIF ---
    st.image(
        "https://raw.githubusercontent.com/Jmontoyaor/motor-control-theories-web/main/Fotos/Pesta%C3%B1eo.gif",
        caption="Pestañeo en slow motion — Control anticipatorio",
        use_container_width=True
    )
    st.caption(
        "Fuente: https://peakd.com/spanish/@jfernandez/una-persona-parpadea-aproximadamente-25-mil-veces-por-semana"
    )

    # --- Segundo GIF ---
    st.image(
        "https://raw.githubusercontent.com/Jmontoyaor/motor-control-theories-web/main/Fotos/Beisbol.gif",
        caption="Lanzamiento de béisbol — Movimiento balístico (teoría de asa abierta)",
        use_container_width=True
    )
    st.caption(
        "Fuente: https://www.drivelinebaseball.com/2021/07/introduction-to-hitting-biomechanics/"
    )

# Este write está fuera del bloque 'with' porque no tiene sangría
st.write("---")
# --- 2. TEORÍA DE LA ASA CERRADA ---
st.header("2. TEORÍA DE LA ASA CERRADA")
col3, col4 = st.columns([2, 1])

with col3:
    with st.expander("Ver Fundamentos de la Teoría de la asa cerrada", expanded=False):
        st.subheader("Análisis de Teoría de la asa cerrada")
        st.markdown("""
**TEORÍA DE LA ASA CERRADA**

1. **Definición y Concepto General**
La teoría de lazo cerrado se centra en el uso de la retroalimentación (feedback) para controlar el movimiento. Funciona como un GPS interno que verifica constantemente si el cuerpo sigue la trayectoria correcta y realiza ajustes en tiempo real. Los movimientos se controlan comparando el estado actual del sistema con un valor de referencia o estado deseado.

2. **Componentes del Sistema**
* **Mecanismo Efector:** Músculos esqueléticos, articulaciones y unidades motoras que ejecutan las órdenes del sistema nervioso central.
* **Mecanismo de Retroalimentación:** Receptores sensoriales que detectan el estado real del movimiento.
* **Mecanismo Comparador:** Contrasta la retroalimentación recibida con el objetivo del movimiento. Si existe discrepancia, genera una señal de error para iniciar acciones correctivas en el efector.

3. **Tipos de Retroalimentación**
* **Intrínseca:** Generada por receptores internos del cuerpo sobre posición, fuerza y movimiento.
* **Extrínseca:** Proviene de fuentes externas, como instrucciones verbales de un fisioterapeuta o video de análisis de marcha.

4. **Integración con el Movimiento y la APTA**
Desde la perspectiva de la APTA y el análisis del movimiento como sistema complejo, la teoría de lazo cerrado es vital en la rehabilitación motora:
* **Sistema Complejo:** El movimiento no depende de un solo comando, sino de la interacción de múltiples subsistemas (sensorial, muscular, ambiental). El lazo cerrado permite que estos subsistemas se autoorganicen mediante el ajuste continuo del error.
* **Aplicación Clínica:** Un fisioterapeuta utiliza el lazo cerrado al proporcionar “pistas verbales” (retroalimentación aumentada) mientras el paciente utiliza su propiocepción para corregir su patrón de marcha en tiempo real.

5. **Limitaciones de la Teoría**
* **Velocidad:** No explica movimientos balísticos o muy rápidos (lanzamiento de béisbol, golpe de artes marciales), donde el feedback no puede ser procesado a tiempo para corregir la acción en curso.
* **Complejidad:** Puede ser menos efectivo en movimientos que involucran múltiples articulaciones y grados de libertad simultáneos.
* **Factores Cognitivos:** No considera plenamente el impacto de la motivación, el miedo o la atención en el control motor.

**Ejemplos de Aplicación**
* **Fisioterapia y rehabilitación:** Un fisioterapeuta proporciona instrucciones verbales (retroalimentación extrínseca aumentada) para ayudar a un paciente a corregir su patrón de marcha, mientras el paciente utiliza su propia propiocepción (retroalimentación intrínseca) para realizar ajustes en tiempo real.
* **Actividades cotidianas:** El uso de los músculos intrínsecos de la mano permite realizar tareas de alta precisión, como escribir con un bolígrafo o tocar un instrumento musical, ajustando la fuerza y posición mediante los receptores sensoriales.
        """)




with col4:
    st.markdown("### Ejemplo visual")
    # Eliminamos el 'with col_center' para que no cause error de identación
    st.image(
        "https://raw.githubusercontent.com/Jmontoyaor/motor-control-theories-web/main/Fotos/marcha.gif",
        caption="Ciclo de la marcha humana — Biomecánica del patrón de caminar",
        use_container_width=True
    )
    st.caption(
        "Fuente original: https://makeagif.com/gif/biomecanica-de-la-marcha-humana-qEAFH5"
    )

st.write("---")

# --- 3. TEORÍA MEDIOAMBIENTAL ---
st.header("3.TEORÍA MEDIOAMBIENTAL")
col5, col6 = st.columns([2, 1])

with col5:
    with st.expander("Ver Fundamentos de la Teoría de Gibson", expanded=False):
        st.subheader("Teoría de la Percepción Ecológica")

        st.markdown("""
        La psicología ecológica de **James J. Gibson** propone que la percepción es un proceso **directo**. A diferencia de las teorías tradicionales, Gibson rechaza la idea de que el cerebro necesite procesar "imágenes" o "sensaciones" indirectas para construir la realidad; en su lugar, sostiene que percibimos el mundo tal cual es.

        Para Gibson, la visión no ocurre de forma aislada, sino que depende de un **sistema visual completo**: ojos integrados en una cabeza, sobre un cuerpo apoyado en el suelo. En este esquema, el cerebro actúa únicamente como el órgano central de un sistema mayor. La información no es simplemente luz, sino el **arreglo óptico ambiental**: una estructura de energía que rodea al observador y especifica el entorno de manera inagotable.



        ### El Concepto de Affordances
        El pilar fundamental de esta teoría son las **affordances** (posibilidades de acción). Estas representan lo que el entorno ofrece al individuo, ya sea para su beneficio o perjuicio. Por ejemplo, una superficie rígida ofrece apoyo, mientras que un objeto pequeño permite ser sujetado.

        Esta relación es **recíproca**: el animal y el entorno forman un par inseparable. Se crea un bucle continuo donde la percepción guía la acción y, a su vez, la acción permite la detección de nueva información.

        ### El Movimiento como Sistema Complejo
        Bajo esta perspectiva, el movimiento se entiende mediante la **teoría de sistemas**. Los sistemas perceptuales no son canales pasivos de sensación, sino actividades del cuerpo completo dedicadas a extraer, aislar o clarificar activamente la estructura informativa del mundo. Percibir es, en esencia, un acto exploratorio.
        """)

with col6:
    st.markdown("### Ejemplo visual")
    st.image(
        "https://raw.githubusercontent.com/Jmontoyaor/motor-control-theories-web/main/Fotos/Subiendo%20escaleras.gif",

        caption="Subida de escaleras — Control motor funcional y ajuste continuo del movimiento",
        use_container_width=True
    )
    st.caption(
        "Fuente original: https://makeagif.com/gif/subiendo-escaleras-ohWJIe"
    )

st.write("---")

# --- CRÉDITOS ---
st.header("Créditos del Proyecto")
col_c1, col_c2 = st.columns(2)

with col_c1:
    st.markdown("""
**Bibliografía Principal**

Gibson, J. J. (1979). *The ecological approach to visual perception*. Boston, MA: Houghton Mifflin.

American Public Transportation Association (APTA). (1999). *Recommended practice for head end power source characteristics* (APTA PR-E-RP-015-99). Washington, DC: APTA Press.

Hoogenboom, B. J. (2022). The movement system and physical therapist practice: What does the future look like? *International Journal of Sports Physical Therapy, 17*(1). https://doi.org/10.26603/001c.30999
    """)

# Columna 2: Integrantes
with col_c2:
    st.markdown("""
    **Equipo de Trabajo**

    * Maria Fernanda Ramírez Osorio
    * Valeria Villegas Gutiérrez
    * Maria Fernanda Montoya Ortiz
    * Francisco Javier Quintero Morales
    """)

st.caption("© 2026  Teorías del Aprendizaje Motor - J.F Montoya")