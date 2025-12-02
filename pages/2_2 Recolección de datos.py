import streamlit as st
import pandas as pd
from utils.data_loader import load_champions_data, get_data_info
import io
from pathlib import Path
import glob

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
    
    # Estadísticas generales
    col_stat1, col_stat2, col_stat3 = st.columns(3)
    with col_stat1:
        st.metric("📊 Temporadas Disponibles", len(info_df))
    with col_stat2:
        st.metric("📈 Total de Partidos", info_df["Filas"].sum())
    with col_stat3:
        st.metric("💾 Tamaño Total (KB)", round(info_df["Tamaño (KB)"].sum(), 2))
        
except Exception as e:
    st.error(f"Error al leer metadatos: {str(e)}")

# 2. Exploración de Archivos Raw
st.header("2. Exploración de Datos Crudos (Raw Data)")

# Detectar dinámicamente todas las temporadas disponibles
base_path = Path("static/datasets")
csv_files = sorted(glob.glob(str(base_path / "champions_*.csv")))
temporadas = [Path(f).stem.replace("champions_", "") for f in csv_files]

# Crear tabs dinámicamente
tab_names = [t.replace("_", "-") for t in temporadas] + ["Consolidado"]
tabs = st.tabs(tab_names)

# Mostrar cada temporada en su tab
for idx, (tab, temporada) in enumerate(zip(tabs[:-1], temporadas)):
    with tab:
        try:
            df_season = load_champions_data(temporada)
            st.subheader(f"Temporada {temporada.replace('_', '-')}")
            st.dataframe(df_season.head(10), use_container_width=True)
            st.caption(f"Total de registros: {len(df_season)}")
        except Exception as e:
            st.error(f"Error cargando temporada {temporada}: {str(e)}")

# Tab consolidado
with tabs[-1]:
    st.subheader("Dataset Consolidado (Todas las Temporadas)")
    try:
        df_all = load_champions_data("all")
        st.dataframe(df_all.head(10), use_container_width=True)
        st.caption(f"Total de registros consolidados: {len(df_all)}")
        
        # Descarga del dataset consolidado
        csv = df_all.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Descargar Dataset Consolidado (CSV)",
            data=csv,
            file_name="champions_league_consolidated.csv",
            mime="text/csv",
        )
        
        # Información del consolidado
        col_info1, col_info2, col_info3 = st.columns(3)
        with col_info1:
            st.metric("Años Cubiertos", f"{df_all['temporada'].min()} a {df_all['temporada'].max()}")
        with col_info2:
            st.metric("Equipos Únicos", len(pd.concat([df_all['equipo_local'], df_all['equipo_visitante']]).unique()))
        with col_info3:
            st.metric("Total de Goles", int(df_all['goles_local'].sum() + df_all['goles_visitante'].sum()))
    except Exception as e:
        st.error(f"Error cargando datos consolidados: {str(e)}")

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
