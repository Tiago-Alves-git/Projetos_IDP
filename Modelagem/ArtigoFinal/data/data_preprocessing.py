import pandas as pd

def preprocess_club_data(clubs, club_games, appearances, player_valuations, players):
    # Identificar o ID do Chelsea
    chelsea_id = 631

    # Filtrar dados do Chelsea
    chelsea_games = club_games[club_games['club_id'] == chelsea_id]
    chelsea_appearances = appearances[appearances['player_club_id'] == chelsea_id]
    chelsea_valuations = player_valuations[player_valuations['current_club_id'] == chelsea_id]
    
    # Adicionar o nome dos jogadores ao DataFrame de valorações
    chelsea_valuations = pd.merge(
        chelsea_valuations,
        players[['player_id', 'name', 'highest_market_value_in_eur']],  # Inclui apenas as colunas necessárias
        on='player_id',
        how='left'
    )

    # Limpeza: Eliminar colunas que não serão usadas nas análises
    chelsea_valuations = chelsea_valuations[['player_id', 'name', 'highest_market_value_in_eur', 'market_value_in_eur', 'date']]

    # Adicionar a coluna 'highest_market_value_in_eur' se ela não existir
    if 'highest_market_value_in_eur' not in chelsea_valuations.columns:
        chelsea_valuations['highest_market_value_in_eur'] = 0  # Ou algum valor padrão

    # Limpar dados de clubes (se necessário, ajustando apenas as colunas de interesse)
    clubs_cleaned = clubs[['club_id', 'name', 'total_market_value', 'squad_size', 'average_age']]

    return chelsea_id, chelsea_games, chelsea_appearances, chelsea_valuations, clubs_cleaned


def data_preprocessing_game_summary(players, games, game_events, club_games, chelsea_club_id=631):
    """
    Pré-processa os dados para análise de desempenho do Chelsea em partidas.
    
    Parâmetros:
    - players (DataFrame): Tabela com informações dos jogadores.
    - games (DataFrame): Tabela com informações das partidas.
    - game_events (DataFrame): Tabela com eventos das partidas (somente gols).
    - club_games (DataFrame): Tabela com informações sobre clubes nas partidas.
    - chelsea_club_id (int): ID do Chelsea Football Club. Default: 631.
    
    Retorna:
    - DataFrame consolidado com informações para análise de partidas.
    """
    # 1. Seleção inicial dos jogos do Chelsea
    chelsea_games = club_games[club_games['club_id'] == chelsea_club_id].merge(games, on='game_id', how='inner')
    
    # 2. Adicionando informações sobre "em casa" ou "fora"
    chelsea_games['is_home'] = chelsea_games['home_club_id'] == chelsea_club_id

    # 3. Calculando resultados (vitória, empate, derrota)
    chelsea_games['own_goals'] = chelsea_games.apply(
        lambda x: x['home_club_goals'] if x['is_home'] else x['away_club_goals'], axis=1
    )
    chelsea_games['opponent_goals'] = chelsea_games.apply(
        lambda x: x['away_club_goals'] if x['is_home'] else x['home_club_goals'], axis=1
    )
    chelsea_games['is_win'] = chelsea_games['own_goals'] > chelsea_games['opponent_goals']
    chelsea_games['is_draw'] = chelsea_games['own_goals'] == chelsea_games['opponent_goals']
    chelsea_games['is_loss'] = chelsea_games['own_goals'] < chelsea_games['opponent_goals']

    # 4. Adicionando público (attendance) e outras informações relevantes
    chelsea_games['attendance'] = chelsea_games['attendance']

    # 5. Filtrando eventos de gols
    goals = game_events[game_events['type'] == 'Goals']
    
    # 6. Associando informações dos jogadores que marcaram gols
    goals = goals.merge(players[['player_id', 'name']], on='player_id', how='left')

    # Verificando as primeiras linhas para garantir que os dados estão corretos
    print("Gols associados aos jogadores:")
    print(goals[['game_id', 'player_id', 'name']].head())

    # 7. Consolidando métricas importantes
    chelsea_games['total_goals'] = chelsea_games['own_goals'] + chelsea_games['opponent_goals']
    chelsea_games['goals_scored_by'] = goals.groupby('game_id')['name'].apply(list)

    # 8. Filtrando apenas as colunas essenciais
    final_data = chelsea_games[[
        'game_id', 'date', 'is_home', 'own_goals', 'opponent_goals', 'is_win', 
        'is_draw', 'is_loss', 'attendance', 'total_goals', 'goals_scored_by'
    ]].copy()

    return final_data




