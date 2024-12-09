import pandas as pd

def game_summary(game_details):
    """
    Função para resumir o desempenho do Chelsea em suas partidas.

    Parâmetros:
    - game_details (DataFrame): DataFrame contendo detalhes dos jogos.

    Retorna:
    - resumo (dict): Dicionário com métricas resumidas de desempenho.
    """
    total_games = len(game_details)
    total_wins = game_details['is_win'].sum()
    total_draws = ((game_details['own_goals'] == game_details['opponent_goals'])).sum()
    total_losses = total_games - total_wins - total_draws
    
    avg_goals_scored = game_details['own_goals'].mean()
    avg_goals_conceded = game_details['opponent_goals'].mean()
    
    home_games = game_details[game_details['home_club_id'] == 631]
    away_games = game_details[game_details['away_club_id'] == 631]
    
    home_win_rate = (home_games['is_win'].sum() / len(home_games)) * 100 if len(home_games) > 0 else 0
    away_win_rate = (away_games['is_win'].sum() / len(away_games)) * 100 if len(away_games) > 0 else 0
    
    avg_attendance = game_details['attendance'].mean()
    max_attendance = game_details['attendance'].max()
    
    resumo = {
        'Total de Jogos': total_games,
        'Vitórias': total_wins,
        'Empates': total_draws,
        'Derrotas': total_losses,
        'Média de Gols Marcados': round(avg_goals_scored, 2),
        'Média de Gols Sofridos': round(avg_goals_conceded, 2),
        'Taxa de Vitória em Casa (%)': round(home_win_rate, 2),
        'Taxa de Vitória Fora (%)': round(away_win_rate, 2),
        'Público Médio': round(avg_attendance, 2),
        'Maior Público': max_attendance
    }
    
    return resumo
