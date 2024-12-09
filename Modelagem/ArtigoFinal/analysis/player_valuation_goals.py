import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

def calculate_player_valuation_and_goals(chelsea_player_valuations, chelsea_appearances, players):
    """
    Calcula a média anual do valor de mercado e os gols dos jogadores.
    """
    # Converter a data para DateTime e extrair o ano
    chelsea_player_valuations['year'] = pd.to_datetime(chelsea_player_valuations['date']).dt.year
    chelsea_appearances['year'] = pd.to_datetime(chelsea_appearances['date']).dt.year


    # Calcular a média anual do valor de mercado por jogador
    player_valuation_by_year = chelsea_player_valuations.groupby(['player_id', 'year']).agg(
        avg_market_value=('market_value_in_eur', 'mean')
    ).reset_index()

    # Adicionar estatísticas dos jogadores (gols, assistências, etc.)
    chelsea_player_stats = chelsea_appearances.groupby(['player_id', 'year']).agg(
        total_goals=('goals', 'sum')
    ).reset_index()

    # Juntar os dados de valor de mercado e estatísticas de gols
    player_data = pd.merge(player_valuation_by_year, chelsea_player_stats, on=['player_id', 'year'], how='inner')

    # Adicionar o nome do jogador
    player_data = pd.merge(player_data, players[['player_id', 'name']], on='player_id', how='inner')

    return player_data