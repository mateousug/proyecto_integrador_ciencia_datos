import streamlit as st

st.title("Exploración inicial y comprensión de los datos (Data Understanding / EDA)")

st.markdown("""
Objetivo:
- Entender la forma de los datos antes de cualquier modelo.

Pasos básicos:
- Cargar datos (pandas, Excel) y ver primeras filas.
- Revisar estructura: número de filas/columnas, tipos (numérico, texto, fecha).
- Detectar valores faltantes y duplicados.

Estadísticas descriptivas:
- Medidas como media, mediana, desviación ayudan a entender tendencias y variabilidad.
- Revisa mínimos, máximos y valores raros.

Visualizaciones útiles:
- Histogramas: distribución de una variable.
- Boxplots: rangos y outliers.
- Dispersión: relación entre dos variables.
- Matriz de correlación: qué variables se mueven juntas (correlación ≠ causalidad).

Qué buscar:
- Anomalías (edades negativas, fechas imposibles).
- Desbalance de clases (muy pocos positivos).
- Posible leakage (variables que revelan la respuesta de forma indirecta).

Resultados esperados:
- Lista de problemas detectados y preguntas para negocio.
- Hipótesis iniciales sobre relaciones y factores importantes.
""")

st.info("Cuando avances, reemplaza estas indicaciones por la implementación correspondiente de esta etapa.")