import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Champions Analytics - Definición del Problema",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Definición del Problema y Objetivos")
st.markdown("**Business Understanding - UEFA Champions League Analytics**")
st.markdown("---")

# ============================================================================
# SECCIÓN 1: PROBLEMA DE NEGOCIO
# ============================================================================
st.header("1️⃣ Problema de Negocio")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Contexto
    La **UEFA Champions League** es la competición de fútbol más prestigiosa de Europa.
    Históricamente (antes de 2016), ha generado patrones de desempeño predecibles que pueden
    ser analizados para identificar oportunidades de pronóstico.
    
    ### Desafío
    Los apostadores deportivos y analistas enfrentan dificultades para:
    - Identificar equipos con ventaja histórica en contextos específicos
    - Determinar probabilidades reales de Over/Under goles
    - Comparar rendimiento local vs visitante de forma sistemática
    - Identificar equipos en ascenso/declive a través de temporadas
    """)

with col2:
    st.info("""
    **¿Por qué importa?**
    
    - 💰 **Valor económico**: Casas de apuestas mueven millones anualmente
    - 📊 **Acceso a datos**: Bases públicas de partidos históricos disponibles
    - 🎯 **Acción inmediata**: Patrones identificables sin modelos ML complejos
    - ✅ **Alcance limitado**: Análisis descriptivo vs predictivo (más viable)
    """)

st.markdown("""
### Objetivo Principal (1 Frase)
> **"Analizar datos históricos de la UEFA Champions League para identificar patrones 
de éxito que permitan generar pronósticos deportivos orientados a apuestas, 
análisis de rendimiento y comparación evolutiva de equipos."**
""")

st.markdown("---")

# ============================================================================
# SECCIÓN 2: KPIs SMART
# ============================================================================
st.header("2️⃣ Indicadores de Éxito (KPIs SMART)")

kpi_data = {
    "KPI": [
        "Goles Promedio",
        "Win Rate Local",
        "Over 2.5 Goles",
        "Top 10 Equipos",
        "Cobertura Temporal",
        "Calidad de Datos"
    ],
    "Métrica": [
        "Promedio de goles/partido",
        "% victorias equipos locales",
        "% partidos con 3+ goles",
        "Ranking por victorias",
        "Temporadas 2013-2016",
        "Integridad y completitud"
    ],
    "Valor Objetivo": [
        "2.2 - 2.8 goles/partido",
        "50% - 58%",
        "45% - 55%",
        "Identificar 10 élite",
        "3-4 temporadas",
        "> 95% datos válidos"
    ],
    "Relevancia": [
        "Predictor para Over/Under",
        "Ventaja competitiva local",
        "Decisión de apuestas",
        "Equipos a monitorear",
        "Suficiente para patrones",
        "Confiabilidad del análisis"
    ]
}

df_kpis = pd.DataFrame(kpi_data)
st.dataframe(df_kpis, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# SECCIÓN 3: STAKEHOLDERS Y DECISIONES
# ============================================================================
st.header("3️⃣ Stakeholders y Decisiones")

col1, col2 = st.columns(2)

with col1:
    st.subheader("👥 Stakeholders Primarios")
    stakeholders = {
        "Apostadores Deportivos": "Usuarios finales que toman decisiones de apuestas",
        "Analistas de Datos": "Consumen insights para reportes y decisiones",
        "Equipos Técnicos": "Estudian patrones de rivales para preparación",
        "Casas de Apuestas": "Validan probabilidades implícitas en cuotas"
    }
    
    for actor, rol in stakeholders.items():
        st.markdown(f"**{actor}**  \n_{rol}_")

with col2:
    st.subheader("🎯 Decisiones Soportadas")
    decisiones = [
        "✅ ¿Apostar Over o Under en este partido?",
        "✅ ¿Qué equipo tiene más probabilidad de ganar en casa?",
        "✅ ¿Cuál es el nivel de competitividad de la fase?",
        "✅ ¿Qué equipos están en mejor/peor forma?",
        "✅ ¿Cuáles son las tendencias a largo plazo?"
    ]
    
    for decision in decisiones:
        st.write(decision)

st.markdown("---")

# ============================================================================
# SECCIÓN 4: ALCANCE Y SUPUESTOS
# ============================================================================
st.header("4️⃣ Alcance y Supuestos")

col1, col2 = st.columns(2)

with col1:
    st.subheader("✅ IN SCOPE (Sí se hará)")
    in_scope = [
        "📊 Análisis descriptivo e identificación de patrones",
        "📈 Visualización de tendencias temporales",
        "🔍 Comparación local vs visitante por equipo",
        "🏆 Ranking y estadísticas por fase del torneo",
        "💡 Insights exploratorios con IA Generativa",
        "🎯 Dashboard interactivo con filtros"
    ]
    
    for item in in_scope:
        st.markdown(item)

with col2:
    st.subheader("❌ OUT OF SCOPE (No se hará)")
    out_scope = [
        "🤖 Modelo predictivo de Machine Learning",
        "📱 Datos en tiempo real durante temporadas",
        "💳 Integración con casas de apuestas reales",
        "📲 Aplicación móvil nativa",
        "🌍 Predicciones para ligas menores/otras competiciones",
        "🔐 Análisis de arbitraje o control de partidos"
    ]
    
    for item in out_scope:
        st.markdown(item)

st.markdown("---")

# ============================================================================
# SECCIÓN 5: SUPUESTOS Y RESTRICCIONES
# ============================================================================
st.header("5️⃣ Supuestos y Restricciones")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🤔 Supuestos")
    supuestos = """
    - **Datos disponibles**: Existen bases públicas de partidos históricos pre-2016
    - **Patrones estables**: Los factores de éxito se mantienen relativamente estables
    - **Contexto homogéneo**: Reglas del torneo no cambian significativamente
    - **Calidad de datos**: Información de goles, fechas y equipos es confiable
    - **Independencia**: Cada partido es un evento independiente (sin matchfixing)
    """
    st.markdown(supuestos)

with col2:
    st.subheader("⚠️ Restricciones y Riesgos")
    restricciones = """
    - **Temporales**: Proyecto finalizará en plazo fijo de 2 días
    - **Datos históricos**: Solo temporadas 2013-2016 (cambios de formato después)
    - **Presupuesto**: Herramientas de código abierto/gratuitas (Streamlit, Gemini API)
    - **Regulatorios**: Análisis informativo, no recomendación de apuestas legales
    - **Acceso a datos**: Depende de disponibilidad pública en Kaggle/estadísticas
    """
    st.markdown(restricciones)

st.markdown("---")

# ============================================================================
# SECCIÓN 6: CRITERIOS DE ÉXITO
# ============================================================================
st.header("6️⃣ Criterios de Éxito del Proyecto")

success_criteria = {
    "Criterio": [
        "Funcionalidad",
        "Análisis Robusto",
        "Presentación",
        "Documentación"
    ],
    "Descripción": [
        "App Streamlit sin errores, todos los gráficos cargan correctamente",
        "Mínimo 5 gráficos exploratorios, métricas relevantes para apuestas",
        "Interfaz limpia, navegación intuitiva, redacción clara",
        "README completo, código comentado, fuentes citadas"
    ],
    "Ponderación": ["40%", "30%", "20%", "10%"]
}

df_success = pd.DataFrame(success_criteria)
st.dataframe(df_success, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# SECCIÓN 7: DATOS Y FUENTES
# ============================================================================
st.header("7️⃣ Descripción del Dataset")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Características del Dataset")
    st.markdown("""
    - **Período**: 2013-2014, 2014-2015, 2015-2016
    - **Origen**: Kaggle / Fuentes públicas de estadísticas UEFA
    - **Formato**: CSV con columnas estándar
    - **Tamaño Esperado**: < 50MB
    - **Granularidad**: Partido individual (fila = 1 partido)
    """)

with col2:
    st.subheader("📊 Columnas Clave Esperadas")
    columnas = [
        "📅 **fecha**: Fecha del partido (YYYY-MM-DD)",
        "🏟️ **equipo_local**: Nombre del equipo local",
        "✈️ **equipo_visitante**: Nombre del equipo visitante",
        "⚽ **goles_local**: Goles del equipo local",
        "⚽ **goles_visitante**: Goles del equipo visitante",
        "🎭 **fase**: Fase del torneo (Grupos, Octavos, etc)",
        "🏛️ **estadio**: Nombre del estadio (opcional)"
    ]
    for col in columnas:
        st.markdown(col)

st.markdown("---")

# ============================================================================
# SECCIÓN 8: HERRAMIENTAS Y AMBIENTE
# ============================================================================
st.header("8️⃣ Herramientas y Ambiente")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🛠️ Stack Tecnológico")
    tech_stack = [
        "**Python 3.8+**",
        "**Pandas** (manipulación)",
        "**Streamlit** (UI)",
        "**Plotly** (visualización)",
        "**Google Gemini** (IA)"
    ]
    for tech in tech_stack:
        st.write(tech)

with col2:
    st.subheader("📁 Estructura de Proyecto")
    structure = [
        "Inicio.py (portada)",
        "pages/ (secciones)",
        "utils/ (funciones reutilizables)",
        "static/datasets (CSVs)",
        ".streamlit/ (config)"
    ]
    for item in structure:
        st.write(f"• {item}")

with col3:
    st.subheader("📈 Métricas de Calidad")
    metrics = [
        "✅ Cobertura de datos > 95%",
        "✅ Replicabilidad 100%",
        "✅ Documentación completa",
        "✅ Tests manuales pasados",
        "✅ Código limpio (PEP 8)"
    ]
    for metric in metrics:
        st.write(metric)

st.markdown("---")

# ============================================================================
# SECCIÓN 9: CRONOGRAMA
# ============================================================================
st.header("9️⃣ Cronograma de Ejecución")

timeline_data = {
    "Fase": ["Configuración", "Datos", "Análisis", "Visualización", "IA Generativa", "Pulido", "Entrega"],
    "Duración": ["2-3h", "4-6h", "6-8h", "6-8h", "4-6h", "4-6h", "2-3h"],
    "Status": ["✅", "🔄", "⏳", "⏳", "⏳", "⏳", "⏳"]
}

df_timeline = pd.DataFrame(timeline_data)
st.dataframe(df_timeline, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# SECCIÓN 10: CHECKLIST FINAL
# ============================================================================
st.header("🔟 Checklist de Business Understanding")

checklist = [
    ("✅", "Problema escrito en una frase clara y específica"),
    ("✅", "KPIs definidos y cuantificables (SMART)"),
    ("✅", "Stakeholders identificados y alineados"),
    ("✅", "Decisiones que el análisis soportará"),
    ("✅", "Alcance definido: in-scope vs out-of-scope"),
    ("✅", "Supuestos documentados y validados"),
    ("✅", "Restricciones y riesgos identificados"),
    ("✅", "Criterios de éxito establecidos"),
    ("✅", "Datos y fuentes documentadas"),
    ("✅", "Herramientas y cronograma acordados")
]

for status, item in checklist:
    st.write(f"{status} {item}")

st.markdown("---")
st.success("✅ **ETAPA 1 COMPLETADA**: Business Understanding listo para avanzar a Recolección de Datos")
