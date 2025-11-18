import streamlit as st

st.title("Definición del problema y objetivos (Business Understanding)")

st.markdown("""
¿Qué es esta etapa?
- Define con palabras simples qué quieres lograr y por qué.
- El resultado es una frase clara con objetivos y cómo medir el éxito.

Cómo redactar el problema:
- Plantilla: "Queremos [acción] para [impacto] en [área/cliente]".
- Ejemplos:
  - "Reducir el churn de clientes en 15% en 12 meses".
  - "Predecir ventas del próximo trimestre para planificar inventario".
  - "Detectar posibles fraudes en transacciones en tiempo real".

KPIs (métricas de éxito):
- Deben ser SMART (Específicos, Medibles, Alcanzables, Relevantes, con Tiempo).
- Ejemplos:
  - Churn: tasa de cancelación mensual.
  - Ventas: error medio absoluto (MAE) de la predicción.
  - Fraude: recall en casos de fraude + tasa de falsos positivos aceptable.

Stakeholders:
- ¿Quién usa el resultado? (gerentes, marketing, finanzas, atención al cliente).
- Define decisiones que soportará el modelo/informe.
- Acordar criterios de éxito y restricciones (presupuesto, tiempos, regulaciones).

Alcance y supuestos:
- Qué sí y qué no se hará (anti-objetivos).
- Supuestos iniciales y riesgos (datos incompletos, cambios de negocio).

Checklist para completar:
- Problema escrito en una frase.
- KPIs definidos con umbrales.
- Stakeholders y decisiones identificadas.
- Criterios de éxito y límites acordados.
""")

st.info("Cuando avances, reemplaza estas indicaciones por la implementación correspondiente de esta etapa.")