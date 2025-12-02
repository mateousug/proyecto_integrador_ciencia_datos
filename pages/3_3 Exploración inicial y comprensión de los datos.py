import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_champions_data, prepare_data, get_team_stats
from utils.visualizations import (
    create_goals_distribution,
    create_goals_by_phase,
    create_top_teams_chart,
    create_temporal_evolution,
    create_correlation_heatmap,
    create_result_distribution,
    create_goals_by_season,
    create_stadium_analysis
)

st.set_page_config(page_title="EDA - Exploración de Datos", page_icon="🔍", layout="wide")

st.title("🔍 Exploración Inicial y Comprensión de Datos (EDA)")

st.markdown("""
En esta fase utilizamos visualizaciones interactivas para entender la estructura, 
patrones y relaciones en los datos antes de proceder al modelado.
""")

# Cargar y preparar datos
try:
    df_raw = load_champions_data("all")
    df = prepare_data(df_raw)
    stats_df = get_team_stats(df)
except Exception as e:
    st.error(f"Error al cargar datos: {str(e)}")
    st.stop()

# Sidebar para filtros globales
st.sidebar.header("Filtros de Análisis")
selected_season = st.sidebar.multiselect(
    "Seleccionar Temporadas",
    options=df['temporada'].unique(),
    default=df['temporada'].unique()
)

if selected_season:
    df_filtered = df[df['temporada'].isin(selected_season)]
else:
    df_filtered = df

# 1. Estadísticas Descriptivas
st.header("1. Resumen Estadístico")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Partidos", len(df_filtered))
col2.metric("Total Goles", df_filtered['total_goles'].sum())
col3.metric("Promedio Goles/Partido", round(df_filtered['total_goles'].mean(), 2))
col4.metric("Equipos Únicos", len(pd.concat([df_filtered['equipo_local'], df_filtered['equipo_visitante']]).unique()))

with st.expander("Ver Estadísticas Detalladas"):
    st.dataframe(df_filtered.describe(), use_container_width=True)

# 2. Análisis de Goles
st.header("2. Análisis de Goles")

col_g1, col_g2 = st.columns(2)

with col_g1:
    st.plotly_chart(create_goals_distribution(df_filtered), use_container_width=True)

with col_g2:
    st.plotly_chart(create_goals_by_phase(df_filtered), use_container_width=True)

st.plotly_chart(create_temporal_evolution(df_filtered), use_container_width=True)

# 3. Análisis de Equipos
st.header("3. Rendimiento de Equipos")

st.plotly_chart(create_top_teams_chart(stats_df), use_container_width=True)

# 4. Análisis de Resultados y Correlaciones
st.header("4. Factores de Influencia")

col_f1, col_f2 = st.columns(2)

with col_f1:
    st.plotly_chart(create_result_distribution(df_filtered), use_container_width=True)
    st.caption("Distribución de resultados (Local vs Visitante)")

with col_f2:
    st.plotly_chart(create_correlation_heatmap(df_filtered), use_container_width=True)
    st.caption("Correlación entre variables numéricas")

# 5. Análisis de Estadios
st.header("5. Análisis de Estadios")
st.plotly_chart(create_stadium_analysis(df_filtered), use_container_width=True)

# 6. Comparativa por Temporada
st.header("6. Comparativa por Temporada")
st.plotly_chart(create_goals_by_season(df), use_container_width=True)
