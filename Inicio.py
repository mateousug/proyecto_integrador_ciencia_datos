import streamlit as st
from PIL import Image
import pandas as pd
from utils.data_loader import get_data_info, sidebar_reload_button

# Configuración de la página
st.set_page_config(
    page_title="Champions League Analytics",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Botón de recarga
sidebar_reload_button()

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    .card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f8f9fa;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        color: #2c3e50; /* Force dark text for visibility on light background */
    }
    .card h3, .card h4 {
        color: #1f77b4;
        margin-top: 0;
    }
    .card p {
        color: #2c3e50;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)

# Título Principal
st.markdown('<h1 class="main-header">⚽ UEFA Champions League Analytics</h1>', unsafe_allow_html=True)

# Introducción
st.markdown("""
<div class="card">
    <h3>Bienvenido al Proyecto Integrador de Ciencia de Datos</h3>
    <p>
        Este proyecto analiza datos históricos de la UEFA Champions League (temporadas 2013-2016) 
        para descubrir patrones de rendimiento, factores de éxito y tendencias evolutivas en el fútbol europeo de élite.
        Utilizamos metodología CRISP-DM y técnicas avanzadas de visualización e Inteligencia Artificial.
    </p>
</div>
""", unsafe_allow_html=True)

# Columnas para Equipo y Datos
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 👥 Equipo de Trabajo")
    with st.container():
        st.info("""
        **Roles y Responsabilidades:**
        
        * **Project Manager & Data Analyst:** Liderazgo, definición de KPIs y análisis de negocio.
        * **Data Engineer:** Limpieza, transformación y preparación de datasets.
        * **Data Scientist:** Modelado predictivo y análisis estadístico avanzado.
        * **AI Engineer:** Integración de Gemini y generación de insights automatizados.
        """)

with col2:
    st.markdown("### 📊 Resumen del Dataset")
    try:
        info_df = get_data_info()
        st.dataframe(
            info_df,
            column_config={
                "Temporada": st.column_config.TextColumn("Temporada", help="Año de la competición"),
                "Filas": st.column_config.NumberColumn("Partidos", format="%d"),
                "Tamaño (KB)": st.column_config.NumberColumn("Tamaño", format="%.2f KB"),
            },
            hide_index=True,
            use_container_width=True
        )
    except Exception as e:
        st.error(f"Error al cargar información de datos: {str(e)}")

# Sección de Objetivos
st.markdown("### 🎯 Objetivos del Proyecto")
col_obj1, col_obj2, col_obj3 = st.columns(3)

with col_obj1:
    st.markdown("""
    <div class="card">
        <h4>🔍 Análisis Exploratorio</h4>
        <p>Entender distribuciones de goles, ventaja de localía y rendimiento por fases.</p>
    </div>
    """, unsafe_allow_html=True)

with col_obj2:
    st.markdown("""
    <div class="card">
        <h4>📈 Modelado Predictivo</h4>
        <p>Identificar factores clave que determinan la victoria en partidos de alta competencia.</p>
    </div>
    """, unsafe_allow_html=True)

with col_obj3:
    st.markdown("""
    <div class="card">
        <h4>🤖 IA Generativa</h4>
        <p>Asistente inteligente para profundizar en los hallazgos y generar reportes automáticos.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("*Proyecto desarrollado con Streamlit, Plotly y Google Gemini*")