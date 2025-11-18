import streamlit as st

st.title("Limpieza y preparación de datos (Data Cleaning & Wrangling)")

st.markdown("""
Objetivo:
- Dejar los datos consistentes y listos para análisis/modelado.

Limpieza:
- Valores faltantes: imputar (media/mediana/moda) o eliminar según impacto.
- Duplicados: identificar y quitar si no aportan.
- Consistencia: unificar categorías (ej. "México"/"Mexico"/"MEX").
- Tipos: convertir a fecha, numérico o texto según corresponda.

Feature engineering:
- Fechas: día de la semana, mes, trimestre, estacionalidad.
- Ratios y banderas (flags) para reglas simples.
- Variables dummy para categorías.

Preparación para modelado:
- Escalado/normalización para algoritmos que lo requieren.
- Codificación de texto/categorías (one-hot, ordinal) según el caso.

Split de datos:
- Separar entrenamiento/validación/prueba para evaluar correctamente.
- Evitar fuga de información: aplicar transformaciones usando solo entrenamiento.

Checklist:
- Datos sin nulos críticos ni duplicados.
- Categorías consistentes y tipos correctos.
- Conjunto dividido con reproducibilidad (semillas).
""")

st.info("Cuando avances, reemplaza estas indicaciones por la implementación correspondiente de esta etapa.")