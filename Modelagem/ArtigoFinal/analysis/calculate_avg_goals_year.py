import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_average_goals_per_year(chelsea_games):
    """
    Calcula a média de gols marcados pelo Chelsea por ano.
    """
    # Adicionar a coluna de ano
    chelsea_games['year'] = pd.to_datetime(chelsea_games['date']).dt.year

    # Calcular a média de gols marcados por ano
    average_goals_per_year = chelsea_games.groupby('year')['own_goals'].mean().reset_index()
    average_goals_per_year.rename(columns={'own_goals': 'average_goals'}, inplace=True)
    
    return average_goals_per_year