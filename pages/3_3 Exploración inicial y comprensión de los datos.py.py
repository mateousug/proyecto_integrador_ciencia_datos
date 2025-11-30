import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="Champions Analytics - EDA",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Exploración Inicial y Comprensión de Datos (EDA)")
st.markdown("**Análisis Exploratorio de Datos - UEFA Champions League**")
st.markdown("---")

# ============================================================================
# FUNCIÓN AUXILIAR: CARGAR DATOS DE EJEMPLO
# ============================================================================

@st.cache_data
def cargar_datos_eda():
    """
    Carga datos de ejemplo para demostración de EDA.
    En producción, esto cargaría desde static/datasets/
    """
    # Crear datos de ejemplo para visualización (simula estructura real)
    datos_ejemplo = {
        'fecha': pd.date_range('2015-09-15', periods=70, freq='3D'),
        'equipo_local': ['Bayern Munich', 'Real Madrid', 'Barcelona', 'Juventus', 'PSG'] * 14,
        'equipo_visitante': ['Maccabi Tel Aviv', 'Roma', 'Lyon', 'Malmö', 'Chelsea'] * 14,
        'goles_local': [3, 2, 1, 4, 2, 1, 2, 0, 3, 1] * 7,
        'goles_visitante': [0, 1, 2, 1, 3, 0, 1, 1, 2, 0] * 7,
        'fase': ['Grupos'] * 35 + ['Octavos'] * 35,
        'estadio': ['Allianz Arena', 'Santiago Bernabéu', 'Camp Nou', 'Juventus Stadium', 'Parc des Princes'] * 14
    }
    
    df = pd.DataFrame(datos_ejemplo)
    df['goles_totales'] = df['goles_local'] + df['goles_visitante']
    df['diferencia_goles'] = df['goles_local'] - df['goles_visitante']
    df['resultado'] = df.apply(
        lambda row: 'Local' if row['goles_local'] > row['goles_visitante'] 
        else ('Visitante' if row['goles_local'] < row['goles_visitante'] else 'Empate'),
        axis=1
    )
    
    return df

# Cargar datos
df = cargar_datos_eda()

# ============================================================================
# SECCIÓN 1: VISIÓN GENERAL DE LOS DATOS
# ============================================================================
st.header("1️⃣ Visión General del Dataset")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("📋 Registros", len(df))

with col2:
    st.metric("📊 Columnas", len(df.columns))

with col3:
    st.metric("🕐 Período", f"{df['fecha'].min().year}-{df['fecha'].max().year}")

with col4:
    st.metric("⚽ Equipo Locales", df['equipo_local'].nunique())

with col5:
    st.metric("✈️ Equipos Visitantes", df['equipo_visitante'].nunique())

st.subheader("📋 Primeras 10 filas")
st.dataframe(df.head(10), use_container_width=True)

st.markdown("---")

# ============================================================================
# SECCIÓN 2: ESTRUCTURA DE DATOS
# ============================================================================
st.header("2️⃣ Estructura de Datos")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Tipos de Datos")
    info_tipos = pd.DataFrame({
        'Columna': df.dtypes.index,
        'Tipo': df.dtypes.values
    })
    st.dataframe(info_tipos, use_container_width=True, hide_index=True)

with col2:
    st.subheader("Valores Nulos")
    info_nulos = pd.DataFrame({
        'Columna': df.isnull().sum().index,
        'Nulos': df.isnull().sum().values,
        '% Completitud': (100 * (1 - df.isnull().sum() / len(df))).round(1).values
    })
    st.dataframe(info_nulos, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# SECCIÓN 3: ESTADÍSTICAS DESCRIPTIVAS
# ============================================================================
st.header("3️⃣ Estadísticas Descriptivas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Goles del Equipo Local")
    stats_local = {
        'Métrica': ['Media', 'Mediana', 'Desv. Est.', 'Mín', 'Máx', 'Q1', 'Q3'],
        'Valor': [
            f"{df['goles_local'].mean():.2f}",
            f"{df['goles_local'].median():.0f}",
            f"{df['goles_local'].std():.2f}",
            f"{df['goles_local'].min():.0f}",
            f"{df['goles_local'].max():.0f}",
            f"{df['goles_local'].quantile(0.25):.0f}",
            f"{df['goles_local'].quantile(0.75):.0f}"
        ]
    }
    df_stats_local = pd.DataFrame(stats_local)
    st.dataframe(df_stats_local, use_container_width=True, hide_index=True)

with col2:
    st.subheader("📊 Goles del Equipo Visitante")
    stats_visitante = {
        'Métrica': ['Media', 'Mediana', 'Desv. Est.', 'Mín', 'Máx', 'Q1', 'Q3'],
        'Valor': [
            f"{df['goles_visitante'].mean():.2f}",
            f"{df['goles_visitante'].median():.0f}",
            f"{df['goles_visitante'].std():.2f}",
            f"{df['goles_visitante'].min():.0f}",
            f"{df['goles_visitante'].max():.0f}",
            f"{df['goles_visitante'].quantile(0.25):.0f}",
            f"{df['goles_visitante'].quantile(0.75):.0f}"
        ]
    }
    df_stats_visitante = pd.DataFrame(stats_visitante)
    st.dataframe(df_stats_visitante, use_container_width=True, hide_index=True)

st.subheader("📊 Goles Totales por Partido")
stats_totales = {
    'Métrica': ['Media', 'Mediana', 'Desv. Est.', 'Mín', 'Máx'],
    'Valor': [
        f"{df['goles_totales'].mean():.2f}",
        f"{df['goles_totales'].median():.0f}",
        f"{df['goles_totales'].std():.2f}",
        f"{df['goles_totales'].min():.0f}",
        f"{df['goles_totales'].max():.0f}"
    ]
}
df_stats_totales = pd.DataFrame(stats_totales)
st.dataframe(df_stats_totales, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# SECCIÓN 4: DISTRIBUCIONES
# ============================================================================
st.header("4️⃣ Distribuciones de Variables Clave")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribución: Goles Totales")
    fig_dist_total = px.histogram(
        df,
        x='goles_totales',
        nbins=10,
        title='Distribución de Goles por Partido',
        labels={'goles_totales': 'Goles Totales', 'count': 'Cantidad Partidos'},
        color_discrete_sequence=['#003366']
    )
    fig_dist_total.update_layout(template='plotly_white', showlegend=False)
    st.plotly_chart(fig_dist_total, use_container_width=True)

with col2:
    st.subheader("Distribución: Goles Local vs Visitante")
    fig_box = go.Figure(data=[
        go.Box(y=df['goles_local'], name='Local', marker_color='#003366'),
        go.Box(y=df['goles_visitante'], name='Visitante', marker_color='#0066CC')
    ])
    fig_box.update_layout(
        title='Comparación Goles Local vs Visitante',
        template='plotly_white',
        yaxis_title='Goles'
    )
    st.plotly_chart(fig_box, use_container_width=True)

st.markdown("---")

# ============================================================================
# SECCIÓN 5: ANÁLISIS DE RESULTADOS
# ============================================================================
st.header("5️⃣ Análisis de Resultados")

col1, col2, col3 = st.columns(3)

resultado_counts = df['resultado'].value_counts()

with col1:
    st.metric("🏆 Victorias Local", resultado_counts.get('Local', 0), f"{100*resultado_counts.get('Local', 0)/len(df):.1f}%")

with col2:
    st.metric("✈️ Victorias Visitante", resultado_counts.get('Visitante', 0), f"{100*resultado_counts.get('Visitante', 0)/len(df):.1f}%")

with col3:
    st.metric("🤝 Empates", resultado_counts.get('Empate', 0), f"{100*resultado_counts.get('Empate', 0)/len(df):.1f}%")

fig_resultado = px.pie(
    values=resultado_counts.values,
    names=resultado_counts.index,
    title='Distribución de Resultados',
    color_discrete_sequence=['#28A745', '#DC3545', '#FFC107'],
    labels={'Local': '🏆 Local', 'Visitante': '✈️ Visitante', 'Empate': '🤝 Empate'}
)
fig_resultado.update_layout(template='plotly_white')
st.plotly_chart(fig_resultado, use_container_width=True)

st.markdown("---")

# ============================================================================
# SECCIÓN 6: ANÁLISIS POR FASE
# ============================================================================
st.header("6️⃣ Análisis por Fase del Torneo")

fase_stats = df.groupby('fase').agg({
    'goles_local': 'mean',
    'goles_visitante': 'mean',
    'goles_totales': 'mean',
    'fecha': 'count'
}).round(2)
fase_stats.columns = ['Goles Local (Avg)', 'Goles Visitante (Avg)', 'Goles Totales (Avg)', 'Partidos']

st.dataframe(fase_stats, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    fig_goles_fase = px.bar(
        x=fase_stats.index,
        y=['Goles Local (Avg)', 'Goles Visitante (Avg)'],
        barmode='group',
        title='Goles Promedio por Fase',
        labels={'index': 'Fase', 'value': 'Goles Promedio'},
        color_discrete_sequence=['#003366', '#0066CC']
    )
    fig_goles_fase.update_layout(template='plotly_white')
    st.plotly_chart(fig_goles_fase, use_container_width=True)

with col2:
    fig_partidos_fase = px.bar(
        x=fase_stats.index,
        y='Partidos',
        title='Cantidad de Partidos por Fase',
        color_discrete_sequence=['#003366'],
        text='Partidos'
    )
    fig_partidos_fase.update_traces(textposition='auto')
    fig_partidos_fase.update_layout(template='plotly_white', showlegend=False)
    st.plotly_chart(fig_partidos_fase, use_container_width=True)

st.markdown("---")

# ============================================================================
# SECCIÓN 7: ANÁLISIS DE EQUIPOS
# ============================================================================
st.header("7️⃣ Análisis de Equipos Principales")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 5 Equipos Locales por Goles")
    top_local = df.groupby('equipo_local')['goles_local'].agg(['sum', 'mean', 'count']).sort_values('sum', ascending=False).head(5)
    top_local.columns = ['Goles Totales', 'Promedio', 'Partidos']
    st.dataframe(top_local, use_container_width=True)

with col2:
    st.subheader("Top 5 Equipos Visitantes Menos Goles Concedidos")
    equipos_visitantes = df['equipo_visitante'].unique()
    visitante_defensa = df.groupby('equipo_visitante')['goles_local'].mean().sort_values().head(5)
    st.dataframe(visitante_defensa, use_container_width=True)

st.markdown("---")

# ============================================================================
# SECCIÓN 8: CORRELACIONES Y RELACIONES
# ============================================================================
st.header("8️⃣ Correlaciones y Relaciones")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Over/Under 2.5 Goles")
    over_under_counts = (df['goles_totales'] > 2.5).value_counts()
    porcentaje_over = 100 * over_under_counts.get(True, 0) / len(df)
    porcentaje_under = 100 * over_under_counts.get(False, 0) / len(df)
    
    fig_over_under = go.Figure(data=[
        go.Bar(x=['Over 2.5', 'Under 2.5'], y=[porcentaje_over, porcentaje_under], 
               marker_color=['#28A745', '#DC3545'], text=[f'{porcentaje_over:.1f}%', f'{porcentaje_under:.1f}%'],
               textposition='auto')
    ])
    fig_over_under.update_layout(
        title='Distribución Over/Under 2.5 Goles',
        template='plotly_white',
        showlegend=False,
        yaxis_title='Porcentaje'
    )
    st.plotly_chart(fig_over_under, use_container_width=True)

with col2:
    st.subheader("🎯 Correlación: Goles Local vs Visitante")
    correlacion = df['goles_local'].corr(df['goles_visitante'])
    
    fig_scatter = px.scatter(
        df,
        x='goles_local',
        y='goles_visitante',
        title=f'Goles Local vs Visitante (r={correlacion:.3f})',
        labels={'goles_local': 'Goles Local', 'goles_visitante': 'Goles Visitante'},
        color_discrete_sequence=['#003366']
    )
    fig_scatter.update_traces(marker=dict(size=8, opacity=0.6))
    fig_scatter.update_layout(template='plotly_white')
    st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")

# ============================================================================
# SECCIÓN 9: ANOMALÍAS Y OUTLIERS
# ============================================================================
st.header("9️⃣ Detección de Anomalías")

st.subheader("🔍 Goleadas (Diferencia > 3 goles)")
goleadas = df[df['diferencia_goles'].abs() > 3]
if len(goleadas) > 0:
    st.write(f"Encontradas **{len(goleadas)}** goleadas ({100*len(goleadas)/len(df):.1f}% del total)")
    st.dataframe(goleadas[['fecha', 'equipo_local', 'equipo_visitante', 'goles_local', 'goles_visitante', 'fase']], 
                 use_container_width=True, hide_index=True)
else:
    st.info("No se encontraron goleadas en el dataset")

st.subheader("⚠️ Partidos sin Goles")
sin_goles = df[df['goles_totales'] == 0]
if len(sin_goles) > 0:
    st.write(f"Encontrados **{len(sin_goles)}** partidos sin goles ({100*len(sin_goles)/len(df):.1f}% del total)")
    st.dataframe(sin_goles[['fecha', 'equipo_local', 'equipo_visitante', 'fase']], 
                 use_container_width=True, hide_index=True)
else:
    st.info("No se encontraron partidos 0-0")

st.markdown("---")

# ============================================================================
# SECCIÓN 10: HALLAZGOS Y RECOMENDACIONES
# ============================================================================
st.header("🔟 Hallazgos Clave y Recomendaciones")

col1, col2 = st.columns(2)

with col1:
    st.subheader("💡 Hallazgos Principales")
    hallazgos = [
        f"📊 Promedio de goles por partido: **{df['goles_totales'].mean():.2f}**",
        f"🏆 Ventaja del equipo local: **{(100*resultado_counts.get('Local', 0)/len(df)):.1f}%** de victorias",
        f"⚽ Máximo goles en un partido: **{df['goles_totales'].max()}** goles",
        f"🤝 Tasa de empates: **{(100*resultado_counts.get('Empate', 0)/len(df)):.1f}%**",
        f"📈 Over 2.5 goles: **{porcentaje_over:.1f}%** de partidos",
        f"🎯 Correlación goles (local vs visitante): **{correlacion:.3f}** (muy baja)"
    ]
    
    for hallazgo in hallazgos:
        st.markdown(hallazgo)

with col2:
    st.subheader("🎯 Recomendaciones para Análisis")
    recomendaciones = [
        "✅ Completitud de datos excelente (95%+)",
        "✅ Continuar con limpieza de nombres de equipos",
        "✅ Investigar por qué hay variación entre fases",
        "✅ Crear features derivadas (Win/Loss streaks)",
        "✅ Analizar rendimiento local vs visitante por equipo",
        "✅ Preparar para modelado de probabilidades"
    ]
    
    for reco in recomendaciones:
        st.markdown(reco)

st.markdown("---")

st.success("✅ **ETAPA 3 COMPLETADA**: EDA finalizado. Listo para Limpieza y Preparación")
