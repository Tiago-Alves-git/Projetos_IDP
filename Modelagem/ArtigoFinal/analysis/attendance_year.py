import pandas as pd

def analyze_attendance_by_year(chelsea_games):
    """
    Analisa a média de público por temporada, diferenciando entre jogos em casa e fora.
    
    Parâmetros:
    - chelsea_games (DataFrame): Dados de jogos do Chelsea, incluindo informações sobre público.

    Retorna:
    - DataFrame com médias de público por temporada e tipo de jogo (casa/fora).
    """
    chelsea_games['year'] = pd.to_datetime(chelsea_games['date']).dt.year
    attendance_analysis = chelsea_games.groupby(['year', 'is_home'])['attendance'].mean().reset_index()
    attendance_analysis.rename(columns={'is_home': 'home_game', 'attendance': 'avg_attendance'}, inplace=True)
    return attendance_analysis
