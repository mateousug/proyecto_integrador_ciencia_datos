# 🏆 Proyecto Integrador de Ciencia de Datos - UEFA Champions League Analytics

Análisis de datos históricos de la UEFA Champions League (2013-2016) para identificar patrones de éxito que permitan generar pronósticos deportivos con fines de análisis y apuestas.

---

## 📋 Tabla de Contenidos

1. [Estructura del Proyecto](#estructura-del-proyecto)
2. [Estado de Implementación](#estado-de-implementación)
3. [Configuración Inicial](#configuración-inicial)
4. [Ejecución](#ejecución)
5. [Descripción de Páginas](#descripción-de-páginas)
6. [Asignación de Tareas](#asignación-de-tareas)
7. [Datos y Fuentes](#datos-y-fuentes)
8. [Buenas Prácticas](#buenas-prácticas)
9. [Problemas Comunes](#problemas-comunes)

---

## 🗂️ Estructura del Proyecto

```
│   │   └── diccionario_datos.json                    # 📝 Crear con esquema
│   └── images/                                        # 📊 Para exportar gráficos
├── utils/                                             # 🔧 Crear módulos reutilizables
│   ├── __init__.py
│   ├── data_loader.py                                # 📥 Funciones de carga
│   ├── visualizations.py                             # 📊 Funciones de visualización
│   └── gemini_helper.py                              # 🤖 Funciones IA Generativa
├── .streamlit/
│   ├── config.toml                                   # ⚙️ Configuración
│   └── secrets.toml                                  # 🔐 NO versionar
├── .gitignore
├── README.md                                          # 📖 Este archivo
├── documentation/
│   ├── guia_estilos.md                               # 📋 Estándares de código
│   └── plan_ejecucion.md                             # 📅 Cronograma
└── requirements.txt                                   # 📦 Dependencias

```

---

## ✅ Estado de Implementación

### 🎯 COMPLETADO ✅

#### 1️⃣ **Inicio.py** - Portada del Proyecto
- ✅ Descripción general del proyecto
- ✅ Objetivo principal y KPIs
- ✅ Equipo de trabajo y roles
- ✅ Cronograma de ejecución
- ✅ Herramientas y stack tecnológico
- ✅ Navegación clara a cada sección

#### 2️⃣ **1_1 Definición del Problema y Objetivos**
- ✅ Problema de negocio claramente definido
- ✅ KPIs SMART con métricas específicas
- ✅ Stakeholders identificados
- ✅ Decisiones que soportará el análisis
- ✅ Alcance (in-scope y out-of-scope)
- ✅ Supuestos y restricciones
- ✅ Criterios de éxito del proyecto
- ✅ Descripción del dataset esperado
- ✅ Herramientas y cronograma

#### 3️⃣ **2_2 Recolección de Datos**
- ✅ Fuentes de datos identificadas (Kaggle, StatsBomb)
- ✅ Metadatos de extracción documentados
- ✅ Diccionario de datos completo
- ✅ Proceso de extracción paso a paso
- ✅ Cantidad de datos esperados
- ✅ Estándares de calidad definidos
- ✅ Política de almacenamiento y acceso
- ✅ Referencias y URLs de fuentes

#### 4️⃣ **3_3 Exploración Inicial (EDA)**
- ✅ Carga de datos de ejemplo
- ✅ Visión general del dataset (registros, columnas, período)
- ✅ Estructura de datos y tipos
- ✅ Detección de valores nulos
- ✅ Estadísticas descriptivas (media, mediana, desv. est., etc.)
- ✅ Distribuciones (histogramas, boxplots)
- ✅ Análisis de resultados (Local/Visitante/Empate)
- ✅ Análisis por fase del torneo
- ✅ Análisis de equipos principales
- ✅ Correlaciones y relaciones
- ✅ Detección de anomalías (goleadas, partidos sin goles)
- ✅ Hallazgos clave y recomendaciones

---

### 🔄 EN PROGRESO

#### 5️⃣ **4_4 Limpieza y Preparación de Datos** (Asignado a: **Brayan**)
**Estado**: ✅ Completado

**Qué debe incluir:**
- ✅ Carga de datos desde `static/datasets/`
- ✅ Tratamiento de valores nulos (estrategia por columna)
- ✅ Eliminación de duplicados
- ✅ Normalización de nombres de equipos (unificación de variantes)
- ✅ Conversión de tipos de datos
- ✅ Validación de rangos de fechas y valores
- ✅ Feature engineering:
  - `goles_totales` = goles_local + goles_visitante
  - `diferencia_goles` = goles_local - goles_visitante
  - `resultado` = clasificación (Local/Visitante/Empate)
  - `es_goleada` = diferencia > 3
  - `es_over_2_5` = goles_totales > 2.5
  - Características temporales (año, mes, día_semana)
- ✅ Validación post-limpieza
- ✅ Estadísticas comparativas (antes/después)
- ✅ Código reutilizable en función `limpiar_datos_champions()`

**Recursos disponibles:**
- Guía de estilos: `documentation/guia_estilos.md` (sección 5 - Manejo de Datos)
- Plan de ejecución: `documentation/plan_ejecucion.md` (FASE 2)
- Template de código en EDA para referencia de transformaciones

---

#### 6️⃣ **5_5 Evaluación e Interpretación de Resultados** (Asignado a: **Brayan**)
**Estado**: ✅ Completado

**Qué debe incluir:**
- ✅ Carga de datos limpios
- ✅ Métricas clave calculadas:
  - Goles promedio por partido
  - Win rate local vs visitante
  - Porcentaje Over/Under 2.5 goles
  - Frecuencia de goleadas
  - Rendimiento por fase
- ✅ Validación cruzada de hallazgos (comparación entre temporadas)
- ✅ Análisis de confiabilidad de datos
- ✅ Interpretación de patrones encontrados
- ✅ Alineación con KPIs del negocio
- ✅ Recomendaciones accionables para apostadores
- ✅ Identificación de puntos de mejora
- ✅ Limitaciones y supuestos

**Recursos disponibles:**
- Guía de estilos: `documentation/guia_estilos.md` (sección 4 - Visualización y sección 5 - Manejo de Datos)
- Datos limpios de página 4_4

---

### ⏳ PENDIENTE

#### 7️⃣ **6_6 Comunicación de Resultados** (Asignado a: **Teo**)
**Estado**: ✅ Completado

**Qué debe incluir:**
- ✅ Dashboard interactivo con:
  - Filtros por temporada, fase, equipo
  - Visualizaciones clave del análisis
  - Métricas en tarjetas (KPIs)
- ✅ Gráficos exploratorios:
  - Distribución de goles
  - Rendimiento local vs visitante
  - Evolución temporal
  - Top equipos
  - Análisis Over/Under
- ✅ Narrativa y storytelling:
  - Contexto del problema
  - Hallazgos principales
  - Impacto de cada insight
- ✅ Recomendaciones específicas para:
  - Apostadores
  - Analistas deportivos
  - Equipos técnicos
- ✅ Siguientes pasos y mejoras futuras
- ✅ Documentación de supuestos y limitaciones

**Recursos disponibles:**
- Guía de estilos: `documentation/guia_estilos.md` (sección 4 - Estándares de Visualización)
- Datos e insights de páginas 3_3 y 5_5
- Paleta de colores oficial: Azul UEFA (#003366, #0066CC, #FFD700)

---

#### 8️⃣ **7_7 Aplicación IA Generativa (Gemini)** (Asignado a: **Teo**)
**Estado**: ✅ Completado

**Qué debe incluir:**
- ✅ Configuración de Google Gemini API
- ✅ Interfaz de chat con preguntas libres
- ✅ Contexto del proyecto inyectado en prompts:
  - Problema y objetivos
  - KPIs principales
  - Resumen de datos
  - Hallazgos clave
- ✅ Modos de consulta:
  - Q&A sobre datos
  - Recomendaciones de apuestas
  - Explicación de métricas
  - Generación de reportes
- ✅ Historial de conversación
- ✅ Validaciones de privacidad (no enviar datos sensibles)
- ✅ Manejo de errores y límites de rate limiting

**Recursos necesarios:**
- API Key de Gemini: `AIzaSyChnCK7i1avrHy91sdf0TVBRcZeVHflD7M`
- Guardar en `.streamlit/secrets.toml`:
  ```toml
  gemini_api_key = "AIzaSyChnCK7i1avrHy91sdf0TVBRcZeVHflD7M"
  ```
- Guía de estilos: `documentation/guia_estilos.md` (sección 6 - Integración con Gemini)
- Contexto de datos de página 5_5

---

## ⚙️ Configuración Inicial

### 1. Crear estructura de carpetas

```bash
# Crear carpetas necesarias
mkdir -p static/datasets static/images utils .streamlit
```

### 2. Crear archivo de configuración Streamlit

Archivo: `.streamlit/config.toml`
```toml
[client]
showErrorDetails = true

[server]
enableStaticServing = true
enableXsrfProtection = true

[logger]
level = "info"
```

### 3. Crear archivo de secretos (NO versionar)

Archivo: `.streamlit/secrets.toml`
```toml
# API Key de Google Gemini (guardar tu clave real)
gemini_api_key = "AIzaSyChnCK7i1avrHy91sdf0TVBRcZeVHflD7M"

# Otros secretos si es necesario
database_url = "tu_url_aqui"
```

### 4. Verificar .gitignore

```
# No versionar secretos
.streamlit/secrets.toml
.env

# No versionar datos grandes
static/datasets/*.csv
*.xlsx

# Cache de Python
__pycache__/
*.py[cod]
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

**requirements.txt**:
```
streamlit==1.28.0
pandas==2.0.3
plotly==5.17.0
numpy==1.24.3
google-generativeai==0.3.0
```

---

## 🚀 Ejecución

### Opción 1: Ejecutar aplicación (Desarrollo)

```bash
streamlit run Inicio.py
```

La aplicación se abrirá en `http://localhost:8501`

### Opción 2: Ejecutar en modo producción

```bash
streamlit run Inicio.py --logger.level=error
```

### Opción 3: Con configuración personalizada

```bash
streamlit run Inicio.py --server.port=8080 --server.headless=true
```

---

## 📖 Descripción de Páginas

| # | Página | Estado | Responsable | Descripción |
|---|--------|--------|-------------|-------------|
| 🏠 | **Inicio.py** | ✅ Completo | Implementado | Portada y navegación principal |
| 1️⃣ | **Definición del Problema** | ✅ Completo | Implementado | Problema, KPIs, stakeholders y alcance |
| 2️⃣ | **Recolección de Datos** | ✅ Completo | Implementado | Fuentes, metadatos y diccionario de datos |
| 3️⃣ | **Exploración (EDA)** | ✅ Completo | Implementado | Análisis exploratorio y visualizaciones |
| 4️⃣ | **Limpieza de Datos** | 🔄 En Progreso | **Brayan** | Limpieza, feature engineering, validación |
| 5️⃣ | **Evaluación** | 🔄 En Progreso | **Brayan** | Métricas, interpretación, recomendaciones |
| 6️⃣ | **Comunicación** | ⏳ Pendiente | **Teo** | Dashboard, storytelling, visualizaciones finales |
| 7️⃣ | **IA Generativa** | ⏳ Pendiente | **Teo** | Chat con Gemini, análisis contextual |

---

## 👥 Asignación de Tareas

### **Brayan** - Etapas 4 y 5

#### 4_4 Limpieza y Preparación de Datos
**Objetivos:**
1. Cargar datos descargados de Kaggle
2. Aplicar transformaciones de limpieza
3. Generar features derivadas
4. Validar calidad post-limpieza

**Checklist:**
- [x] Leer archivos CSV de `static/datasets/`
- [x] Detectar y tratar valores nulos
- [x] Unificar nombres de equipos
- [x] Crear features: goles_totales, resultado, es_over_2_5, etc.
- [x] Validar tipos de datos
- [x] Eliminar duplicados
- [x] Mostrar estadísticas antes/después
- [x] Crear función reutilizable `limpiar_datos_champions()`
- [x] Hacer commit: `feat: limpieza y feature engineering`

#### 5_5 Evaluación e Interpretación
**Objetivos:**
1. Calcular métricas clave
2. Validar hallazgos
3. Generar recomendaciones
4. Alinear con negocio

**Checklist:**
- [x] Cargar datos limpios del paso anterior
- [x] Calcular goles promedio, win rate, Over/Under %
- [x] Análisis por temporada y fase
- [x] Comparar rendimiento local vs visitante
- [x] Identificar equipos outliers
- [x] Generar recomendaciones accionables
- [x] Documentar limitaciones y supuestos
- [x] Hacer commit: `feat: evaluación e interpretación`

---

### **Teo** - Etapas 6 y 7

#### 6_6 Comunicación de Resultados
**Objetivos:**
1. Crear dashboard interactivo
2. Contar historia de datos
3. Visualizar insights clave

**Checklist:**
- [x] Crear filtros interactivos (temporada, fase, equipo)
- [x] Agregar métricas clave en tarjetas
- [x] Implementar gráficos interactivos (Plotly)
- [x] Redactar narrativa de hallazgos
- [x] Generar recomendaciones visuales
- [x] Permitir exportación de datos/gráficos
- [x] Hacer commit: `feat: dashboard y comunicación`

#### 7_7 Aplicación IA Generativa
**Objetivos:**
1. Integrar Google Gemini
2. Permitir Q&A sobre datos
3. Generar análisis contextualizados

**Checklist:**
- [x] Configurar cliente de Gemini
- [x] Crear interfaz de chat
- [x] Inyectar contexto del proyecto en prompts
- [x] Implementar diferentes modos de consulta
- [x] Agregar validaciones de privacidad
- [x] Manejar errores y rate limiting
- [x] Hacer commit: `feat: integración con Gemini`

---

## 📊 Datos y Fuentes

### Fuentes Principales

| Fuente | URL | Formato | Cobertura | Licencia |
|--------|-----|---------|-----------|----------|
| **Kaggle** | https://www.kaggle.com/datasets/elvinagammed/the-champions-league/data | CSV | 2013-2016 | CC0 |
| **StatsBomb** | https://github.com/statsbomb/open-data | JSON | Histórico | CC0 |
| **Football-Data.co.uk** | http://www.football-data.co.uk/ | CSV | Años variados | Público |

### Descarga de Datos

**Paso 1:** Ir a Kaggle
```
https://www.kaggle.com/datasets/elvinagammed/the-champions-league/data
```

**Paso 2:** Descargar archivos CSV de temporadas:
- `champions_2015_2016.csv`
- `champions_2014_2015.csv`
- `champions_2013_2014.csv`

**Paso 3:** Guardar en:
```
static/datasets/
├── champions_2015_2016.csv
├── champions_2014_2015.csv
└── champions_2013_2014.csv
```

### Estructura de Datos Esperada

| Campo | Tipo | Descripción | Ejemplo |
|-------|------|-------------|---------|
| `fecha` | DATE | Fecha del partido | 2015-09-16 |
| `equipo_local` | VARCHAR | Equipo que juega en casa | Bayern Munich |
| `equipo_visitante` | VARCHAR | Equipo que viaja | Maccabi Tel Aviv |
| `goles_local` | INT | Goles del equipo local | 6 |
| `goles_visitante` | INT | Goles del equipo visitante | 0 |
| `fase` | VARCHAR | Etapa del torneo | Grupos, Octavos, Cuartos, Semifinal, Final |
| `estadio` | VARCHAR | Nombre del estadio | Allianz Arena |
| `asistencia` | INT | Espectadores (opcional) | 75029 |

---

## 📚 Buenas Prácticas

### 1. Nomenclatura y Estándares

Seguir guía en `documentation/guia_estilos.md`:

- **Archivos Python**: `snake_case` (ej: `data_loader.py`)
- **Variables**: `snake_case` descriptivo (ej: `goles_promedio`)
- **Funciones**: `snake_case` con docstring (ej: `cargar_datos_temporada()`)
- **Constantes**: `UPPER_CASE` (ej: `COLOR_PRIMARY = "#003366"`)

### 2. Commits Descriptivos

```bash
git commit -m "feat: agregar gráfico de distribución de goles"
git commit -m "fix: corregir normalización de nombres de equipos"
git commit -m "docs: actualizar diccionario de datos"
```

### 3. Reproducibilidad

- Usar semillas para valores aleatorios
- Documentar versiones de librerías
- Mantener datos versionados o con trazabilidad
- Scripts deben ser independientes de máquina

### 4. Seguridad

- **Nunca** subir `secrets.toml` a Git
- **Nunca** versionar datos sensibles
- Usar variables de entorno para configuraciones
- Validar inputs de usuarios

### 5. Documentación

- Comentarios en código explican **por qué**, no **qué**
- Docstrings en funciones con Args, Returns, Examples
- README actualizado con instrucciones claras
- Cambios importantes en comentarios de commit

---

## 🐛 Problemas Comunes

### Error: Módulos no encontrados (pandas, plotly, etc.)

**Solución:**
```bash
pip install pandas plotly streamlit google-generativeai
```

O desde requirements.txt:
```bash
pip install -r requirements.txt
```

---

### Error: `enableStaticServing = true` no funciona

**Verificar:**
1. `.streamlit/config.toml` existe y tiene la configuración
2. Archivos en `static/` existen realmente
3. Rutas son relativas: `static/datasets/archivo.csv`

**Solución:**
```toml
[server]
enableStaticServing = true
```

---

### Error: Clave de Gemini no encontrada

**Verificar:**
1. `.streamlit/secrets.toml` existe
2. Contiene: `gemini_api_key = "tu_clave_aqui"`
3. Acceso correcto: `st.secrets.get("gemini_api_key")`

**Solución:**
```python
import streamlit as st

api_key = st.secrets.get("gemini_api_key")
if not api_key:
    st.error("API Key de Gemini no configurada")
    st.stop()
```

---

### Error: CSV con caracteres extraños

**Solución:**
```python
df = pd.read_csv(
    'static/datasets/champions_2015_2016.csv',
    encoding='utf-8'
)
```

---

### Error: Duplicados en datos

**Verificar:**
```python
duplicados = df.duplicated(subset=['fecha', 'equipo_local', 'equipo_visitante'])
print(f"Duplicados encontrados: {duplicados.sum()}")
```

**Solución:**
```python
df = df.drop_duplicates(subset=['fecha', 'equipo_local', 'equipo_visitante'], keep='first')
```

---

## 📞 Contacto y Coordinación

**Equipo del Proyecto:**
- 👨‍💻 **Implementador**: Juan (Etapas 1-3 completadas)
- 🧹 **Limpieza/Evaluación**: **Brayan** (Etapas 4-5)
- 📊 **Comunicación/IA**: **Teo** (Etapas 6-7)

**Comunicación:**
- 📅 Reuniones cada 4 horas
- 💬 Actualizar status en Discord/Slack
- ⚠️ Notificar antes de cambios en archivos compartidos
- ✅ Hacer commits descriptivos

---

## 📅 Cronograma

| Fase | Duración | Estado | Responsable |
|------|----------|--------|-------------|
| 1. Configuración Inicial | 2-3h | ✅ Hecho | Implementador |
| 2. Recolección de Datos | 4-6h | ✅ Hecho | Implementador |
| 3. Análisis Exploratorio | 6-8h | ✅ Hecho | Implementador |
| **4. Limpieza de Datos** | **6-8h** | ✅ Hecho | **Brayan** |
| **5. Evaluación** | **4-6h** | ✅ Hecho | **Brayan** |
| **6. Comunicación** | **6-8h** | ✅ Hecho | **Teo** |
| **7. IA Generativa** | **4-6h** | ✅ Hecho | **Teo** |
| 8. Integración Final | 2-3h | ✅ Hecho | Todos |

---

## 📝 Notas Importantes

1. **Datos**: Descargar de Kaggle antes de ejecutar Brayan
2. **API Key**: Teo necesita configurar `secrets.toml` con clave de Gemini
3. **Commits**: Hacer después de cada etapa completada
4. **Testing**: Probar localmente antes de hacer push
5. **Documentación**: Actualizar README si hay cambios

---

**Última actualización**: 30 de noviembre de 2024  
**Versión**: 1.0  
**Estado General**: 100% Completado (9/9 etapas)
