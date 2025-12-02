"""
Módulo para crear visualizaciones interactivas con Plotly
"""
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Tema de colores consistente
COLORS = {
    'primary': '#1f77b4',
    'secondary': '#ff7f0e',
    'success': '#2ca02c',
    'danger': '#d62728',
    'warning': '#ff9800',
    'info': '#17a2b8',
    'dark': '#2c3e50',
    'light': '#ecf0f1'
}

TEMPLATE = 'plotly_white'


def create_goals_distribution(df: pd.DataFrame) -> go.Figure:
    """
    Crea histograma de distribución de goles totales
    """
    fig = px.histogram(
        df,
        x='total_goles',
        nbins=15,
        title='Distribución de Goles Totales por Partido',
        labels={'total_goles': 'Goles Totales', 'count': 'Frecuencia'},
        color_discrete_sequence=[COLORS['primary']],
        template=TEMPLATE
    )
    
    fig.update_layout(
        showlegend=False,
        hovermode='x unified',
        height=400
    )
    
    return fig


def create_goals_by_phase(df: pd.DataFrame) -> go.Figure:
    """
    Crea gráfico de barras de goles por fase del torneo
    """
    phase_stats = df.groupby('fase').agg({
        'goles_local': 'sum',
        'goles_visitante': 'sum'
    }).reset_index()
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Goles Local',
        x=phase_stats['fase'],
        y=phase_stats['goles_local'],
        marker_color=COLORS['primary']
    ))
    
    fig.add_trace(go.Bar(
        name='Goles Visitante',
        x=phase_stats['fase'],
        y=phase_stats['goles_visitante'],
        marker_color=COLORS['secondary']
    ))
    
    fig.update_layout(
        title='Goles por Fase del Torneo',
        xaxis_title='Fase',
        yaxis_title='Total de Goles',
        barmode='group',
        template=TEMPLATE,
        height=400,
        hovermode='x unified'
    )
    
    return fig


def create_top_teams_chart(stats_df: pd.DataFrame, top_n: int = 10) -> go.Figure:
    """
    Crea gráfico de barras horizontales con los mejores equipos
    """
    top_teams = stats_df.head(top_n).sort_values('diferencia_goles')
    
    fig = go.Figure(go.Bar(
        x=top_teams['diferencia_goles'],
        y=top_teams.index,
        orientation='h',
        marker=dict(
            color=top_teams['diferencia_goles'],
            colorscale='RdYlGn',
            showscale=True,
            colorbar=dict(title="Diferencia<br>de Goles")
        ),
        text=top_teams['diferencia_goles'],
        textposition='auto',
    ))
    
    fig.update_layout(
        title=f'Top {top_n} Equipos por Diferencia de Goles',
        xaxis_title='Diferencia de Goles',
        yaxis_title='Equipo',
        template=TEMPLATE,
        height=500,
        showlegend=False
    )
    
    return fig


def create_temporal_evolution(df: pd.DataFrame) -> go.Figure:
    """
    Crea gráfico de líneas de evolución temporal de goles
    """
    monthly_goals = df.groupby(df['fecha'].dt.to_period('M')).agg({
        'total_goles': 'sum',
        'goles_local': 'sum',
        'goles_visitante': 'sum'
    }).reset_index()
    
    monthly_goals['fecha'] = monthly_goals['fecha'].dt.to_timestamp()
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=monthly_goals['fecha'],
        y=monthly_goals['total_goles'],
        mode='lines+markers',
        name='Total',
        line=dict(color=COLORS['primary'], width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_goals['fecha'],
        y=monthly_goals['goles_local'],
        mode='lines+markers',
        name='Local',
        line=dict(color=COLORS['success'], width=2, dash='dash'),
        marker=dict(size=6)
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_goals['fecha'],
        y=monthly_goals['goles_visitante'],
        mode='lines+markers',
        name='Visitante',
        line=dict(color=COLORS['danger'], width=2, dash='dash'),
        marker=dict(size=6)
    ))
    
    fig.update_layout(
        title='Evolución Temporal de Goles',
        xaxis_title='Fecha',
        yaxis_title='Goles',
        template=TEMPLATE,
        height=400,
        hovermode='x unified',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig


def create_correlation_heatmap(df: pd.DataFrame) -> go.Figure:
    """
    Crea mapa de calor de correlaciones
    """
    numeric_cols = ['goles_local', 'goles_visitante', 'total_goles', 'diferencia_goles']
    corr_matrix = df[numeric_cols].corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='RdBu',
        zmid=0,
        text=corr_matrix.values.round(2),
        texttemplate='%{text}',
        textfont={"size": 12},
        colorbar=dict(title="Correlación")
    ))
    
    fig.update_layout(
        title='Matriz de Correlación',
        template=TEMPLATE,
        height=500,
        xaxis={'side': 'bottom'}
    )
    
    return fig


def create_result_distribution(df: pd.DataFrame) -> go.Figure:
    """
    Crea gráfico de pastel de distribución de resultados
    """
    result_counts = df['resultado'].value_counts()
    
    fig = go.Figure(data=[go.Pie(
        labels=result_counts.index,
        values=result_counts.values,
        hole=0.4,
        marker=dict(colors=[COLORS['success'], COLORS['warning'], COLORS['danger']]),
        textinfo='label+percent',
        textposition='outside'
    )])
    
    fig.update_layout(
        title='Distribución de Resultados',
        template=TEMPLATE,
        height=400,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        )
    )
    
    return fig


def create_goals_by_season(df: pd.DataFrame) -> go.Figure:
    """
    Crea gráfico de barras agrupadas por temporada
    """
    season_stats = df.groupby('temporada').agg({
        'total_goles': 'sum',
        'equipo_local': 'count'
    }).reset_index()
    
    season_stats['promedio_goles'] = (season_stats['total_goles'] / season_stats['equipo_local']).round(2)
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            name='Total de Goles',
            x=season_stats['temporada'],
            y=season_stats['total_goles'],
            marker_color=COLORS['primary']
        ),
        secondary_y=False,
    )
    
    fig.add_trace(
        go.Scatter(
            name='Promedio por Partido',
            x=season_stats['temporada'],
            y=season_stats['promedio_goles'],
            mode='lines+markers',
            marker=dict(size=12, color=COLORS['danger']),
            line=dict(width=3)
        ),
        secondary_y=True,
    )
    
    fig.update_xaxes(title_text="Temporada")
    fig.update_yaxes(title_text="Total de Goles", secondary_y=False)
    fig.update_yaxes(title_text="Promedio de Goles por Partido", secondary_y=True)
    
    fig.update_layout(
        title='Goles por Temporada',
        template=TEMPLATE,
        height=400,
        hovermode='x unified'
    )
    
    return fig


def create_stadium_analysis(df: pd.DataFrame, top_n: int = 10) -> go.Figure:
    """
    Crea análisis de estadios con más goles
    """
    stadium_stats = df.groupby('estadio').agg({
        'total_goles': 'sum',
        'equipo_local': 'count'
    }).reset_index()
    
    stadium_stats['promedio'] = (stadium_stats['total_goles'] / stadium_stats['equipo_local']).round(2)
    stadium_stats = stadium_stats.sort_values('total_goles', ascending=False).head(top_n)
    
    fig = go.Figure(data=[
        go.Bar(
            x=stadium_stats['estadio'],
            y=stadium_stats['total_goles'],
            marker_color=COLORS['primary'],
            text=stadium_stats['promedio'],
            texttemplate='Prom: %{text}',
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title=f'Top {top_n} Estadios con Más Goles',
        xaxis_title='Estadio',
        yaxis_title='Total de Goles',
        template=TEMPLATE,
        height=500,
        xaxis={'tickangle': -45}
    )
    
    return fig


def create_confusion_matrix(cm, labels):
    """
    Crea matriz de confusión interactiva
    """
    fig = go.Figure(data=go.Heatmap(
        z=cm,
        x=labels,
        y=labels,
        colorscale='Blues',
        text=cm,
        texttemplate='%{text}',
        textfont={"size": 14},
        colorbar=dict(title="Cantidad")
    ))
    
    fig.update_layout(
        title='Matriz de Confusión',
        xaxis_title='Predicción',
        yaxis_title='Real',
        template=TEMPLATE,
        height=500
    )
    
    return fig
