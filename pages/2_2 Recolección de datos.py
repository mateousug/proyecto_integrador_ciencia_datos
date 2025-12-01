import streamlit as st
import pandas as pd
import json
from datetime import datetime

st.set_page_config(
    page_title="Champions Analytics - Recolección de Datos",
    page_icon="📥",
    layout="wide"
)

st.title("📥 Recolección de Datos (Data Collection)")
st.markdown("**Documentación de fuentes, extracción y trazabilidad**")
st.markdown("---")

# ============================================================================
# SECCIÓN 1: DESCRIPCIÓN DE FUENTES
# ============================================================================
st.header("1️⃣ Fuentes de Datos")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔗 Fuentes Primarias")
    st.markdown("""
    ### Kaggle UEFA Champions League
    - **Descripción**: Dataset consolidado de partidos de UCL 
    - **URL**: https://www.kaggle.com/datasets/
    - **Temporadas**: 2013-14, 2014-15, 2015-16
    - **Formato**: CSV
    - **Actualización**: Estática (antes de 2016)
    - **Licencia**: CC0 / Público
    - **Acceso**: Requiere cuenta Kaggle (gratuita)
    
    ### StatsBomb Open Data
    - **Descripción**: Eventos detallados de partidos
    - **URL**: https://github.com/statsbomb/open-data
    - **Granularidad**: Evento por evento
    - **Formato**: JSON
    - **Ventaja**: Muy detallado, actualizado
    """)

with col2:
    st.subheader("📊 Estructura de Datos")
    st.markdown("""
    ### Archivo Principal: `champions_YYYY_YYYY.csv`
    
    **Columnas mínimas requeridas:**
    - `fecha` (DATE): Día del partido
    - `equipo_local` (TEXT): Nombre equipo local
    - `equipo_visitante` (TEXT): Nombre equipo visitante
    - `goles_local` (INT): Goles del equipo local
    - `goles_visitante` (INT): Goles del equipo visitante
    - `fase` (TEXT): Grupos, Octavos, Cuartos, Semifinal, Final
    - `estadio` (TEXT): Nombre del estadio (opcional)
    - `asistencia` (INT): Espectadores (opcional)
    """)

st.markdown("---")

# ============================================================================
# SECCIÓN 2: METADATOS DE EXTRACCIÓN
# ============================================================================
st.header("2️⃣ Metadatos de Extracción")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Trazabilidad de Datos")
    
    extraction_log = {
        "Temporada": ["2013-2014", "2014-2015", "2015-2016"],
        "Archivo": ["champions_2013_2014.csv", "champions_2014_2015.csv", "champions_2015_2016.csv"],
        "Fecha Extracción": ["2024-11-30", "2024-11-30", "2024-11-30"],
        "Registros": ["79-125", "79-125", "79-125"],
        "Versión": ["v1.0", "v1.0", "v1.0"]
    }
    
    df_extraction = pd.DataFrame(extraction_log)
    st.dataframe(df_extraction, use_container_width=True, hide_index=True)

with col2:
    st.subheader("🔐 Seguridad y Privacidad")
    st.markdown("""
    ### Datos Públicos
    - ✅ Toda la información es **pública y de dominio abierto**
    - ✅ No contiene datos personales identificables
    - ✅ Disponible sin restricciones de RGPD
    - ✅ No requiere anonimización
    
    ### Cumplimiento
    - ✅ Respeta términos de Kaggle CC0
    - ✅ Cita fuentes en documentación
    - ✅ No comercializa los datos
    - ✅ Fines académicos/analíticos
    """)

st.markdown("---")

# ============================================================================
# SECCIÓN 3: DICCIONARIO DE DATOS
# ============================================================================
st.header("3️⃣ Diccionario de Datos")

diccionario_campos = {
    "Campo": [
        "fecha",
        "equipo_local",
        "equipo_visitante",
        "goles_local",
        "goles_visitante",
        "fase",
        "estadio",
        "asistencia",
        "temporada"
    ],
    "Tipo": [
        "DATE",
        "VARCHAR",
        "VARCHAR",
        "INT",
        "INT",
        "VARCHAR",
        "VARCHAR",
        "INT",
        "VARCHAR"
    ],
    "Descripción": [
        "Fecha del partido (YYYY-MM-DD)",
        "Nombre oficial del equipo que juega en casa",
        "Nombre oficial del equipo que juega fuera",
        "Goles marcados por el equipo local",
        "Goles marcados por el equipo visitante",
        "Etapa del torneo (Grupos, Octavos, Cuartos, Semifinal, Final)",
        "Nombre del estadio donde se jugó",
        "Número de espectadores",
        "Temporada en formato YYYY_YYYY"
    ],
    "Ejemplo": [
        "2015-09-16",
        "Bayern Munich",
        "Maccabi Tel Aviv",
        "6",
        "0",
        "Grupos",
        "Allianz Arena",
        "75029",
        "2015_2016"
    ],
    "Nulable": [
        "NO",
        "NO",
        "NO",
        "NO",
        "NO",
        "SÍ",
        "SÍ",
        "SÍ",
        "NO"
    ]
}

df_diccionario = pd.DataFrame(diccionario_campos)
st.dataframe(df_diccionario, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# SECCIÓN 4: PROCESO DE EXTRACCIÓN
# ============================================================================
st.header("4️⃣ Proceso de Extracción")

st.subheader("🔄 Workflow de Ingesta")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    ### 1. Buscar
    Identificar fuente en Kaggle o StatsBomb
    """)

with col2:
    st.markdown("""
    ### 2. Descargar
    Obtener CSV en máquina local
    """)

with col3:
    st.markdown("""
    ### 3. Validar
    Revisar estructura y columnas
    """)

with col4:
    st.markdown("""
    ### 4. Organizar
    Renombrar y guardar en `static/datasets/`
    """)

with col5:
    st.markdown("""
    ### 5. Documentar
    Registrar en trazabilidad
    """)

st.markdown("---")

# ============================================================================
# SECCIÓN 5: CANTIDAD DE DATOS
# ============================================================================
st.header("5️⃣ Cantidad de Datos")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Temporadas",
        "3",
        "2013-2014 a 2015-2016"
    )

with col2:
    st.metric(
        "Partidos Estimados",
        "~300-400",
        "80-130 por temporada"
    )

with col3:
    st.metric(
        "Tamaño Total",
        "< 1 MB",
        "CSV sin comprimir"
    )

st.markdown("""
### Desglose por Temporada

| Temporada | Fase | Partidos | Registros |
|-----------|------|----------|-----------|
| 2015-2016 | Grupos | 48 | 48 |
| 2015-2016 | Eliminatoria | ~20 | 20 |
| **2015-2016 Subtotal** | | | **~68-70** |
| 2014-2015 | Grupos | 48 | 48 |
| 2014-2015 | Eliminatoria | ~20 | 20 |
| **2014-2015 Subtotal** | | | **~68-70** |
| 2013-2014 | Grupos | 48 | 48 |
| 2013-2014 | Eliminatoria | ~20 | 20 |
| **2013-2014 Subtotal** | | | **~68-70** |
| | | | |
| **TOTAL** | | | **~204-210 partidos** |
""")

st.markdown("---")

# ============================================================================
# SECCIÓN 6: CALIDAD ESPERADA
# ============================================================================
st.header("6️⃣ Estándares de Calidad")

quality_checks = {
    "Validación": [
        "Completitud de campos",
        "Coherencia de fechas",
        "Nombres de equipos consistentes",
        "Valores de goles no negativos",
        "Fases válidas",
        "Sin duplicados"
    ],
    "Criterio": [
        "> 95% registros con campos clave llenos",
        "Fechas en rango 2013-2016",
        "Sin variantes (ej: 'Barcelona' vs 'FC Barcelona')",
        "goles_local >= 0, goles_visitante >= 0",
        "Solo: Grupos, Octavos, Cuartos, Semifinal, Final",
        "Una fila por partido única (fecha + local + visitante)"
    ],
    "Acción si Falla": [
        "Rellenar con estadísticas o descartar fila",
        "Revisar y corregir o excluir",
        "Standarizar mediante lookup table",
        "Rechazar o investigar",
        "Revisar fuente o clasificar como 'Otro'",
        "Investigar y eliminar duplicado"
    ]
}

df_quality = pd.DataFrame(quality_checks)
st.dataframe(df_quality, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# SECCIÓN 7: POLÍTICA DE USO Y ALMACENAMIENTO
# ============================================================================
st.header("7️⃣ Política de Uso y Almacenamiento")

col1, col2 = st.columns(2)

with col1:
    st.subheader("💾 Almacenamiento")
    st.markdown("""
    **Ubicación**
    - Ruta: `proyecto_integrador/static/datasets/`
    - Formato: CSV UTF-8 (sin BOM)
    - Nomenclatura: `champions_YYYY_YYYY.csv`
    
    **Respaldo**
    - Copia en repositorio Git (< 1MB)
    - Versión original en Kaggle disponible siempre
    - No requiere backup externo
    """)

with col2:
    st.subheader("🔑 Acceso y Permisos")
    st.markdown("""
    **Acceso en Código**
    ```python
    import pandas as pd
    df = pd.read_csv(
        'static/datasets/champions_2015_2016.csv',
        encoding='utf-8'
    )
    ```
    
    **Permisos**
    - ✅ Lectura: Cualquiera
    - ✅ Análisis: Sin restricciones
    - ✅ Compartir: Cita fuente
    """)

st.markdown("---")

# ============================================================================
# SECCIÓN 8: FUENTES DE REFERENCIA
# ============================================================================
st.header("8️⃣ Fuentes de Referencia")

st.markdown("""
### Datasets Públicos Recomendados

1. **Kaggle - UEFA Champions League**
   - Link: https://www.kaggle.com/datasets/
   - Buscar: "UEFA Champions League matches"
   - Descargar: CSV con histórico

2. **StatsBomb Open Data**
   - Link: https://github.com/statsbomb/open-data
   - Ventaja: Datos completos y detallados
   - Formato: JSON

3. **Football-Data.co.uk**
   - Link: http://www.football-data.co.uk/
   - Cobertura: Liga y copas europeas
   - Actualizado: Semanalmente

### Documentación Complementaria

- 📖 Diccionario de datos: `static/datasets/diccionario_champions.json`
- 📋 Guía de limpieza: Ver sección siguiente (Data Cleaning)
- 🔗 Fuente original: Documentada en cada CSV
""")

st.markdown("---")

# ============================================================================
# SECCIÓN 9: CHECKLIST DE RECOLECCIÓN
# ============================================================================
st.header("9️⃣ Checklist de Recolección")

checklist_items = [
    ("✅", "Fuentes identificadas y documentadas"),
    ("✅", "Permisos y derechos verificados"),
    ("✅", "Archivos descargados de forma confiable"),
    ("✅", "Diccionario de datos creado"),
    ("✅", "Estructura de carpetas preparada"),
    ("✅", "Metadatos de extracción registrados"),
    ("✅", "Validaciones de calidad definidas"),
    ("✅", "Procesos de acceso documentados"),
    ("✅", "Backup y respaldo considerados"),
    ("✅", "Equipo tiene acceso a los datos")
]

for status, item in checklist_items:
    st.write(f"{status} {item}")

st.markdown("---")

st.success("✅ **ETAPA 2 COMPLETADA**: Datos recolectados y documentados. Listo para Exploración (EDA)")
