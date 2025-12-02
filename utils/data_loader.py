"""
Módulo para cargar y procesar datos de Champions League
"""
import pandas as pd
import streamlit as st
from pathlib import Path

@st.cache_data
def load_champions_data(season: str = "all") -> pd.DataFrame:
    """
    Carga los datos de Champions League
    
    Args:
        season: "2013_2014", "2014_2015", "2015_2016", o "all" para todos
    
    Returns:
        DataFrame con los datos de Champions League
    """
    base_path = Path("static/datasets")
    
    datasets = {
        "2013_2014": base_path / "champions_2013_2014.csv",
        "2014_2015": base_path / "champions_2014_2015.csv",
        "2015_2016": base_path / "champions_2015_2016.csv"
    }
    
    if season == "all":
        dfs = []
        for season_name, file_path in datasets.items():
            df = pd.read_csv(file_path)
            df['temporada'] = season_name.replace("_", "-")
            dfs.append(df)
        return pd.concat(dfs, ignore_index=True)
    else:
        if season not in datasets:
            raise ValueError(f"Temporada inválida: {season}")
        df = pd.read_csv(datasets[season])
        df['temporada'] = season.replace("_", "-")
        return df


@st.cache_data
def get_data_info():
    """
    Retorna información sobre los datasets disponibles
    """
    base_path = Path("static/datasets")
    
    info = []
    for season in ["2013_2014", "2014_2015", "2015_2016"]:
        file_path = base_path / f"champions_{season}.csv"
        if file_path.exists():
            df = pd.read_csv(file_path)
            info.append({
                "Temporada": season.replace("_", "-"),
                "Archivo": file_path.name,
                "Filas": len(df),
                "Columnas": len(df.columns),
                "Tamaño (KB)": round(file_path.stat().st_size / 1024, 2)
            })
    
    return pd.DataFrame(info)


def prepare_data(df: pd.DataFrame, clean_duplicates: bool = False, impute_missing: bool = False, unify_consistency: bool = False) -> pd.DataFrame:
    """
    Prepara y limpia los datos para análisis
    
    Args:
        df: DataFrame con datos crudos
        clean_duplicates: Si es True, elimina filas duplicadas
        impute_missing: Si es True, imputa valores faltantes (numéricos con media, categóricos con moda)
        unify_consistency: Si es True, unifica categorías inconsistentes
    
    Returns:
        DataFrame procesado con features adicionales
    """
    df = df.copy()
    
    # 1. Limpieza de Duplicados
    if clean_duplicates:
        df = df.drop_duplicates()
        
    # 2. Imputación de Valores Faltantes
    if impute_missing:
        # Numéricos: Imputar con media
        numeric_cols = df.select_dtypes(include=['number']).columns
        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].mean())
            
        # Categóricos: Imputar con moda
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns
        for col in categorical_cols:
            if not df[col].mode().empty:
                df[col] = df[col].fillna(df[col].mode()[0])
                
    # 3. Consistencia de Datos
    if unify_consistency:
        # Ejemplo: Unificar nombres de estadios o equipos si hubiera inconsistencias conocidas
        # Normalización básica de strings (strip whitespace)
        str_cols = df.select_dtypes(include=['object']).columns
        for col in str_cols:
            df[col] = df[col].str.strip()
            
        # Ejemplo específico (placeholder para lógica futura)
        # if 'estadio' in df.columns:
        #     df['estadio'] = df['estadio'].replace({'Allianz Arena ': 'Allianz Arena'})
    
    # 4. Conversión de Tipos
    df['fecha'] = pd.to_datetime(df['fecha'])
    
    # 5. Feature Engineering
    df['total_goles'] = df['goles_local'] + df['goles_visitante']
    df['diferencia_goles'] = df['goles_local'] - df['goles_visitante']
    
    # 6. Variable Objetivo (Target)
    df['resultado'] = df['diferencia_goles'].apply(
        lambda x: 'Victoria Local' if x > 0 else ('Empate' if x == 0 else 'Victoria Visitante')
    )
    
    # 7. Features Temporales
    df['año'] = df['fecha'].dt.year
    df['mes'] = df['fecha'].dt.month
    df['dia_semana'] = df['fecha'].dt.day_name()
    
    # 8. Ordenar por fase
    fase_order = ['Grupos', 'Octavos', 'Cuartos', 'Semifinal', 'Final', 'Final Extra']
    df['fase'] = pd.Categorical(df['fase'], categories=fase_order, ordered=True)
    
    return df


def get_team_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula estadísticas por equipo
    
    Args:
        df: DataFrame con datos procesados
    
    Returns:
        DataFrame con estadísticas por equipo
    """
    # Partidos como local
    local_stats = df.groupby('equipo_local').agg({
        'goles_local': 'sum',
        'goles_visitante': 'sum',
        'equipo_local': 'count'
    }).rename(columns={
        'goles_local': 'goles_favor_local',
        'goles_visitante': 'goles_contra_local',
        'equipo_local': 'partidos_local'
    })
    
    # Partidos como visitante
    visitante_stats = df.groupby('equipo_visitante').agg({
        'goles_visitante': 'sum',
        'goles_local': 'sum',
        'equipo_visitante': 'count'
    }).rename(columns={
        'goles_visitante': 'goles_favor_visitante',
        'goles_local': 'goles_contra_visitante',
        'equipo_visitante': 'partidos_visitante'
    })
    
    # Combinar estadísticas
    stats = pd.DataFrame(index=list(set(local_stats.index) | set(visitante_stats.index)))
    
    for col in local_stats.columns:
        stats[col] = local_stats[col]
    for col in visitante_stats.columns:
        stats[col] = visitante_stats[col]
    
    stats = stats.fillna(0)
    
    # Totales
    stats['partidos_total'] = stats['partidos_local'] + stats['partidos_visitante']
    stats['goles_favor'] = stats['goles_favor_local'] + stats['goles_favor_visitante']
    stats['goles_contra'] = stats['goles_contra_local'] + stats['goles_contra_visitante']
    stats['diferencia_goles'] = stats['goles_favor'] - stats['goles_contra']
    
    # Victorias
    victorias_local = df[df['resultado'] == 'Victoria Local'].groupby('equipo_local').size()
    victorias_visitante = df[df['resultado'] == 'Victoria Visitante'].groupby('equipo_visitante').size()
    
    stats['victorias'] = 0
    for equipo in stats.index:
        v_local = victorias_local.get(equipo, 0)
        v_visitante = victorias_visitante.get(equipo, 0)
        stats.loc[equipo, 'victorias'] = v_local + v_visitante
    
    # Porcentaje de victorias
    stats['porcentaje_victorias'] = (stats['victorias'] / stats['partidos_total'] * 100).round(2)
    
    return stats.sort_values('diferencia_goles', ascending=False)


def sidebar_reload_button():
    """
    Agrega un botón en el sidebar para recargar los datos (limpiar caché)
    """
    st.sidebar.markdown("---")
    if st.sidebar.button("🔄 Recargar Datos", help="Limpia la caché para recargar cambios en los CSV"):
        st.cache_data.clear()
        st.rerun()
