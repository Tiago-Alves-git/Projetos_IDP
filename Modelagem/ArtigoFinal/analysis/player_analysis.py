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

def analyze_goals_by_players(chelsea_games, chelsea_appearances, game_events):
    """
    Analisa os jogadores responsáveis pelos gols do Chelsea em cada temporada.
    """
    # Filtrar eventos de gols
    goals_events = game_events[game_events['type'] == 'Goals']
    
    # Garantir que a coluna 'date' seja convertida para datetime
    game_events['date'] = pd.to_datetime(game_events['date'], errors='coerce')

    # Garantir que game_events e chelsea_appearances têm as colunas necessárias
    required_columns = ['player_id', 'date', 'game_id']
    for col in required_columns:
        if col not in goals_events.columns:
            raise ValueError(f"Coluna {col} não encontrada em game_events")
    
    if 'player_id' not in chelsea_appearances.columns:
        raise ValueError("Coluna player_id não encontrada em chelsea_appearances")

    print("Antes do merge:", goals_events.head())  # Depuração para conferir dados antes do merge

    # Combinar eventos de gols com aparições do Chelsea
    goals_events = goals_events.merge(chelsea_appearances[['player_id', 'player_name']], on='player_id', how='inner')

    # Adicionar a coluna do ano
    goals_events['year'] = pd.to_datetime(goals_events['date'], errors='coerce').dt.year

    # Depuração para garantir que as colunas necessárias foram adicionadas corretamente
    print("Após o merge:", goals_events.head())  # Verificação para conferir os dados pós-merge

    # Contar gols por jogador e temporada
    goals_by_players = (
        goals_events.groupby(['year', 'player_name'])
        .size()
        .reset_index(name='total_goals')
    )

    # Verificar os dados do resultado
    print("Gols por jogador por temporada:", goals_by_players.head())  # Verificando o resultado

    return goals_by_players



