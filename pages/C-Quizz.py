import streamlit as st
import time

# --- CONFIGURACIÓN DE PÁGINA Y ESTILOS ---
st.set_page_config(
    layout="wide",
    page_title="Quiz de Teorías del Aprendizaje Motor",
    page_icon="🧠"
)

# CSS personalizado (Exactamente el mismo "ambiente" que me pediste)
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

    .stApp {
        background-color: #066BA4;
        color: #E0E0E0;
        font-family: 'Poppins', sans-serif;
    }

    h1, h2, h3 {
        color: #00BFFF;
        font-family: 'Poppins', sans-serif;
    }

    section[data-testid="stSidebar"] {
        background-color: #FDE55D !important;
        border-radius: 10px;
        font-family: 'Poppins', sans-serif;
    }

    section[data-testid="stSidebar"] * {
        color: #416cf2 !important;
    }

    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: rgba(34, 47, 91, 0.6);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        margin-bottom: 2rem;
        border: 2px solid #FDE55D;
        box-shadow: 0 8px 32px 0 rgba(34, 47, 91, 0.6);
    }

    .quiz-container {
        /* AQUÍ ESTÁ EL CAMBIO: Fondo plano con transparencia en lugar de degradado */
        background: rgba(34, 47, 91, 0.6);

        backdrop-filter: blur(15px);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(0, 191, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(0, 191, 255, 0.1);
    }

    .question-number {
        background: linear-gradient(45deg, #00BFFF, #222f5b);
        color: 066BA4;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 1rem;
        box-shadow: 0 4px 15px rgba(0, 191, 255, 0.3);
    }

    .stRadio > div {
        background: rgba(34, 47, 91, 0.4);
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid rgba(0, 191, 255, 0.2);
        color: #ffffff !important;
    }

    .stRadio > div > label {
        color: #ffffff !important;
    }

    .stRadio > div > label > div {
        color: #ffffff !important;
    }

    .stRadio label {
        color: #ffffff !important;
    }

    div[data-testid="stRadio"] label span {
        color: #ffffff !important;
    }

    div[data-testid="stRadio"] > div > label {
        color: #ffffff !important;
    }

    .result-correct {
        background: linear-gradient(45deg, #00BFFF, #222f5b);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(0, 191, 255, 0.3);
    }

    .result-incorrect {
        background: linear-gradient(45deg, #ff4757, #222f5b);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(255, 71, 87, 0.3);
    }

    .hint-box {
        background: rgba(34, 47, 91, 0.6);
        border-left: 4px solid #00BFFF;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        font-style: italic;
        color: #c6e2ff;
    }

    .score-container {
        text-align: center;
        background: linear-gradient(135deg, #222f5b, #00BFFF);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 8px 32px 0 rgba(0, 191, 255, 0.4);
        border: 2px solid rgba(0, 191, 255, 0.5);
    }

    .stButton > button {
       background: linear-gradient(90deg,rgba(204, 200, 82, 0.55) 0%, rgba(214, 142, 41, 1) 0%, rgba(237, 209, 83, 1) 33%);
        color: white;
        border: #FDE55D;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 191, 255, 0.3);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 191, 255, 0.4);
        background: linear-gradient(45deg, #00BFFF, #222f5b);
    }

    .stProgress > div > div > div {
        background: linear-gradient(90deg, #00BFFF, #222f5b);
    }

    .stMetric {
        background: rgba(34, 47, 91, 0.6);
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #FDE55D;
    }

    .stExpander {
        background: rgba(34, 47, 91, 0.4);
        border: 1px solid #FDE55D;
        border-radius: 10px;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# --- DATOS DEL QUIZ (CONTENIDO ACTUALIZADO: CONTROL MOTOR) ---
quiz_data = {
    "title": "🧠 Quiz Teorías del Aprendizaje Motor",
    "description": "Evalúa tu comprensión sobre los sistemas de Asa Abierta y Cerrada, Feedforward y Feedback.",
    "questions": [
        {
            "id": 1,
            "question": "¿Cuál es la función principal del 'feedforward' en el sistema de asa abierta?",
            "options": [
                "Corregir errores una vez que el movimiento ha finalizado.",
                "Comparar la posición actual con la deseada durante el movimiento.",
                "Preparar al cuerpo anticipando condiciones basadas en experiencia previa.",
                "Eliminar por completo la necesidad de músculos."
            ],
            "correct_answer": 2,
            "explanation": "El feedforward es un mecanismo anticipatorio. Prepara al sistema para perturbaciones conocidas antes de que ocurran, minimizando el error inicial.",
            "hint": "Es un mecanismo de predicción ('hacia adelante'), no de reacción."
        },
        {
            "id": 2,
            "question": "En un movimiento de asa abierta estricto, ¿el cerebro espera información propioceptiva antes de completar la acción?",
            "options": [
                "Sí, el cerebro necesita saber dónde está la mano para terminar.",
                "No, el cerebro envía el paquete completo de instrucciones sin esperar retorno.",
                "Depende de la fatiga muscular.",
                "Sí, pero solo información visual, no propioceptiva."
            ],
            "correct_answer": 1,
            "explanation": "En asa abierta, el programa motor se ejecuta completo sin esperar feedback. Si hubiera espera para corregir, sería asa cerrada.",
            "hint": "Recuerda que el asa abierta opera 'a ciegas' durante la ejecución."
        },
        {
            "id": 3,
            "question": "¿Cuál es la principal DESVENTAJA del sistema de asa abierta?",
            "options": [
                "Es demasiado lento para deportes rápidos.",
                "No puede adaptarse a perturbaciones externas inesperadas durante la ejecución.",
                "Requiere demasiada atención visual.",
                "Requiere retroalimentación constante."
            ],
            "correct_answer": 1,
            "explanation": "Al no usar retroalimentación en tiempo real, si algo cambia en el entorno (ej. un empujón), el sistema no detecta el error y falla.",
            "hint": "Si el plan falla a mitad de camino, el sistema no tiene forma de saberlo."
        },
        {
            "id": 4,
            "question": "¿Cómo funciona el sistema de asa cerrada (analogía)?",
            "options": [
                "Como un disparo de cañón (balístico).",
                "Como un semáforo de tiempos fijos.",
                "Como un GPS interno que compara ruta y destino constantemente.",
                "Como una lista de reproducción de música."
            ],
            "correct_answer": 2,
            "explanation": "El asa cerrada verifica constantemente si el movimiento va por el camino correcto, compara con el objetivo y ajusta errores (como un GPS o termostato).",
            "hint": "Implica medición, comparación y corrección constante."
        },
        {
            "id": 5,
            "question": "¿Cuál de las siguientes actividades es el mejor ejemplo de control de ASA ABIERTA?",
            "options": [
                "Enhebrar una aguja con hilo fino.",
                "Chasquear los dedos.",
                "Dibujar un círculo perfecto muy lentamente.",
                "Caminar sobre una cuerda floja."
            ],
            "correct_answer": 1,
            "explanation": "Chasquear es un movimiento muy rápido (milisegundos). No hay tiempo biológico para procesar feedback y corregir la trayectoria.",
            "hint": "Busca el movimiento más rápido y explosivo."
        },
        {
            "id": 6,
            "question": "Al dibujar un círculo perfecto lentamente, ¿qué característica principal define que sea un sistema de ASA CERRADA?",
            "options": [
                "El uso de retroalimentación visual continua para corregir el trazo.",
                "La velocidad explosiva del movimiento.",
                "La ausencia total de control consciente.",
                "La capacidad de realizarlo con los ojos cerrados sin errores."
            ],
            "correct_answer": 0,
            "explanation": "Como el movimiento es lento, el cerebro tiene tiempo de recibir la información visual (ver el trazo) y corregir la mano si se desvía del círculo ideal.",
            "hint": "Observas constantemente lo que haces para asegurarte de que el círculo no salga chueco."
        },
        {
            "id": 7,
            "question": "Verdadero o Falso: La práctica y experiencia previa mejoran el sistema de asa abierta mediante el feedforward.",
            "options": [
                "Verdadero: La experiencia refina el programa motor inicial.",
                "Falso: El asa abierta nunca puede mejorarse.",
                "Falso: Solo el asa cerrada se beneficia de la práctica.",
                "Verdadero: Pero solo si el movimiento es lento."
            ],
            "correct_answer": 0,
            "explanation": "La experiencia permite al cerebro predecir mejor qué fuerzas serán necesarias (feedforward), haciendo que el comando inicial sea más preciso sin necesidad de feedback.",
            "hint": "Cuantas más veces lanzas una pelota, mejor calculas el peso y la fuerza antes de lanzarla."
        }
    ]
}


# --- INICIALIZACIÓN DEL ESTADO ---
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False

# --- FUNCIONES AUXILIARES ---
def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.show_results = False
    st.session_state.quiz_completed = False

def calculate_score():
    correct = 0
    total = len(quiz_data['questions'])
    for q_id, answer in st.session_state.answers.items():
        question = next(q for q in quiz_data['questions'] if q['id'] == q_id)
        if answer == question['correct_answer']:
            correct += 1
    return correct, total

# --- HEADER ---


st.markdown(f"""
<div class="main-header">
    <h1>{quiz_data['title']}</h1>
    <p>{quiz_data['description']}</p>
</div>
""", unsafe_allow_html=True)

# --- LÓGICA PRINCIPAL DEL QUIZ ---
if not st.session_state.quiz_completed:
    current_q_index = st.session_state.current_question

    if current_q_index < len(quiz_data['questions']):
        question = quiz_data['questions'][current_q_index]

        st.markdown(f"""
        <div class="quiz-container">
            <div class="question-number">Pregunta {current_q_index + 1} de {len(quiz_data['questions'])}</div>
        </div>
        """, unsafe_allow_html=True)

        # Barra de progreso
        progress = (current_q_index + 1) / len(quiz_data['questions'])
        st.progress(progress)

        # Pregunta
        st.markdown(f"""
        <div class="quiz-container">
            <h3>🤔 {question['question']}</h3>
        </div>
        """, unsafe_allow_html=True)

        # Opciones de respuesta
        with st.container():
            # Recuperar respuesta anterior si existe para mantener la selección al volver
            saved_idx = st.session_state.answers.get(question['id'], 0)

            answer = st.radio(
                "Selecciona tu respuesta:",
                options=range(len(question['options'])),
                format_func=lambda x: question['options'][x],
                key=f"q_{question['id']}",
                index=saved_idx if question['id'] in st.session_state.answers else 0
            )

        # Mostrar pista
        with st.expander("💡 Ver pista"):
            st.markdown(f"""
            <div class="hint-box">
                <strong>Pista:</strong> {question['hint']}
            </div>
            """, unsafe_allow_html=True)

        # Botones de navegación
        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            if current_q_index > 0:
                if st.button("⬅️ Anterior", key="prev_btn"):
                    st.session_state.current_question -= 1
                    st.rerun()

        with col3:
            # Texto dinámico del botón
            btn_text = "Finalizar 🏁" if current_q_index == len(quiz_data['questions']) - 1 else "Siguiente ➡️"

            if st.button(btn_text, key="next_btn"):
                # Guardar respuesta
                st.session_state.answers[question['id']] = answer

                if current_q_index == len(quiz_data['questions']) - 1:
                    # Última pregunta - completar quiz
                    st.session_state.quiz_completed = True
                    st.rerun()
                else:
                    # Siguiente pregunta
                    st.session_state.current_question += 1
                    st.rerun()

# --- MOSTRAR RESULTADOS ---
if st.session_state.quiz_completed:
    correct, total = calculate_score()
    percentage = (correct / total) * 100

    # Resultado general
    st.markdown(f"""
    <div class="score-container">
        <h2>🎉 ¡Quiz Completado! 🎉</h2>
        <h1>{correct}/{total}</h1>
        <h3>Puntuación: {percentage:.1f}%</h3>
        <p>{"¡Excelente dominio del tema! 🌟" if percentage >= 80 else "¡Buen trabajo! 👍" if percentage >= 60 else "¡Repasa los conceptos de Feedback! 📚"}</p>
    </div>
    """, unsafe_allow_html=True)

    # Mostrar respuestas detalladas
    st.markdown("## 📋 Revisión Detallada")

    for question in quiz_data['questions']:
        q_id = question['id']
        user_answer = st.session_state.answers.get(q_id, -1)
        is_correct = user_answer == question['correct_answer']

        # Contenedor de pregunta
        st.markdown(f"""
        <div class="quiz-container">
            <h4>Pregunta {q_id}: {question['question']}</h4>
        </div>
        """, unsafe_allow_html=True)

        # Mostrar resultado visual
        if is_correct:
            st.markdown(f"""
            <div class="result-correct">
                ✅ <strong>¡Correcto!</strong><br>
                Tu respuesta: {question['options'][user_answer]}<br>
                <strong>Explicación:</strong> {question['explanation']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-incorrect">
                ❌ <strong>Incorrecto</strong><br>
                Tu respuesta: {question['options'][user_answer] if user_answer >= 0 else "Sin respuesta"}<br>
                Respuesta correcta: <strong>{question['options'][question['correct_answer']]}</strong><br>
                <strong>Explicación:</strong> {question['explanation']}
            </div>
            """, unsafe_allow_html=True)

    # Botón para reiniciar
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔄 Reiniciar Quiz", key="restart_btn"):
            reset_quiz()
            st.rerun()

# --- Sidebar ---
st.sidebar.image(
    "https://raw.githubusercontent.com/Jmontoyaor/motor-control-theories-web/main/Fotos/Autonoma.png",
    use_container_width=True
)

with st.sidebar:
    st.markdown("""
    ###  Estadísticas
    """)

    if st.session_state.quiz_completed:
        correct, total = calculate_score()
        st.metric("Preguntas", f"{total}/{total}")
        st.metric("Aciertos", correct)
        st.metric("Efectividad", f"{(correct/total)*100:.1f}%")
    else:
        answered = len(st.session_state.answers)
        st.metric("Progreso", f"{st.session_state.current_question + 1}/{len(quiz_data['questions'])}")
        st.metric("Respondidas", answered)

    st.markdown("""
    ---
    ### 💡 Consejos
    - **Asa Abierta:** No corrige errores durante la ejecución.
    - **Asa Cerrada:** Usa feedback para corregir.
    - **Feedforward:** Anticipación basada en experiencia.
    """)

    st.markdown("""
    ---
    ### 🎯 Temas Cubiertos
    - Diferencia funcional Open/Closed Loop
    - Rol de la Propiocepción y Visión
    - Feedforward (Anticipación)
    - Ejemplos prácticos (Chasquido vs. Dibujo)
    """)