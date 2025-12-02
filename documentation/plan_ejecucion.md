# Plan de Ejecución - Proyecto Champions League Analytics

## Información General
- **Plazo**: 2 días (48 horas)
- **Equipo**: 3 desarrolladores (trabajo paralelo)
- **Entrega**: App Streamlit funcional
- **Enfoque**: Análisis exploratorio + visualización + IA Generativa

---

## Estrategia de Trabajo

### Principios
1. **Trabajo paralelo**: Cada persona puede trabajar en cualquier módulo
2. **Commits frecuentes**: Subir avances cada 2-3 horas para evitar conflictos
3. **Comunicación continua**: Avisar antes de modificar archivos compartidos
4. **Prioridad**: Funcionalidad > Estética (entregar algo que funcione bien)

### División Sugerida por Día

**DÍA 1 (Horas 1-24)**: Fundamentos y datos  
**DÍA 2 (Horas 25-48)**: Visualización e integración

---

## FASE 1: Configuración Inicial (2-3 horas)

### Tareas Críticas
- [ ] **Configurar repositorio Git**
  - Crear repo en GitHub
  - Clonar en las 3 máquinas
  - Verificar que todos pueden hacer push/pull

- [ ] **Preparar estructura de carpetas**
  ```bash
  mkdir -p static/datasets static/images utils
  touch utils/__init__.py utils/data_loader.py utils/visualizations.py utils/gemini_helper.py
  ```

- [ ] **Configurar Streamlit**
  - Crear `.streamlit/config.toml`:
    ```toml
    [theme]
    primaryColor = "#003366"
    backgroundColor = "#FFFFFF"
    secondaryBackgroundColor = "#F0F2F6"
    
    [server]
    enableStaticServing = true
    ```
  
  - Crear `.streamlit/secrets.toml`:
    ```toml
    gemini_api_key = "TU_API_KEY_AQUI"
    ```
  
  - Actualizar `.gitignore`:
    ```
    .venv
    .streamlit/secrets.toml
    __pycache__/
    *.pyc
    .DS_Store
    ```

- [ ] **Obtener API Key de Gemini**
  - Ir a https://aistudio.google.com/app/apikey
  - Crear API key gratuita
  - Guardar en `secrets.toml`

### Checkpoint 1
✅ Todos pueden ejecutar `streamlit run Inicio.py` sin errores  
✅ Git configurado y funcionando  
✅ Estructura de carpetas lista

---

## FASE 2: Datos (4-6 horas)

### 2.1 Recolección de Datos
- [ ] **Buscar y descargar datasets de Champions League**
  - Fuentes recomendadas:
    - Kaggle: "UEFA Champions League"
    - Football-Data.co.uk
    - StatsBomb (datos abiertos)
  
  - Buscar CSVs con estas columnas mínimas:
    ```
    fecha, equipo_local, equipo_visitante, goles_local, goles_visitante, fase
    ```

- [ ] **Organizar datasets**
  - Renombrar archivos: `champions_YYYY_YYYY.csv` (ej: `champions_2013_2014.csv`)
  - Guardar en `static/datasets/`
  - El sistema detecta automáticamente todos los archivos CSV

- [ ] **Crear diccionario de datos**
  - Archivo: `static/datasets/diccionario_datos.json`
  - Contenido:
    ```json
    {
      "fecha": "Fecha del partido (YYYY-MM-DD)",
      "equipo_local": "Equipo que juega en casa",
      "equipo_visitante": "Equipo visitante",
      "goles_local": "Goles marcados por equipo local",
      "goles_visitante": "Goles marcados por equipo visitante",
      "fase": "Fase del torneo (Grupos, Octavos, Cuartos, Semifinal, Final)",
      "estadio": "Nombre del estadio (opcional)",
      "asistencia": "Número de espectadores (opcional)"
    }
    ```

### 2.2 Crear Utilidades de Carga
- [ ] **Implementar `utils/data_loader.py`**
  ```python
  import pandas as pd
  import os
  
  def cargar_temporada(temporada: str) -> pd.DataFrame:
      """Carga datos de una temporada específica."""
      archivo = f"static/datasets/champions_{temporada}.csv"
      if not os.path.exists(archivo):
          raise FileNotFoundError(f"No se encontró {archivo}")
      return pd.read_csv(archivo)
  
  def cargar_todas_temporadas() -> pd.DataFrame:
      """Carga y concatena todas las temporadas."""
      temporadas = ['2015_2016', '2014_2015', '2013_2014']
      dfs = []
      
      for temp in temporadas:
          try:
              df = cargar_temporada(temp)
              df['temporada'] = temp
              dfs.append(df)
          except FileNotFoundError:
              continue
      
      if not dfs:
          raise ValueError("No se encontraron archivos de datos")
      
      return pd.concat(dfs, ignore_index=True)
  
  def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
      """Limpieza estándar de datos."""
      df = df.copy()
      
      # Convertir fechas
      df['fecha'] = pd.to_datetime(df['fecha'])
      
      # Estandarizar nombres de equipos
      df['equipo_local'] = df['equipo_local'].str.strip().str.title()
      df['equipo_visitante'] = df['equipo_visitante'].str.strip().str.title()
      
      # Calcular columnas derivadas
      df['goles_totales'] = df['goles_local'] + df['goles_visitante']
      df['diferencia_goles'] = df['goles_local'] - df['goles_visitante']
      df['resultado'] = df['diferencia_goles'].apply(
          lambda x: 'Local' if x > 0 else ('Visitante' if x < 0 else 'Empate')
      )
      
      return df
  ```

### Checkpoint 2
✅ Al menos 2 archivos CSV con datos reales descargados  
✅ `data_loader.py` funciona y puede cargar los datos  
✅ Datos limpios y con columnas derivadas

---

## FASE 3: Análisis Exploratorio (6-8 horas)

### 3.1 Actualizar Página de Definición del Problema
- [ ] **Editar `pages/1_Definicion_Problema.py`**
  ```python
  import streamlit as st
  
  st.title("⚽ Definición del Problema y Objetivos")
  
  st.markdown("""
  ## Problema de Negocio
  Generar pronósticos precisos de partidos de UEFA Champions League para 
  identificar oportunidades de apuestas con valor positivo (ROI > 0).
  
  ## Objetivos SMART
  1. **Identificar patrones** de rendimiento local vs visitante por equipo (temporadas 2013-2016)
  2. **Calcular métricas clave** para apuestas: probabilidad de Over 2.5 goles, ventaja local
  3. **Comparar equipos** por fase del torneo y evolución temporal
  4. **Predecir tendencias** basadas en estadísticas históricas
  
  ## KPIs Principales
  - **Goles promedio** por partido (global y por fase)
  - **Win rate local** vs visitante
  - **Frecuencia Over/Under 2.5** goles
  - **Top 10 equipos** por victorias, goles y diferencia
  
  ## Stakeholders
  - Apostadores deportivos (usuarios finales)
  - Analistas de datos deportivos
  - Equipos técnicos que buscan patrones de rivales
  
  ## Alcance
  ✅ Análisis descriptivo e identificación de patrones  
  ✅ Dashboard interactivo con filtros  
  ✅ Asistente IA para consultas sobre datos  
  ❌ Modelo predictivo de ML (fuera de alcance)  
  ❌ Datos en tiempo real (solo históricos)
  """)
  ```

### 3.2 Implementar EDA Principal
- [ ] **Editar `pages/3_EDA.py`**
  - Estructura recomendada:
    ```python
    import streamlit as st
    import pandas as pd
    from utils.data_loader import cargar_todas_temporadas, limpiar_datos
    from utils.visualizations import (
        grafico_distribucion_goles,
        grafico_victorias_local_visitante,
        grafico_goles_por_fase,
        grafico_evolucion_temporal
    )
    
    st.title("📊 Exploración de Datos")
    
    # Cargar datos
    with st.spinner("Cargando datos..."):
        df = cargar_todas_temporadas()
        df = limpiar_datos(df)
    
    # Métricas generales
    st.subheader("📈 Resumen General")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Partidos Totales", len(df))
    with col2:
        st.metric("Equipos Únicos", df['equipo_local'].nunique() + df['equipo_visitante'].nunique())
    with col3:
        st.metric("Goles Promedio", f"{df['goles_totales'].mean():.2f}")
    with col4:
        st.metric("% Victorias Locales", f"{(df['resultado']=='Local').sum()/len(df)*100:.1f}%")
    
    # Distribución de goles
    st.subheader("⚽ Distribución de Goles")
    st.plotly_chart(grafico_distribucion_goles(df), use_container_width=True)
    
    # Rendimiento local vs visitante
    st.subheader("🏠 Rendimiento Local vs Visitante")
    st.plotly_chart(grafico_victorias_local_visitante(df), use_container_width=True)
    
    # Goles por fase
    st.subheader("🏆 Goles por Fase del Torneo")
    st.plotly_chart(grafico_goles_por_fase(df), use_container_width=True)
    
    # Evolución temporal
    st.subheader("📅 Evolución por Temporada")
    st.plotly_chart(grafico_evolucion_temporal(df), use_container_width=True)
    
    # Top equipos
    st.subheader("🥇 Top 10 Equipos por Victorias")
    equipos_victorias = calcular_top_equipos(df)
    st.dataframe(equipos_victorias, use_container_width=True)
    ```

### Checkpoint 3
✅ Página de EDA muestra al menos 4 gráficos diferentes  
✅ Métricas generales calculadas correctamente  
✅ No hay errores al ejecutar la app

---

## FASE 4: Visualizaciones (6-8 horas)

### 4.1 Crear Funciones de Visualización
- [ ] **Implementar `utils/visualizations.py`**
  ```python
  import plotly.express as px
  import plotly.graph_objects as go
  import pandas as pd
  
  # Colores estándar
  COLOR_PRIMARY = "#003366"
  COLOR_SECONDARY = "#0066CC"
  COLOR_ACCENT = "#FFD700"
  
  def aplicar_estilo(fig):
      """Aplica estilo consistente a gráficos."""
      fig.update_layout(
          template='plotly_white',
          font=dict(family="Arial", size=12),
          title_font_size=16,
          title_x=0.5
      )
      return fig
  
  def grafico_distribucion_goles(df: pd.DataFrame):
      """Histograma de goles totales por partido."""
      fig = px.histogram(
          df,
          x='goles_totales',
          nbins=10,
          title='Distribución de Goles Totales por Partido',
          labels={'goles_totales': 'Goles Totales', 'count': 'Frecuencia'},
          color_discrete_sequence=[COLOR_PRIMARY]
      )
      fig.add_vline(x=2.5, line_dash="dash", line_color="red",
                    annotation_text="Over/Under 2.5")
      return aplicar_estilo(fig)
  
  def grafico_victorias_local_visitante(df: pd.DataFrame):
      """Comparación de resultados local vs visitante."""
      resultados = df['resultado'].value_counts()
      fig = px.pie(
          values=resultados.values,
          names=resultados.index,
          title='Distribución de Resultados',
          color_discrete_sequence=[COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT]
      )
      return aplicar_estilo(fig)
  
  def grafico_goles_por_fase(df: pd.DataFrame):
      """Goles promedio por fase del torneo."""
      goles_fase = df.groupby('fase')['goles_totales'].mean().sort_values(ascending=False)
      fig = px.bar(
          x=goles_fase.index,
          y=goles_fase.values,
          title='Goles Promedio por Fase del Torneo',
          labels={'x': 'Fase', 'y': 'Goles Promedio'},
          color=goles_fase.values,
          color_continuous_scale='Blues'
      )
      return aplicar_estilo(fig)
  
  def grafico_evolucion_temporal(df: pd.DataFrame):
      """Evolución de goles por temporada."""
      temporal = df.groupby('temporada').agg({
          'goles_totales': 'mean',
          'fecha': 'count'
      }).reset_index()
      temporal.columns = ['temporada', 'goles_promedio', 'num_partidos']
      
      fig = go.Figure()
      fig.add_trace(go.Scatter(
          x=temporal['temporada'],
          y=temporal['goles_promedio'],
          mode='lines+markers',
          name='Goles Promedio',
          line=dict(color=COLOR_PRIMARY, width=3)
      ))
      fig.update_layout(title='Evolución de Goles Promedio por Temporada')
      return aplicar_estilo(fig)
  ```

### 4.2 Crear Página de Visualización Avanzada
- [ ] **Editar `pages/5_Visualizacion_Resultados.py`**
  - Incluir:
    - Filtros interactivos (temporada, fase, equipo)
    - Dashboard con métricas clave
    - Comparador de 2 equipos
    - Tabla de estadísticas descargable

### Checkpoint 4
✅ Al menos 5 tipos de gráficos diferentes funcionando  
✅ Filtros interactivos operativos  
✅ Gráficos son claros y profesionales

---

## FASE 5: IA Generativa con Gemini (4-6 horas)

### 5.1 Configurar Helper de Gemini
- [ ] **Implementar `utils/gemini_helper.py`**
  ```python
  import streamlit as st
  import google.generativeai as genai
  
  def configurar_gemini():
      """Configura cliente de Gemini."""
      api_key = st.secrets.get("gemini_api_key")
      if not api_key:
          st.error("⚠️ No se encontró la API Key de Gemini")
          st.stop()
      genai.configure(api_key=api_key)
      return genai.GenerativeModel('gemini-pro')
  
  def generar_prompt_contexto(df):
      """Genera contexto del proyecto para Gemini."""
      return f"""
  Eres un analista deportivo experto en UEFA Champions League.
  
  DATOS DISPONIBLES:
  - Temporadas: {df['temporada'].unique().tolist()}
  - Total de partidos: {len(df)}
  - Equipos: {df['equipo_local'].nunique() + df['equipo_visitante'].nunique()}
  - Goles promedio: {df['goles_totales'].mean():.2f}
  - Win rate local: {(df['resultado']=='Local').sum()/len(df)*100:.1f}%
  
  OBJETIVO:
  Identificar patrones para pronósticos de apuestas deportivas.
  
  MÉTRICAS CLAVE:
  - Over/Under 2.5 goles
  - Ventaja de local vs visitante
  - Rendimiento por fase del torneo
  """
  
  def consultar_gemini(modelo, pregunta: str, contexto: str):
      """Realiza consulta a Gemini."""
      prompt = f"{contexto}\n\nPREGUNTA: {pregunta}\n\nRespuesta:"
      
      try:
          response = modelo.generate_content(prompt)
          return response.text
      except Exception as e:
          return f"Error al consultar Gemini: {str(e)}"
  ```

### 5.2 Crear Página de IA Generativa
- [ ] **Editar `pages/6_IA_Generativa.py`**
  ```python
  import streamlit as st
  from utils.data_loader import cargar_todas_temporadas, limpiar_datos
  from utils.gemini_helper import configurar_gemini, generar_prompt_contexto, consultar_gemini
  
  st.title("🤖 Asistente IA con Gemini")
  
  # Cargar datos
  df = cargar_todas_temporadas()
  df = limpiar_datos(df)
  
  # Configurar Gemini
  modelo = configurar_gemini()
  contexto = generar_prompt_contexto(df)
  
  st.markdown("""
  Haz preguntas sobre los datos de Champions League. Ejemplos:
  - ¿Qué equipos tienen mejor rendimiento como visitantes?
  - ¿En qué fase hay más goles?
  - ¿Cuál es la probabilidad de Over 2.5 goles?
  - Dame recomendaciones para apostar en semifinales
  """)
  
  # Interfaz de chat
  pregunta = st.text_input("Tu pregunta:")
  
  if st.button("Consultar"):
      if pregunta:
          with st.spinner("Gemini está pensando..."):
              respuesta = consultar_gemini(modelo, pregunta, contexto)
              st.markdown("### Respuesta:")
              st.write(respuesta)
      else:
          st.warning("Por favor escribe una pregunta")
  
  # Sugerencias rápidas
  st.markdown("### Consultas Rápidas")
  col1, col2 = st.columns(2)
  
  with col1:
      if st.button("📊 Análisis de goles"):
          respuesta = consultar_gemini(
              modelo,
              "Analiza los patrones de goles en Champions League",
              contexto
          )
          st.write(respuesta)
  
  with col2:
      if st.button("🏆 Mejores equipos"):
          respuesta = consultar_gemini(
              modelo,
              "¿Qué equipos tienen mejores estadísticas?",
              contexto
          )
          st.write(respuesta)
  ```

### Checkpoint 5
✅ Gemini responde correctamente a preguntas  
✅ El contexto del proyecto se pasa adecuadamente  
✅ Las respuestas son útiles y relevantes

---

## FASE 6: Integración y Pulido (4-6 horas)

### 6.1 Actualizar Página de Inicio
- [ ] **Editar `Inicio.py`**
  ```python
  import streamlit as st
  
  st.set_page_config(
      page_title="Champions Analytics",
      page_icon="⚽",
      layout="wide"
  )
  
  st.title("⚽ Champions League Analytics")
  st.markdown("### Análisis de datos históricos (2013-2016) para pronósticos deportivos")
  
  st.markdown("---")
  
  # Resumen ejecutivo
  col1, col2, col3 = st.columns(3)
  
  with col1:
      st.info("""
      **🎯 Objetivo**  
      Identificar patrones de éxito en Champions League para generar 
      pronósticos de apuestas con valor positivo.
      """)
  
  with col2:
      st.success("""
      **📊 Datos**  
      3 temporadas completas  
      (2013-2014, 2014-2015, 2015-2016)  
      Todas las fases del torneo
      """)
  
  with col3:
      st.warning("""
      **💡 Herramientas**  
      Python + Streamlit  
      Plotly para gráficos  
      Gemini para análisis IA
      """)
  
  st.markdown("---")
  
  # Navegación
  st.markdown("""
  ## 📋 Contenido del Proyecto
  
  1. **Definición del Problema** - Objetivos y KPIs
  2. **Recolección de Datos** - Fuentes y preparación
  3. **EDA** - Análisis exploratorio con gráficos
  4. **Limpieza** - Preparación de datos
  5. **Visualización** - Dashboard interactivo
  6. **IA Generativa** - Consultas con Gemini
  
  👈 **Usa el menú lateral para navegar**
  """)
  
  # Métricas rápidas (si hay datos disponibles)
  try:
      from utils.data_loader import cargar_todas_temporadas, limpiar_datos
      df = cargar_todas_temporadas()
      df = limpiar_datos(df)
      
      st.markdown("---")
      st.subheader("📈 Métricas Generales")
      
      col1, col2, col3, col4 = st.columns(4)
      
      with col1:
          st.metric("⚽ Partidos", len(df))
      with col2:
          st.metric("🏆 Equipos", df['equipo_local'].nunique())
      with col3:
          st.metric("📊 Goles/Partido", f"{df['goles_totales'].mean():.2f}")
      with col4:
          st.metric("🏠 Win% Local", f"{(df['resultado']=='Local').sum()/len(df)*100:.0f}%")
  
  except:
      st.info("💡 Los datos se cargarán cuando agregues los archivos CSV")
  ```

### 6.2 Completar Páginas Intermedias
- [ ] **`pages/2_Recoleccion_Datos.py`**
  - Documentar fuentes de datos
  - Mostrar estructura de archivos
  - Explicar proceso de limpieza

- [ ] **`pages/4_Limpieza_Preparacion.py`**
  - Mostrar antes/después de limpieza
  - Explicar transformaciones aplicadas
  - Mostrar datos finales

### 6.3 Testing y Ajustes
- [ ] Probar navegación completa
- [ ] Verificar que todos los gráficos cargan
- [ ] Revisar ortografía y redacción
- [ ] Optimizar tiempos de carga (caché de datos)
- [ ] Agregar mensajes de error informativos

### Checkpoint 6
✅ Todas las páginas funcionan sin errores  
✅ Navegación fluida  
✅ Visuales profesionales y consistentes  
✅ Gemini responde correctamente

---

## FASE 7: Documentación y Entrega (2-3 horas)

### 7.1 Actualizar README.md
- [ ] Instrucciones de instalación
- [ ] Cómo ejecutar la app
- [ ] Descripción de cada página
- [ ] Créditos y fuentes de datos

### 7.2 Crear Presentación
- [ ] Preparar demo de 5-10 minutos
- [ ] Capturas de pantalla de secciones clave
- [ ] Lista de insights principales
- [ ] Recomendaciones para apostadores

### 7.3 Checklist Final
- [ ] Todos los archivos en Git
- [ ] `.gitignore` actualizado (no subir secrets)
- [ ] README completo
- [ ] App funciona en las 3 máquinas
- [ ] Sin errores en consola
- [ ] Gráficos cargan rápidamente
- [ ] Gemini responde consistentemente

---

## Distribución de Trabajo Sugerida

### Opción A: Por Módulo
- **Persona 1**: Datos + Limpieza (FASE 2 + 3)
- **Persona 2**: Visualizaciones (FASE 4)
- **Persona 3**: IA Generativa + Integración (FASE 5 + 6)

### Opción B: Por Día
- **DÍA 1 - Todos**: FASE 1-3 (fundamentos)
- **DÍA 2 - Todos**: FASE 4-7 (visualización y entrega)

### Opción C: Por Página
- **Persona 1**: Páginas 1-2 + Inicio
- **Persona 2**: Páginas 3-4 + Visualizaciones
- **Persona 3**: Páginas 5-6 + Gemini

---

## Comunicación Recomendada

### Cada 4 horas
- Reunión rápida (15 min) en Discord/Zoom
- Compartir avances
- Resolver bloqueos
- Coordinar siguientes pasos

### Antes de cada commit
```bash
# Avisar en chat grupal:
"Voy a subir cambios en utils/data_loader.py"

# Hacer pull antes de trabajar
git pull origin main

# Commit descriptivo
git add .
git commit -m "feat: agregar función de carga de datos"
git push origin main

# Avisar al terminar
"Subí data_loader.py, pueden hacer pull"
```

---

## Solución de Problemas Comunes

### Error: Módulo no encontrado
```bash
pip install streamlit pandas plotly google-generativeai
```

### Error: No se cargan archivos CSV
- Verificar rutas relativas: `static/datasets/archivo.csv`
- Confirmar que `enableStaticServing = true` en config.toml

### Error: Gemini no responde
- Verificar API key en secrets.toml
- Revisar que hay saldo en la cuenta de Google AI Studio
- Probar con pregunta simple primero

### Conflictos de Git
```bash
# Si hay conflictos al hacer pull
git stash              # Guardar cambios locales
git pull origin main   # Traer cambios remotos
git stash pop          # Recuperar cambios locales
# Resolver conflictos manualmente
```

---

## Entregables Finales

1. **Repositorio Git** con todo el código
2. **App Streamlit funcional** (demo en vivo)
3. **README.md** con documentación completa
4. **Presentación** de 5-10 minutos mostrando:
   - Problema y objetivos
   - Datasets utilizados
   - 3-5 insights principales
   - Demo del dashboard
   - Demo de Gemini
   - Conclusiones y recomendaciones

---

## Criterios de Éxito

✅ **Funcionalidad (40%)**
- App corre sin errores
- Todos los gráficos cargan
- Gemini responde correctamente

✅ **Análisis (30%)**
- Al menos 5 gráficos diferentes
- Insights claros y útiles
- Métricas relevantes para apuestas

✅ **Presentación (20%)**
- Interfaz limpia y profesional
- Navegación intuitiva
- Redacción clara

✅ **Documentación (10%)**
- README completo
- Código comentado
- Fuentes citadas

---

**Última actualización**: 30 de noviembre de 2024  
**Próxima revisión**: Después de FASE 3 (Checkpoint 3)

¡Éxito con el proyecto! 🚀⚽