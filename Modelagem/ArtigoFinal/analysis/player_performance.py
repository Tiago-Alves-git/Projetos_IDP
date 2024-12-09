def analyze_player_performance(appearances):
    # Agrupar por jogador e calcular estatísticas
    player_stats = appearances.groupby('player_id').agg(
        total_goals=('goals', 'sum'),
        total_assists=('assists', 'sum'),
        total_minutes=('minutes_played', 'sum')
    ).reset_index()

    player_stats = player_stats.sort_values(by='total_goals', ascending=False)

    # Gerar gráfico
    return player_stats
