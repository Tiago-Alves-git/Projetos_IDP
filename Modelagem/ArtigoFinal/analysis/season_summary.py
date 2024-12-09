import pandas as pd

def analyze_performance_by_year(chelsea_games):
    """
    Analisa o desempenho do Chelsea por temporada.
    
    Parâmetros:
    - chelsea_games (DataFrame): Dados de jogos do Chelsea.

    Retorna:
    - DataFrame com contagem de vitórias, derrotas e empates por ano.
    """
    chelsea_games['year'] = pd.to_datetime(chelsea_games['date']).dt.year
    performance_analysis = chelsea_games.groupby('year').agg(
        wins=('is_win', 'sum'),
        losses=('is_loss', 'sum'),
        draws=('is_draw', 'sum')
    ).reset_index()
    return performance_analysis
