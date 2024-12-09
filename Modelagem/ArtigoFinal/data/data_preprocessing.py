import pandas as pd

def preprocess_club_data(clubs, club_games, appearances, player_valuations, players, games):
    # Manter essa função como está

    chelsea_id = 631

    chelsea_games = club_games[club_games['club_id'] == chelsea_id].merge(
    games[['game_id', 'date', 'home_club_id', 'away_club_id', 'attendance']],
    on='game_id',
    how='inner'
    )

    chelsea_games['is_home'] = chelsea_games['home_club_id'] == chelsea_id
    chelsea_games['is_win'] = chelsea_games['own_goals'] > chelsea_games['opponent_goals']
    chelsea_games['is_loss'] = chelsea_games['own_goals'] < chelsea_games['opponent_goals']
    chelsea_games['is_draw'] = chelsea_games['own_goals'] == chelsea_games['opponent_goals']

    chelsea_appearances = appearances[appearances['player_club_id'] == chelsea_id]

    chelsea_player_valuations = player_valuations[player_valuations['current_club_id'] == chelsea_id]

    chelsea_players = players[players['current_club_id'] == chelsea_id]

    chelsea_info = clubs[clubs['club_id'] == chelsea_id]

    return chelsea_games, chelsea_appearances, chelsea_player_valuations, chelsea_players, chelsea_info

def data_preprocessing_game_summary(players, games, game_events, club_games, chelsea_club_id=631):
    # refatorar esta função com base no que estamos buscando
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
    chelsea_games = club_games[club_games['club_id'] == chelsea_club_id].merge(games, on='game_id', how='inner')
    
    chelsea_games['is_home'] = chelsea_games['home_club_id'] == chelsea_club_id

    chelsea_games['own_goals'] = chelsea_games.apply(
        lambda x: x['home_club_goals'] if x['is_home'] else x['away_club_goals'], axis=1
    )
    chelsea_games['opponent_goals'] = chelsea_games.apply(
        lambda x: x['away_club_goals'] if x['is_home'] else x['home_club_goals'], axis=1
    )
    chelsea_games['is_win'] = chelsea_games['own_goals'] > chelsea_games['opponent_goals']
    chelsea_games['is_draw'] = chelsea_games['own_goals'] == chelsea_games['opponent_goals']
    chelsea_games['is_loss'] = chelsea_games['own_goals'] < chelsea_games['opponent_goals']

    chelsea_games['attendance'] = chelsea_games['attendance']

    goals = game_events[game_events['type'] == 'Goals']
    
    goals = goals.merge(players[['player_id', 'name']], on='player_id', how='left')

    print("Gols associados aos jogadores:")
    print(goals[['game_id', 'player_id', 'name']].head())

    chelsea_games['total_goals'] = chelsea_games['own_goals'] + chelsea_games['opponent_goals']
    chelsea_games['goals_scored_by'] = goals.groupby('game_id')['name'].apply(list)

    final_data = chelsea_games[[
        'game_id', 'date', 'is_home', 'own_goals', 'opponent_goals', 'is_win', 
        'is_draw', 'is_loss', 'attendance', 'total_goals', 'goals_scored_by'
    ]].copy()

    return final_data

## Criar novas funções aqui em baixo com base no que estamos buscando




