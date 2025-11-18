import streamlit as st

st.title("Recolección de datos (Data Collection)")

st.markdown("""
Objetivo:
- Saber de dónde vendrán los datos y cómo accederlos de forma segura y trazable.

Fuentes típicas:
- Bases de datos internas: SQL (tablas), NoSQL (documentos).
- APIs externas: servicios que devuelven datos vía internet (JSON).
- Archivos: CSV, Excel, JSON almacenados en carpetas/Drive.
- Web scraping: extraer datos públicos de sitios web (respetando términos).
- Sensores, logs, encuestas: datos generados por sistemas o personas.

Buenas prácticas:
- Documentar para cada fuente:
  - Origen (sistema/URL), dueño, ruta de acceso.
  - Fecha/hora de extracción y versión.
  - Frecuencia (diaria, semanal) y ventana temporal cubierta.
  - Sensibilidad (personal, confidencial) y permisos requeridos.
  - Calidad esperada (campos clave, tamaños, posible ruido).

Privacidad y cumplimiento:
- Revisa políticas (RGPD/ley local). Evita datos sensibles sin necesidad.
- Minimiza datos personales; anonimiza si es posible.

Consejos prácticos:
- Empieza con una muestra pequeña para explorar.
- Guarda un índice de extracción para reproducir y auditar.
""")

st.info("Cuando avances, reemplaza estas indicaciones por la implementación correspondiente de esta etapa.")