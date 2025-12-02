import streamlit as st

st.set_page_config(page_title="Definición del Problema", page_icon="🎯")

st.title("🎯 Definición del Problema y Objetivos")

# Introducción al Business Understanding
st.markdown("""
En esta etapa inicial de la metodología CRISP-DM, establecemos las bases del proyecto,
definiendo claramente qué queremos resolver y cómo mediremos el éxito.
""")

# 1. Definición del Problema
st.header("1. Planteamiento del Problema")

st.info("""
**Problema de Negocio:**
Los clubes de fútbol y analistas deportivos necesitan identificar **qué factores estadísticos y tácticos** 
tienen mayor correlación con el éxito en la UEFA Champions League para optimizar estrategias y toma de decisiones.

Actualmente, el análisis se basa mucho en la intuición o estadísticas aisladas, sin una visión integral 
que combine datos históricos, tendencias y modelos predictivos.
""")

# 2. Objetivos y KPIs
st.header("2. Objetivos y KPIs (Métricas de Éxito)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Objetivos de Negocio")
    st.markdown("""
    * **Identificar patrones de éxito:** Determinar si jugar de local o la fase del torneo influye significativamente.
    * **Predecir resultados:** Crear un modelo base para estimar la probabilidad de victoria.
    * **Optimizar estrategias:** Proveer insights sobre cuándo se marcan más goles.
    """)

with col2:
    st.subheader("KPIs SMART")
    st.markdown("""
    * **Precisión del Modelo:** Alcanzar un Accuracy > 60% en la predicción de resultados (Local/Empate/Visita).
    * **Identificación de Factores:** Determinar al menos 3 variables con alta correlación (>0.5) con la victoria.
    * **Insights de Localía:** Cuantificar la "ventaja de campo" con un intervalo de confianza del 95%.
    """)

# 3. Stakeholders
st.header("3. Stakeholders y Usuarios Finales")

st.markdown("""
| Stakeholder | Interés Principal | Uso de los Resultados |
|-------------|-------------------|-----------------------|
| **Cuerpo Técnico** | Rendimiento deportivo | Ajuste de tácticas según rival y condición (L/V) |
| **Analistas de Datos** | Patrones ocultos | Generación de reportes pre-partido |
| **Directiva** | Fichajes y premios | Evaluación objetiva del rendimiento del equipo |
| **Aficionados** | Entretenimiento | Consumo de estadísticas avanzadas y predicciones |
""")

# 4. Alcance y Limitaciones
st.header("4. Alcance y Supuestos")

with st.expander("Ver Alcance del Proyecto", expanded=True):
    st.markdown("""
    **✅ INCLUYE:**
    * Análisis de temporadas 2013-2014, 2014-2015, 2015-2016.
    * Datos de goles, fases, estadios y equipos.
    * Modelos de clasificación para resultado del partido.
    * Asistente de IA para consultas sobre estos datos.

    **❌ NO INCLUYE:**
    * Datos de posesión, tiros a puerta o tarjetas (no disponibles en el dataset actual).
    * Análisis de jugadores individuales (solo nivel equipo).
    * Predicciones de apuestas financieras.

    **⚠️ SUPUESTOS:**
    * Los datos de los CSV son íntegros y correctos.
    * El formato de competición se mantiene estable en estas temporadas.
    """)
