import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.data_loader import load_champions_data, prepare_data, get_team_stats

st.set_page_config(page_title="Comunicación de Resultados", page_icon="📢", layout="wide")

st.title("📢 Comunicación de Resultados (Storytelling)")

st.markdown("""
En esta etapa final, sintetizamos los hallazgos en un dashboard ejecutivo y contamos la historia 
detrás de los datos para facilitar la toma de decisiones.
""")

# Cargar datos
df_raw = load_champions_data("all")
df = prepare_data(df_raw)
stats = get_team_stats(df)

# 1. Dashboard Ejecutivo
st.header("1. Dashboard Ejecutivo")

# KPIs Principales
col1, col2, col3, col4 = st.columns(4)

total_goles = df['total_goles'].sum()
promedio_goles = df['total_goles'].mean()
equipo_mas_goleador = stats['goles_favor'].idxmax()
goles_equipo_top = stats['goles_favor'].max()

col1.metric("Goles Totales (3 Temporadas)", total_goles)
col2.metric("Promedio Goles/Partido", f"{promedio_goles:.2f}")
col3.metric("Equipo Más Ofensivo", equipo_mas_goleador)
col4.metric("Goles del Top 1", goles_equipo_top)

# Gráfico Principal: Evolución de Campeones (Simulado con equipos con más victorias)
st.subheader("Dominio en Europa: Equipos con Más Victorias")

top_victorias = stats.sort_values('victorias', ascending=False).head(5)

fig = px.bar(
    top_victorias,
    x=top_victorias.index,
    y='victorias',
    title='Top 5 Equipos con Más Victorias (2013-2016)',
    color='victorias',
    color_continuous_scale='Blues',
    labels={'index': 'Equipo', 'victorias': 'Total Victorias'}
)
st.plotly_chart(fig, use_container_width=True)

# 2. Storytelling: La Importancia de la Localía
st.header("2. Insight Clave: El Factor Localía")

col_s1, col_s2 = st.columns([1, 2])

with col_s1:
    st.markdown("""
    ### 🏠 ¿Cuánto pesa jugar en casa?
    
    Nuestro análisis revela que jugar de local es una **ventaja significativa** en la Champions League.
    
    * Los equipos locales marcan más goles.
    * Tienen mayor probabilidad de victoria.
    * Esta tendencia se mantiene incluso en fases avanzadas.
    """)

with col_s2:
    # Gráfico comparativo Local vs Visitante
    goles_local = df['goles_local'].sum()
    goles_visitante = df['goles_visitante'].sum()
    
    fig_pie = go.Figure(data=[go.Pie(
        labels=['Goles Local', 'Goles Visitante'],
        values=[goles_local, goles_visitante],
        hole=0.5,
        marker=dict(colors=['#1f77b4', '#ff7f0e'])
    )])
    fig_pie.update_layout(title="Proporción de Goles: Local vs Visitante")
    st.plotly_chart(fig_pie, use_container_width=True)

# 3. Recomendaciones Estratégicas
st.header("3. Recomendaciones y Siguientes Pasos")

col_r1, col_r2, col_r3 = st.columns(3)

with col_r1:
    st.success("""
    **Para Equipos**
    * Maximizar la ofensiva en partidos de local.
    * En fases de eliminación, un empate de visita es un resultado muy valioso estadísticamente.
    """)

with col_r2:
    st.info("""
    **Para Analistas**
    * Incorporar variables de "momento de forma" (racha de últimos 5 partidos).
    * Analizar el impacto de jugadores clave (no disponible en este dataset).
    """)

with col_r3:
    st.warning("""
    **Limitaciones**
    * El análisis no considera lesiones ni sanciones.
    * Se requiere ampliar el dataset a más temporadas para validar tendencias a largo plazo.
    """)

# 4. Conclusión Final
st.markdown("---")
st.markdown("""
### 🎯 Conclusión
El análisis de datos de la Champions League (2013-2016) demuestra que, aunque el fútbol es impredecible, 
existen patrones claros como la **ventaja de localía** y la **jerarquía de ciertos clubes** (Real Madrid, Bayern, Barcelona) 
que dominan consistentemente la competición. Las organizaciones que utilicen estos insights para su planificación 
estratégica tendrán una ventaja competitiva medible.
""")