import streamlit as st
import pandas as pd
from utils.data_loader import load_champions_data, get_data_info
import io

st.set_page_config(page_title="Recolección de Datos", page_icon="💾")

st.title("💾 Recolección de Datos (Data Collection)")

st.markdown("""
En esta etapa documentamos el origen de los datos, asegurando su trazabilidad y calidad inicial.
Utilizamos datasets históricos de la UEFA Champions League.
""")

# 1. Fuentes de Datos
st.header("1. Inventario de Fuentes de Datos")

st.info("""
**Origen de los Datos:**
Los datos provienen de registros históricos de partidos oficiales de la UEFA Champions League.
Se encuentran almacenados en formato CSV en el directorio `static/datasets/`.
""")

# Mostrar información de los archivos
try:
    info_df = get_data_info()
    st.dataframe(
        info_df,
        use_container_width=True,
        hide_index=True
    )
except Exception as e:
    st.error(f"Error al leer metadatos: {str(e)}")

# 2. Exploración de Archivos Raw
st.header("2. Exploración de Datos Crudos (Raw Data)")

tabs = st.tabs(["2013-2014", "2014-2015", "2015-2016", "Consolidado"])

with tabs[0]:
    st.subheader("Temporada 2013-2014")
    df_13_14 = load_champions_data("2013_2014")
    st.dataframe(df_13_14.head(10), use_container_width=True)
    st.caption(f"Total de registros: {len(df_13_14)}")

with tabs[1]:
    st.subheader("Temporada 2014-2015")
    df_14_15 = load_champions_data("2014_2015")
    st.dataframe(df_14_15.head(10), use_container_width=True)
    st.caption(f"Total de registros: {len(df_14_15)}")

with tabs[2]:
    st.subheader("Temporada 2015-2016")
    df_15_16 = load_champions_data("2015_2016")
    st.dataframe(df_15_16.head(10), use_container_width=True)
    st.caption(f"Total de registros: {len(df_15_16)}")

with tabs[3]:
    st.subheader("Dataset Consolidado")
    df_all = load_champions_data("all")
    st.dataframe(df_all.head(10), use_container_width=True)
    st.caption(f"Total de registros consolidados: {len(df_all)}")
    
    # Descarga del dataset consolidado
    csv = df_all.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar Dataset Consolidado (CSV)",
        data=csv,
        file_name="champions_league_2013_2016.csv",
        mime="text/csv",
    )

# 3. Reporte de Calidad Inicial
st.header("3. Reporte de Calidad Inicial")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ✅ Puntos Fuertes")
    st.success("""
    * **Estructura Consistente:** Todos los archivos comparten las mismas columnas.
    * **Sin Datos Críticos Faltantes:** Fechas, equipos y goles están completos.
    * **Formato Estándar:** CSV separado por comas, codificación UTF-8.
    """)

with col2:
    st.markdown("### ⚠️ Puntos de Atención")
    st.warning("""
    * **Nombres de Equipos:** Posibles inconsistencias (ej. "Bayern Munich" vs "Bayern München").
    * **Fechas:** Necesitan conversión a formato datetime para análisis temporal.
    * **Fases:** Requieren ordenamiento lógico (Grupos -> Final) y no alfabético.
    """)

# 4. Diccionario de Datos
st.header("4. Diccionario de Datos")

diccionario = {
    "Campo": ["fecha", "equipo_local", "equipo_visitante", "goles_local", "goles_visitante", "fase", "estadio"],
    "Descripción": [
        "Fecha del partido (YYYY-MM-DD)",
        "Nombre del equipo que juega en casa",
        "Nombre del equipo visitante",
        "Goles marcados por el equipo local",
        "Goles marcados por el equipo visitante",
        "Etapa de la competición (Grupos, Octavos, etc.)",
        "Nombre del estadio donde se jugó"
    ],
    "Tipo de Dato": ["Fecha", "Texto (Categórico)", "Texto (Categórico)", "Entero", "Entero", "Texto (Categórico)", "Texto"]
}

st.table(pd.DataFrame(diccionario))
