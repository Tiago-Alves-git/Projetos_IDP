from utils.plotter import plot_market_trend
import pandas as pd

def analyze_team_valuation(chelsea_player_valuations):
    """
    Analisa a evolução da valorização do plantel do Chelsea ao longo do tempo.
    
    Parâmetros:
    - chelsea_player_valuations (DataFrame): Dados de avaliações de mercado de jogadores.

    Retorna:
    - DataFrame com média e soma de valores de mercado por ano.
    """
    chelsea_player_valuations['year'] = pd.to_datetime(chelsea_player_valuations['date']).dt.year
    valuation_analysis = chelsea_player_valuations.groupby('year').agg(
        total_market_value=('market_value_in_eur', 'sum'),
        avg_market_value=('market_value_in_eur', 'mean')
    ).reset_index()
    return valuation_analysis


def prepare_market_trend(chelsea_valuations):
    """
    Agrega os valores de mercado por data e retorna um DataFrame para análise temporal.
    """
    # Agregar por data
    chelsea_valuations['date'] = pd.to_datetime(chelsea_valuations['date'])
    market_trend = chelsea_valuations.groupby('date').agg({
        'market_value_in_eur': 'mean'
    }).reset_index()
    # Renomear a coluna para adequar à função de plot
    market_trend.rename(columns={
        'market_value_in_eur': 'avg_market_value'
    }, inplace=True)
    return market_trend