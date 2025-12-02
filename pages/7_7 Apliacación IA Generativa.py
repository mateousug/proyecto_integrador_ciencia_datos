import streamlit as st
import google.generativeai as genai
import pandas as pd
from utils.data_loader import load_champions_data, prepare_data

st.set_page_config(page_title="IA Generativa", page_icon="🤖")

st.title("🤖 Asistente de IA (Gemini)")

st.markdown("""
Utiliza el poder de la Inteligencia Artificial Generativa para explorar los datos, 
obtener explicaciones y generar insights profundos sobre la Champions League.
""")

# Configuración de API Key
try:
    api_key = st.secrets.get("gemini_api_key", None)
except Exception:
    api_key = None

# Si no está en secrets, permitir ingresarla manualmente
if not api_key:
    with st.expander("⚙️ Configurar API Key de Gemini"):
        st.markdown("""
        1. Obtén tu API Key en: https://aistudio.google.com/apikey
        2. Ingresa aquí tu clave (solo durante esta sesión)
        """)
        api_key = st.text_input("API Key de Gemini:", type="password", key="gemini_key_input")
        
        if not api_key:
            st.info("💡 También puedes guardar la clave en `.streamlit/secrets.toml`:\n```\ngemini_api_key = \"TU_API_KEY\"\n```")

if not api_key:
    st.warning("⚠️ Se requiere una API Key para usar el asistente de IA")
    st.stop()

# Configurar Gemini
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"Error al configurar Gemini: {str(e)}")
    st.stop()

# Cargar contexto de datos
@st.cache_data
def get_data_context():
    df = load_champions_data("all")
    df = prepare_data(df)
    
    # Crear un resumen estadístico para el contexto
    summary = {
        "total_partidos": len(df),
        "total_goles": df['total_goles'].sum(),
        "promedio_goles": df['total_goles'].mean(),
        "equipos_unicos": len(pd.concat([df['equipo_local'], df['equipo_visitante']]).unique()),
        "temporadas": df['temporada'].unique().tolist(),
        "ejemplo_registros": df.head(5).to_dict(orient='records'),
        "columnas": df.columns.tolist()
    }
    return str(summary)

data_context = get_data_context()

# Interfaz de Chat
st.header("💬 Chat con tus Datos")

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hola! Soy tu asistente de datos de la Champions League. ¿Qué te gustaría saber sobre las temporadas 2013-2016?"}
    ]

# Mostrar mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
if prompt := st.chat_input("Escribe tu pregunta aquí..."):
    # Agregar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar respuesta
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Construir prompt con contexto
            system_prompt = f"""
            Eres un experto analista de datos deportivos especializado en fútbol y la Champions League.
            Tienes acceso al siguiente resumen de datos del proyecto:
            {data_context}
            
            Responde a la pregunta del usuario basándote en estos datos y en tu conocimiento general sobre fútbol.
            Sé conciso, profesional y usa formato Markdown para resaltar puntos clave.
            Si te preguntan algo fuera del contexto de fútbol o datos, indica amablemente que solo puedes hablar del proyecto.
            
            Pregunta del usuario: {prompt}
            """
            
            response = model.generate_content(system_prompt)
            full_response = response.text
            
            message_placeholder.markdown(full_response)
            
            # Guardar respuesta
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Error al generar respuesta: {str(e)}")

# Sugerencias de preguntas
st.markdown("---")
st.subheader("💡 Sugerencias de Preguntas")

col1, col2 = st.columns(2)

with col1:
    if st.button("¿Cuál es el promedio de goles por partido?"):
        # Esto no envía el mensaje automáticamente al chat input, pero el usuario puede copiarlo
        st.info("Copia y pega: ¿Cuál es el promedio de goles por partido?")

with col2:
    if st.button("Explícame la ventaja de jugar de local"):
        st.info("Copia y pega: Explícame la ventaja de jugar de local basándote en los datos.")