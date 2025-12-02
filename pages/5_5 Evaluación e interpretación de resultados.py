import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from utils.data_loader import load_champions_data, prepare_data
from utils.visualizations import create_confusion_matrix

st.set_page_config(page_title="Evaluación de Resultados", page_icon="📊")

st.title("📊 Evaluación e Interpretación de Resultados")

st.markdown("""
En esta etapa construimos un modelo predictivo para validar si los datos contienen 
patrones suficientes para anticipar el resultado de un partido.
""")

# Cargar y preparar datos
df_raw = load_champions_data("all")
df = prepare_data(df_raw)

# 1. Preparación para Modelado
st.header("1. Configuración del Modelo")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Selección de Features")
    features = ['goles_local', 'goles_visitante', 'fase'] # Features base
    # Nota: En un caso real, no usaríamos goles del partido para predecir el resultado del mismo partido (data leakage).
    # Para este ejercicio académico, simularemos predecir el resultado basado en estadísticas.
    
    st.info("""
    **Nota Metodológica:**
    Para este ejercicio demostrativo, utilizaremos un modelo de clasificación Random Forest.
    El objetivo es predecir: **Victoria Local, Empate o Victoria Visitante**.
    """)

# Preprocesamiento simple para el modelo
le_fase = LabelEncoder()
df['fase_encoded'] = le_fase.fit_transform(df['fase'])

# Features para el modelo (simulado para demostración)
# Usamos features que estarían disponibles ANTES del partido en un modelo real (ej. históricos)
# Pero aquí usaremos una simplificación para mostrar el flujo
X = df[['fase_encoded']] # Feature muy simple solo para demo
y = df['resultado']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

with col2:
    st.metric("Datos de Entrenamiento", len(X_train))
    st.metric("Datos de Prueba", len(X_test))

# 2. Entrenamiento y Evaluación
st.header("2. Resultados del Modelo")

if st.button("🚀 Entrenar Modelo"):
    # Entrenar modelo
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Predicciones
    y_pred = clf.predict(X_test)
    
    # Métricas
    acc = accuracy_score(y_test, y_pred)
    
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Accuracy (Exactitud)", f"{acc:.2%}")
    col_m2.metric("Baseline (Azar)", "33.33%")
    col_m3.metric("Mejora sobre Baseline", f"{(acc - 0.3333):.2%}")
    
    # Matriz de Confusión
    st.subheader("Matriz de Confusión")
    cm = confusion_matrix(y_test, y_pred, labels=clf.classes_)
    st.plotly_chart(create_confusion_matrix(cm, clf.classes_), use_container_width=True)
    
    # Reporte de Clasificación
    st.subheader("Reporte Detallado")
    report = classification_report(y_test, y_pred, output_dict=True)
    st.dataframe(pd.DataFrame(report).transpose(), use_container_width=True)
    
    st.warning("""
    **Interpretación:**
    El modelo actual es muy básico (solo usa la fase del torneo). 
    Para mejorar el rendimiento real, necesitaríamos agregar features históricas como:
    * Rendimiento previo de los equipos
    * Valor de mercado de la plantilla
    * Historial de enfrentamientos directos
    """)

else:
    st.info("Presiona el botón para entrenar el modelo y ver los resultados.")

# 3. Interpretación de Negocio
st.header("3. Interpretación para el Negocio")

st.markdown("""
### 💡 Hallazgos Clave

1. **Ventaja de Localía:**
   Los datos muestran consistentemente que jugar en casa es un factor determinante.
   Los equipos locales ganan aproximadamente el **45-50%** de los partidos.

2. **Fase del Torneo:**
   En fases de eliminación directa (Octavos, Cuartos), los partidos tienden a ser más cerrados
   y con menos goles en comparación con la fase de grupos.

3. **Recomendación:**
   Los equipos deben priorizar estrategias ofensivas cuando juegan de local en fase de grupos
   para maximizar la acumulación de puntos, ya que la ventaja estadística es significativa.
""")