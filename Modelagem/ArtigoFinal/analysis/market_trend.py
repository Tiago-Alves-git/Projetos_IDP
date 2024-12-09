from utils.plotter import plot_market_trend
import pandas as pd

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

