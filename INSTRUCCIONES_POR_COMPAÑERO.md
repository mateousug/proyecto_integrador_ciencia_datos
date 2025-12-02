# 📋 INSTRUCCIONES ESPECÍFICAS POR COMPAÑERO

---

## 👨‍💻 PARA BRAYAN - Etapas 4 y 5

### Tu Rol
Completar la **limpieza de datos** y **evaluación/interpretación** para transformar datos crudos en insights limpios y métricas clave.

### Archivos a Editar
1. `pages/4_4 Limpieza y preparación de datos.py`
2. `pages/5_5 Evaluación e interpretación de resultados.py`

---

### ETAPA 4️⃣: Limpieza y Preparación de Datos (6-8 horas)

#### Qué Debes Hacer

**1. Preparación Inicial**
```bash
# Descarga datos de Kaggle
# URL: https://www.kaggle.com/datasets/elvinagammed/the-champions-league/data

# Guarda en: static/datasets/
# Archivos esperados (2010-2021):
# - champions_2010_2011.csv
# - champions_2011_2012.csv
# - champions_2012_2013.csv
# - champions_2013_2014.csv
# - champions_2014_2015.csv
# - champions_2015_2016.csv
# - champions_2016_2017.csv
# - champions_2017_2018.csv
# - champions_2018_2019.csv
# - champions_2019_2020.csv
# - champions_2020_2021.csv

# NOTA: El sistema detecta automáticamente todos los archivos champions_*.csv
```

**2. Estructura de Código a Implementar**
```python
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

@st.cache_data
def cargar_datos_kaggle():
    """Carga todos los CSVs de Champions League"""
    # Implementar lectura desde static/datasets/

@st.cache_data  
def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica limpieza estándar según guía_estilos.md sección 5
    
    Incluir:
    1. Conversión de fechas
    2. Normalización de nombres de equipos
    3. Tratamiento de nulos
    4. Feature engineering
    5. Validación post-limpieza
    """

# En la página Streamlit:
# - Mostrar datos antes/después
# - Estadísticas comparativas
# - Validaciones de calidad
# - Función reutilizable
```

**3. Transformaciones Específicas a Aplicar**

Seguir exactamente los procedimientos en `documentation/guia_estilos.md` sección 5:

| Transformación | Método | Resultado Esperado |
|---|---|---|
| Fechas | `pd.to_datetime()` | YYYY-MM-DD estándar |
| Nombres equipos | `.str.strip().str.title()` | "Bayern Munich" (consistente) |
| Nulos en goles | `.fillna(0).astype(int)` | Valores numéricos válidos |
| Fases | Validar contra lista conocida | Solo: Grupos, Octavos, Cuartos, Semifinal, Final |
| Duplicados | `drop_duplicates()` | Registros únicos |

**4. Features a Crear**
```python
df['goles_totales'] = df['goles_local'] + df['goles_visitante']
df['diferencia_goles'] = df['goles_local'] - df['goles_visitante']
df['resultado'] = df.apply(lambda row: ... , axis=1)  # Local/Visitante/Empate
df['es_goleada'] = df['diferencia_goles'].abs() > 3
df['es_over_2_5'] = df['goles_totales'] > 2.5
df['año'] = df['fecha'].dt.year
df['mes'] = df['fecha'].dt.month
df['dia_semana'] = df['fecha'].dt.day_name()
```

**5. Validaciones de Calidad**
```python
# Verificar después de limpieza:
assert df['goles_local'].min() >= 0  # No goles negativos
assert df['goles_visitante'].min() >= 0
assert df['fecha'].notna().sum() == len(df)  # Sin nulos en fechas
assert len(df) == len(df.drop_duplicates(...))  # Sin duplicados
assert df['fase'].isin(['Grupos', 'Octavos', ...]).all()  # Fases válidas
```

#### Recursos Disponibles
- 📖 **Guía de estilos**: `documentation/guia_estilos.md` (sección 5)
- 📅 **Plan de ejecución**: `documentation/plan_ejecucion.md` (FASE 2-3)
- 💻 **Referencia de código**: `pages/3_3 ...` (ver cómo se usan los datos)
- 🎨 **Estilos Streamlit**: Ver Inicio.py y otras páginas

#### Commit Esperado
```bash
git commit -m "feat: limpieza y feature engineering de datos Champions

- Carga de CSVs desde Kaggle (3 temporadas)
- Normalización de nombres de equipos
- Tratamiento de valores nulos
- Creación de 8 features derivadas
- Validación post-limpieza
- Función reutilizable limpiar_datos_champions()"
```

---

### ETAPA 5️⃣: Evaluación e Interpretación (4-6 horas)

#### Qué Debes Hacer

**1. Cargar Datos Limpios**
```python
# Reutilizar función de etapa 4
df_limpio = cargar_y_limpiar_datos()
```

**2. Calcular Métricas Clave**
```python
# Goles promedio
goles_prom = df_limpio['goles_totales'].mean()

# Win rate local
win_rate_local = (df_limpio['resultado'] == 'Local').sum() / len(df_limpio)

# Over/Under 2.5
pct_over = (df_limpio['es_over_2_5']).sum() / len(df_limpio) * 100

# Rendimiento por fase
rendimiento_fase = df_limpio.groupby('fase').agg({
    'goles_local': 'mean',
    'goles_visitante': 'mean',
    'resultado': lambda x: (x == 'Local').sum() / len(x)
})

# Top equipos
top_equipos = df_limpio.groupby('equipo_local').agg({
    'goles_local': ['sum', 'mean'],
    'resultado': lambda x: (x == 'Local').sum()
})
```

**3. Visualizaciones a Crear**
```python
# Ejemplo con Plotly
fig1 = px.bar(...)  # Goles por fase
fig2 = px.line(...)  # Evolución temporal
fig3 = px.scatter(...) # Correlación
fig4 = px.pie(...)  # Over/Under
```

**4. Hallazgos y Recomendaciones**
- Identificar 5-10 patrones clave
- Generar recomendaciones accionables
- Documentar limitaciones y supuestos
- Alinear con KPIs de negocio

#### Commit Esperado
```bash
git commit -m "feat: evaluación e interpretación de resultados

- Cálculo de 8+ métricas clave
- Análisis por temporada y fase
- Rendimiento local vs visitante
- Identificación de equipos outliers
- 10 hallazgos principales
- Recomendaciones accionables"
```

---

### Checklist para Brayan

- [ ] Descargar CSVs de Kaggle
- [ ] Crear `static/datasets/` con 3 archivos CSV
- [ ] Editar 4_4 con código de limpieza
- [ ] Implementar 8 transformaciones
- [ ] Crear 8 features derivadas
- [ ] Hacer commit de 4_4
- [ ] Editar 5_5 con código de evaluación
- [ ] Calcular 8+ métricas
- [ ] Crear 4+ visualizaciones
- [ ] Hacer commit de 5_5
- [ ] Reportar completitud a Juan

---

## 👨‍💻 PARA TEO - Etapas 6 y 7

### Tu Rol
Completar la **comunicación de resultados** y **aplicación de IA generativa** para visualizar insights y permitir análisis conversacional.

### Archivos a Editar
1. `pages/6_6 Comunicación de resultados (Storytelling & Visualización).py`
2. `pages/7_7 Apliacación IA Generativa.py`

---

### ETAPA 6️⃣: Comunicación de Resultados (6-8 horas)

#### Qué Debes Hacer

**1. Dashboard Interactivo**
```python
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = cargar_datos_limpios()

# Crear filtros
col1, col2, col3 = st.columns(3)
with col1:
    temporada = st.selectbox("Temporada", df['año'].unique())
with col2:
    fase = st.selectbox("Fase", df['fase'].unique())
with col3:
    equipo = st.selectbox("Equipo", df['equipo_local'].unique())

# Filtrar datos
df_filtrado = df[
    (df['año'] == temporada) &
    (df['fase'] == fase) &
    ((df['equipo_local'] == equipo) | (df['equipo_visitante'] == equipo))
]
```

**2. KPIs en Tarjetas**
```python
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("⚽ Goles Promedio", f"{goles_prom:.2f}")
    
with col2:
    st.metric("🏆 Win Rate Local", f"{win_rate_local:.1f}%")
    
with col3:
    st.metric("📈 Over 2.5", f"{pct_over:.1f}%")
    
with col4:
    st.metric("🎯 Equipos", total_equipos)
```

**3. Gráficos Finales**
```python
# Usar paleta de colores UEFA
COLOR_PRIMARY = "#003366"
COLOR_SECONDARY = "#0066CC"
COLOR_ACCENT = "#FFD700"
COLOR_SUCCESS = "#28A745"
COLOR_DANGER = "#DC3545"

# Gráfico 1: Distribución de goles
fig1 = px.histogram(df_filtrado, x='goles_totales', 
                   color_discrete_sequence=[COLOR_PRIMARY])

# Gráfico 2: Rendimiento local vs visitante  
fig2 = px.bar(resultado_dist, color_discrete_sequence=[COLOR_SUCCESS, COLOR_DANGER])

# Gráfico 3: Evolución temporal
fig3 = px.line(df_filtrado.groupby('fecha')['goles_totales'].mean())

# Gráfico 4: Top 10 equipos
fig4 = px.bar(top_equipos, x='equipo', y='victorias')
```

**4. Narrativa de Storytelling**
```python
st.markdown("""
## 📊 Análisis de Champions League

### Contexto
La UEFA Champions League es la competición más prestigiosa...

### Hallazgo 1: Ventaja Local
Los equipos locales ganan el [X]% de los partidos...

### Hallazgo 2: Goles Altos
El [X]% de los partidos superan 2.5 goles...

### Recomendaciones
1. Para apostadores: Considera sobre/bajo basado en...
2. Para analistas: Estudia rendimiento por fase...
3. Para equipos: Prepárate para presión en casa/fuera...
""")
```

**5. Exportación de Datos**
```python
# Permitir descarga de resultados
csv = df_filtrado.to_csv(index=False)
st.download_button(
    label="Descargar datos (CSV)",
    data=csv,
    file_name="champions_analisis.csv"
)
```

#### Recursos Disponibles
- 📖 **Guía de estilos**: `documentation/guia_estilos.md` (sección 4)
- 🎨 **Paleta de colores**: Azul UEFA (#003366, #0066CC), Dorado (#FFD700)
- 📊 **Datos**: De etapa 5 de Brayan
- 💡 **Inspiración**: Ver Inicio.py para estructura

#### Commit Esperado
```bash
git commit -m "feat: dashboard interactivo y comunicación

- Dashboard con filtros por temporada, fase, equipo
- 4 KPIs principales en tarjetas
- 5+ gráficos Plotly interactivos
- Narrativa de storytelling
- Recomendaciones por stakeholder
- Descarga de datos"
```

---

### ETAPA 7️⃣: Aplicación IA Generativa (4-6 horas)

#### Qué Debes Hacer

**1. Configurar Gemini API**

Primero, crear `.streamlit/secrets.toml`:
```toml
gemini_api_key = "AIzaSyChnCK7i1avrHy91sdf0TVBRcZeVHflD7M"
```

**2. Crear Cliente de Gemini**
```python
import streamlit as st
import google.generativeai as genai

@st.cache_resource
def configurar_gemini():
    """Configura y retorna cliente de Gemini"""
    api_key = st.secrets.get("gemini_api_key")
    if not api_key:
        st.error("API Key de Gemini no configurada")
        st.stop()
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-pro')

modelo = configurar_gemini()
```

**3. Crear Interfaz de Chat**
```python
st.title("🤖 Asistente IA - Champions League Analytics")

# Historial de conversación
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Chat
for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])

# Input del usuario
prompt = st.chat_input("Pregunta sobre los datos de Champions League...")

if prompt:
    # Agregar pregunta al historial
    st.session_state.mensajes.append({"role": "user", "content": prompt})
    
    # Generar respuesta con Gemini
    contexto = generar_contexto_proyecto()
    respuesta = modelo.generate_content(f"{contexto}\n\nPregunta: {prompt}")
    
    # Agregar respuesta al historial
    st.session_state.mensajes.append({"role": "assistant", "content": respuesta.text})
    st.rerun()
```

**4. Inyectar Contexto del Proyecto**
```python
def generar_contexto_proyecto() -> str:
    """Genera contexto para Gemini basado en datos del proyecto"""
    
    df = cargar_datos_limpios()
    
    contexto = f"""
    Eres un analista deportivo experto en UEFA Champions League.
    
    CONTEXTO DEL PROYECTO:
    - Objetivo: Identificar patrones para pronósticos de apuestas
    - Temporadas: 2013-2014, 2014-2015, 2015-2016
    - Total partidos: {len(df)}
    - Equipos únicos: {df['equipo_local'].nunique()}
    
    ESTADÍSTICAS PRINCIPALES:
    - Goles promedio: {df['goles_totales'].mean():.2f}
    - Win rate local: {(df['resultado']=='Local').sum()/len(df)*100:.1f}%
    - Over 2.5 goles: {(df['es_over_2_5']).sum()/len(df)*100:.1f}%
    - Goleadas (>3): {(df['es_goleada']).sum()} partidos
    
    HALLAZGOS CLAVE:
    [Incluir hallazgos de etapa 5]
    
    RESPONDE SIEMPRE EN ESPAÑOL Y CON REFERENCIAS A LOS DATOS.
    """
    
    return contexto
```

**5. Modos de Consulta**
```python
st.markdown("### Modos de Consulta")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Análisis de Datos"):
        prompt = "¿Cuáles son los patrones más importantes en los datos?"
        st.session_state.prompt_inicial = prompt

with col2:
    if st.button("💰 Apuestas"):
        prompt = "¿Qué recomendaciones tienes para apuestas?"
        st.session_state.prompt_inicial = prompt

with col3:
    if st.button("📈 Tendencias"):
        prompt = "¿Cuáles son las tendencias a largo plazo?"
        st.session_state.prompt_inicial = prompt
```

**6. Validaciones de Privacidad**
```python
# Validar que no envíe PII
palabras_prohibidas = ['email', 'teléfono', 'contraseña', 'tarjeta']

if any(palabra in prompt.lower() for palabra in palabras_prohibidas):
    st.warning("⚠️ Pregunta contiene información sensible")
    st.stop()
```

#### Recursos Disponibles
- 📖 **Guía de estilos**: `documentation/guia_estilos.md` (sección 6)
- 🔑 **API Key**: AIzaSyChnCK7i1avrHy91sdf0TVBRcZeVHflD7M
- 📊 **Datos**: De etapa 5 de Brayan
- 💬 **Contexto**: Basado en análisis de etapas anteriores

#### Commit Esperado
```bash
git commit -m "feat: integración de Google Gemini para análisis conversacional

- Configuración de cliente Gemini
- Interfaz de chat con historial
- Inyección de contexto del proyecto
- 3 modos de consulta predefinidos
- Validaciones de privacidad
- Manejo de errores y rate limiting"
```

---

### Checklist para Teo

#### Etapa 6
- [ ] Entender datos de Brayan
- [ ] Diseñar layout del dashboard
- [ ] Crear filtros interactivos
- [ ] Implementar 4 KPIs
- [ ] Crear 5+ gráficos
- [ ] Redactar narrativa
- [ ] Agregar botones de descarga
- [ ] Hacer commit de 6_6

#### Etapa 7
- [ ] Configurar `.streamlit/secrets.toml`
- [ ] Instalar `google-generativeai`
- [ ] Crear cliente de Gemini
- [ ] Implementar interfaz de chat
- [ ] Inyectar contexto del proyecto
- [ ] Crear 3 modos de consulta
- [ ] Agregar validaciones
- [ ] Probar localmente
- [ ] Hacer commit de 7_7

---

## 🎯 COORDINACIÓN GENERAL

### Timeline Sugerida

| Semana | Brayan | Teo |
|--------|--------|-----|
| **Semana 1** | Etapas 4-5 (12-14h) | Prepara ambiente, revisa datos |
| **Semana 2** | Finaliza 5, reporta | Etapas 6-7 (10-12h) |
| **Semana 3** | Testing | Testing y ajustes finales |

### Commits Esperados por Persona

**Brayan:**
1. `feat: limpieza y feature engineering` (4_4)
2. `feat: evaluación e interpretación` (5_5)

**Teo:**
1. `feat: dashboard interactivo y comunicación` (6_6)
2. `feat: integración Google Gemini` (7_7)

### Comunicación

- **Cada 4 horas**: Estado en Discord/Slack
- **Antes de cambios**: Avisar al equipo
- **After commit**: Notificar con mensaje

---

## 📞 PREGUNTAS FRECUENTES

**Brayan**: ¿Dónde descargo los datos?
→ https://www.kaggle.com/datasets/elvinagammed/the-champions-league/data

**Teo**: ¿Dónde está la API Key de Gemini?
→ AIzaSyChnCK7i1avrHy91sdf0TVBRcZeVHflD7M (guardar en secrets.toml)

**Ambos**: ¿Qué si me bloqueo?
→ Revisa documentación, mira código de otras páginas, pregunta a Juan

---

**Última actualización**: 30 de noviembre de 2024  
**Estado**: Listo para que Brayan comience etapa 4  
**Próximo Evento**: Brayan reporta completitud de etapa 4
