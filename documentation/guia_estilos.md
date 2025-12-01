# Guía de Estilos - Proyecto Champions League Analytics

## 1. Objetivo del Proyecto
Analizar datos históricos de la UEFA Champions League (antes de 2016) para identificar patrones de éxito que permitan generar pronósticos deportivos con fines de apuestas, análisis de rendimiento y comparación evolutiva de equipos.

---

## 2. Estructura de Archivos y Nomenclatura

### 2.1 Organización de Carpetas
```
proyecto_integrador_ciencia_datos/
├── Inicio.py
├── pages/
│   ├── 1_Definicion_Problema.py
│   ├── 2_Recoleccion_Datos.py
│   ├── 3_EDA.py
│   ├── 4_Limpieza_Preparacion.py
│   ├── 5_Visualizacion_Resultados.py
│   └── 6_IA_Generativa.py
├── static/
│   ├── datasets/
│   │   ├── champions_2015_2016.csv
│   │   ├── champions_2014_2015.csv
│   │   ├── champions_2013_2014.csv
│   │   └── diccionario_champions.json
│   └── images/
│       └── (logos, gráficos exportados)
├── utils/
│   ├── data_loader.py
│   ├── visualizations.py
│   └── gemini_helper.py
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── README.md
├── GUIA_ESTILOS.md
└── PLAN_EJECUCION.md
```

### 2.2 Nomenclatura de Archivos
- **Archivos Python**: `snake_case` (ej: `data_loader.py`)
- **Páginas Streamlit**: Usar prefijo numérico + nombre descriptivo (ej: `3_EDA.py`)
- **Datasets CSV**: `champions_YYYY_YYYY.csv` (ej: `champions_2015_2016.csv`)
- **Imágenes**: `descripcion_version.png` (ej: `distribucion_goles_v1.png`)

### 2.3 Nomenclatura de Variables y Funciones

#### Variables
```python
# ✅ CORRECTO
df_champions = pd.read_csv(...)
goles_local = df['home_goals']
equipos_top_10 = df.head(10)

# ❌ INCORRECTO
df = pd.read_csv(...)
x = df['home_goals']
top = df.head(10)
```

#### Funciones
```python
# ✅ CORRECTO
def cargar_datos_temporada(temporada: str) -> pd.DataFrame:
    """Carga datos de una temporada específica."""
    pass

def calcular_estadisticas_equipo(df: pd.DataFrame, equipo: str) -> dict:
    """Calcula estadísticas clave de un equipo."""
    pass

# ❌ INCORRECTO
def load(t):
    pass

def calc(df, e):
    pass
```

---

## 3. Estándares de Código Python

### 3.1 Imports
Orden estándar:
```python
# 1. Librerías estándar
import json
from datetime import datetime

# 2. Librerías de terceros
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# 3. Módulos locales
from utils.data_loader import cargar_datos_temporada
from utils.visualizations import grafico_goles_promedio
```

### 3.2 Docstrings
```python
def analizar_rendimiento_local_visitante(df: pd.DataFrame) -> dict:
    """
    Analiza el rendimiento de equipos como locales vs visitantes.
    
    Args:
        df: DataFrame con datos de partidos
        
    Returns:
        dict: Diccionario con estadísticas de local/visitante
        
    Ejemplo:
        >>> stats = analizar_rendimiento_local_visitante(df_champions)
        >>> print(stats['goles_promedio_local'])
    """
    pass
```

### 3.3 Configuración de Páginas Streamlit
```python
import streamlit as st

st.set_page_config(
    page_title="Champions Analytics - EDA",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Exploración de Datos - UEFA Champions League")
st.markdown("---")
```

---

## 4. Estándares de Visualización

### 4.1 Paleta de Colores
```python
# Colores principales (azul Champions League)
COLOR_PRIMARY = "#003366"      # Azul oscuro UEFA
COLOR_SECONDARY = "#0066CC"    # Azul medio
COLOR_ACCENT = "#FFD700"       # Dorado (trofeo)
COLOR_SUCCESS = "#28A745"      # Verde (victorias)
COLOR_DANGER = "#DC3545"       # Rojo (derrotas)
COLOR_WARNING = "#FFC107"      # Amarillo (empates)

# Paleta para gráficos
COLORS_TEAMS = ["#003366", "#0066CC", "#6699CC", "#99CCFF", "#CCE5FF"]
```

### 4.2 Tipos de Gráficos por Caso de Uso

#### Distribuciones
```python
# Histogramas para distribución de goles
fig = px.histogram(
    df, 
    x='total_goals',
    title='Distribución de Goles por Partido',
    color_discrete_sequence=[COLOR_PRIMARY]
)
fig.update_layout(template='plotly_white')
```

#### Comparaciones
```python
# Barras para comparar equipos
fig = px.bar(
    top_equipos,
    x='equipo',
    y='victorias',
    title='Top 10 Equipos por Victorias',
    color='victorias',
    color_continuous_scale='Blues'
)
```

#### Evolución temporal
```python
# Líneas para tendencias
fig = px.line(
    df_temporal,
    x='temporada',
    y='goles_promedio',
    title='Evolución de Goles Promedio por Temporada',
    markers=True
)
```

### 4.3 Formato Estándar de Gráficos
```python
# Configuración común para todos los gráficos
def aplicar_estilo_grafico(fig):
    fig.update_layout(
        template='plotly_white',
        font=dict(family="Arial, sans-serif", size=12),
        title_font_size=16,
        title_x=0.5,  # Centrar título
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig
```

---

## 5. Manejo de Datos

### 5.1 Carga de Datos
```python
def cargar_todas_temporadas(carpeta: str = "static/datasets") -> pd.DataFrame:
    """
    Carga y concatena todos los datasets de Champions League.
    
    Returns:
        DataFrame consolidado con columna 'temporada' agregada
    """
    archivos = [
        "champions_2015_2016.csv",
        "champions_2014_2015.csv",
        "champions_2013_2014.csv"
    ]
    
    dfs = []
    for archivo in archivos:
        df = pd.read_csv(f"{carpeta}/{archivo}")
        df['temporada'] = archivo.replace("champions_", "").replace(".csv", "")
        dfs.append(df)
    
    return pd.concat(dfs, ignore_index=True)
```

### 5.2 Columnas Esperadas en Datasets
```python
# Columnas mínimas requeridas en cada CSV:
COLUMNAS_REQUERIDAS = [
    'fecha',           # Fecha del partido
    'equipo_local',    # Nombre del equipo local
    'equipo_visitante',# Nombre del equipo visitante
    'goles_local',     # Goles del equipo local
    'goles_visitante', # Goles del equipo visitante
    'fase',            # Fase del torneo (grupos, octavos, cuartos, etc.)
    'estadio',         # Nombre del estadio
    'asistencia'       # Número de asistentes (opcional)
]
```

### 5.3 Limpieza Estándar
```python
def limpiar_datos_champions(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica limpieza estándar a datos de Champions."""
    df = df.copy()
    
    # Convertir fechas
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')
    
    # Unificar nombres de equipos (ej: "FC Barcelona" vs "Barcelona")
    df['equipo_local'] = df['equipo_local'].str.strip().str.title()
    df['equipo_visitante'] = df['equipo_visitante'].str.strip().str.title()
    
    # Calcular resultado
    df['resultado'] = df.apply(
        lambda row: 'Local' if row['goles_local'] > row['goles_visitante']
        else ('Visitante' if row['goles_local'] < row['goles_visitante'] else 'Empate'),
        axis=1
    )
    
    # Goles totales
    df['goles_totales'] = df['goles_local'] + df['goles_visitante']
    
    return df
```

---

## 6. Integración con Gemini (IA Generativa)

### 6.1 Configuración de Secretos
```toml
# .streamlit/secrets.toml
gemini_api_key = "TU_API_KEY_AQUI"
```

### 6.2 Estructura de Prompts
```python
def generar_prompt_analisis(contexto: str, pregunta: str) -> str:
    """Genera prompt estructurado para Gemini."""
    return f"""
Eres un analista deportivo experto en UEFA Champions League con conocimientos en:
- Estadísticas de fútbol y métricas de rendimiento
- Patrones históricos de equipos en competiciones europeas
- Probabilidades y pronósticos deportivos

CONTEXTO DEL PROYECTO:
{contexto}

DATOS DISPONIBLES:
- Temporadas: 2013-2014, 2014-2015, 2015-2016
- Variables: equipos, goles, fases del torneo, estadios

PREGUNTA DEL USUARIO:
{pregunta}

Por favor proporciona una respuesta clara, basada en datos y orientada a:
1. Identificar patrones de éxito
2. Generar insights accionables para pronósticos
3. Explicar métricas clave en lenguaje simple
"""
```

---

## 7. Buenas Prácticas de Desarrollo

### 7.1 Control de Versiones (Git)
```bash
# Nombres de ramas
main                    # Rama principal (solo código funcional)
feature/eda             # Nueva funcionalidad de EDA
feature/visualizaciones # Gráficos
fix/limpieza-datos      # Corrección de bugs

# Commits descriptivos
git commit -m "feat: agregar gráfico de goles promedio por fase"
git commit -m "fix: corregir carga de temporada 2014-2015"
git commit -m "docs: actualizar diccionario de datos"
```

### 7.2 Comentarios en Código
```python
# ✅ CORRECTO - Comentarios que explican "por qué"
# Usamos mediana en lugar de media porque hay outliers de goleadas
goles_tipicos = df['goles_totales'].median()

# Filtramos solo fase de grupos para análisis de regularidad
df_grupos = df[df['fase'] == 'Grupos']

# ❌ INCORRECTO - Comentarios que repiten el código
# Calcular la mediana
goles_tipicos = df['goles_totales'].median()
```

### 7.3 Manejo de Errores
```python
try:
    df = pd.read_csv(f"static/datasets/{archivo}")
except FileNotFoundError:
    st.error(f"⚠️ No se encontró el archivo: {archivo}")
    st.info("Verifica que el archivo esté en la carpeta static/datasets/")
    st.stop()
except pd.errors.EmptyDataError:
    st.error(f"⚠️ El archivo {archivo} está vacío")
    st.stop()
```

---

## 8. Checklist de Calidad

Antes de hacer commit, verificar:

- [ ] El código sigue la nomenclatura establecida
- [ ] Las funciones tienen docstrings
- [ ] Los gráficos usan la paleta de colores definida
- [ ] No hay datos sensibles en el código (API keys)
- [ ] Los archivos CSV están en `.gitignore` si son muy grandes (>10MB)
- [ ] Las páginas de Streamlit tienen títulos y descripciones claras
- [ ] Los mensajes de error son informativos para el usuario
- [ ] Se probó la funcionalidad localmente antes del push

---

## 9. Estructura de Presentación Final

### 9.1 Página de Inicio
- Logo/banner de Champions League
- Objetivo del proyecto en 2-3 líneas
- Navegación clara a cada sección
- Resumen ejecutivo con KPIs principales

### 9.2 Métricas Clave a Mostrar
```python
# KPIs principales en tarjetas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("⚽ Goles Promedio", f"{goles_prom:.2f}", delta="+0.3 vs 2014")

with col2:
    st.metric("🏆 Equipos Analizados", total_equipos)

with col3:
    st.metric("📊 Partidos Totales", total_partidos)

with col4:
    st.metric("🎯 Precisión Pronóstico", f"{precision:.1f}%")
```

### 9.3 Orden de Secciones
1. **Inicio**: Resumen ejecutivo y navegación
2. **Definición del Problema**: Objetivos y KPIs de apuestas
3. **EDA**: Análisis exploratorio con gráficos clave
4. **Insights**: Patrones identificados y recomendaciones
5. **Visualización Interactiva**: Dashboard con filtros
6. **IA Generativa**: Consultas con Gemini sobre los datos

---

## 10. Glosario de Términos

| Término | Definición |
|---------|------------|
| **Temporada** | Período de un año de competición (ej: 2015-2016) |
| **Fase** | Etapa del torneo (Grupos, Octavos, Cuartos, Semifinal, Final) |
| **Local/Visitante** | Equipo que juega en su estadio vs equipo que viaja |
| **Goleada** | Diferencia de 3+ goles |
| **Over/Under** | Apuesta sobre si habrá más o menos de X goles |
| **Cuota** | Probabilidad implícita en casas de apuestas |
| **ROI** | Retorno de inversión en apuestas |

---

**Fecha de creación**: 30 de noviembre de 2024  
**Versión**: 1.0  
**Mantenedores**: Equipo de desarrollo (3 personas)