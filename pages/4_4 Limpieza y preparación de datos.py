import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_champions_data, prepare_data, sidebar_reload_button

st.set_page_config(page_title="Limpieza y Preparación", page_icon="🧹")

st.title("🧹 Limpieza y Preparación de Datos")

st.markdown("""
En esta etapa transformamos los datos crudos en un formato adecuado para el análisis y modelado.
Realizamos limpieza, conversión de tipos y creación de nuevas variables (Feature Engineering).
""")

# Cargar datos crudos
df_raw = load_champions_data("all")

# Botón de recarga en sidebar
sidebar_reload_button()

# 1. Configuración del Pipeline
st.header("1. Configuración del Pipeline de Limpieza")

col_conf1, col_conf2, col_conf3 = st.columns(3)

with col_conf1:
    clean_duplicates = st.checkbox("Eliminar Duplicados", value=True, help="Identifica y elimina filas idénticas")

with col_conf2:
    impute_missing = st.checkbox("Imputar Valores Faltantes", value=True, help="Rellena nulos con Media (numéricos) o Moda (categóricos)")

with col_conf3:
    unify_consistency = st.checkbox("Unificar Consistencia", value=True, help="Limpia espacios y estandariza textos")

# 2. Diagnóstico Inicial
st.header("2. Diagnóstico Inicial (Datos Crudos)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Valores Faltantes")
    null_counts = df_raw.isnull().sum()
    if null_counts.sum() == 0:
        st.success("✅ No se detectaron valores nulos.")
    else:
        st.warning(f"⚠️ Se detectaron {null_counts.sum()} valores nulos.")
        st.dataframe(null_counts[null_counts > 0])

with col2:
    st.subheader("Duplicados")
    duplicates = df_raw.duplicated().sum()
    if duplicates == 0:
        st.success("✅ No hay filas duplicadas.")
    else:
        st.warning(f"⚠️ Se encontraron {duplicates} filas duplicadas.")

# Aplicar transformaciones con opciones seleccionadas
df_processed = prepare_data(
    df_raw, 
    clean_duplicates=clean_duplicates, 
    impute_missing=impute_missing, 
    unify_consistency=unify_consistency
)

# 3. Resultados de la Limpieza
st.header("3. Resultados de la Limpieza")

col_res1, col_res2 = st.columns(2)

with col_res1:
    st.metric("Filas Originales", len(df_raw))
    st.metric("Filas Procesadas", len(df_processed))

with col_res2:
    filas_eliminadas = len(df_raw) - len(df_processed)
    st.metric("Filas Eliminadas", filas_eliminadas, delta_color="inverse")
    
    if clean_duplicates and duplicates > 0:
        st.success(f"✅ Se eliminaron {duplicates} duplicados.")
    
    if impute_missing and null_counts.sum() > 0:
        st.success("✅ Se imputaron los valores faltantes.")

# 4. Pipeline de Transformación
st.header("4. Pipeline de Transformación (Feature Engineering)")

st.info("""
**Pasos realizados:**
1. **Limpieza:** Según configuración (Duplicados, Nulos, Consistencia).
2. **Conversión de Fechas:** 'fecha' a datetime.
3. **Cálculo de Goles:** 'total_goles', 'diferencia_goles'.
4. **Variable Objetivo:** 'resultado' (Victoria Local/Empate/Visita).
5. **Extracción Temporal:** año, mes, día de la semana.
""")

# 5. Preview del Dataset Transformado
st.header("5. Preview del Dataset Transformado")

st.markdown("Muestra de las primeras 10 filas con todas las nuevas variables generadas:")

st.dataframe(df_processed.head(10), use_container_width=True)

# Visualización de la variable objetivo
st.subheader("Distribución de la Variable Objetivo (Resultado)")
fig = px.pie(
    df_processed, 
    names='resultado', 
    title='Proporción de Resultados',
    color='resultado',
    color_discrete_map={
        'Victoria Local': '#2ca02c',
        'Victoria Visitante': '#d62728',
        'Empate': '#ff7f0e'
    }
)
st.plotly_chart(fig, use_container_width=True)

# 6. Exportación y Metadatos
st.header("6. Metadatos Finales")

st.success(f"""
El dataset está listo para el modelado.
* **Dimensiones:** {df_processed.shape[0]} filas x {df_processed.shape[1]} columnas
* **Memoria:** {df_processed.memory_usage(deep=True).sum() / 1024:.2f} KB
""")

if st.checkbox("Ver tipos de datos finales"):
    st.dataframe(df_processed.dtypes.astype(str), use_container_width=True)