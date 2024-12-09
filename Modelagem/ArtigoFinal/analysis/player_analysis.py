import pandas as pd

def player_stats(chelsea_appearances, players):
    # Agrupar por jogador e calcular estatísticas
    chelsea_player_stats = chelsea_appearances.groupby('player_id').agg(
        total_goals=('goals', 'sum'),
        total_assists=('assists', 'sum'),
        total_minutes=('minutes_played', 'sum')
    ).reset_index()

    # Calcular gols e assistências por 90 minutos
    chelsea_player_stats['goals_per_90'] = chelsea_player_stats['total_goals'] / (chelsea_player_stats['total_minutes'] / 90)
    chelsea_player_stats['assists_per_90'] = chelsea_player_stats['total_assists'] / (chelsea_player_stats['total_minutes'] / 90)

    # Juntar os nomes dos jogadores
    chelsea_player_stats = pd.merge(
        chelsea_player_stats, players[['player_id', 'name']], on='player_id', how='inner'
    )

    return chelsea_player_stats
