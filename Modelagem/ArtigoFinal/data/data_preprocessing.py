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

def data_preprocessing_game_summary(players, games, game_events, club_games):
    """
    Pré-processa os dados para análise de desempenho do Chelsea em partidas.
    """
    # Primeiro, vamos garantir que a data no arquivo games está no formato datetime
    games['date'] = pd.to_datetime(games['date'], errors='coerce')

    # Associar os eventos de gol com os jogos, unindo com base no game_id
    game_events = game_events.merge(games[['game_id', 'date']], on='game_id', how='left')

    # Verificar se a data foi associada corretamente
    print("Após associar a data com os eventos de jogo:", game_events.head())  # Depuração

    # Filtrar os jogos do Chelsea (club_id == 631)
    chelsea_games = club_games[club_games['club_id'] == 631].merge(games, on='game_id', how='inner')
    
    chelsea_games['is_home'] = chelsea_games['home_club_id'] == 631

    chelsea_games['own_goals'] = chelsea_games.apply(
        lambda x: x['home_club_goals'] if x['is_home'] else x['away_club_goals'], axis=1
    )
    chelsea_games['opponent_goals'] = chelsea_games.apply(
        lambda x: x['away_club_goals'] if x['is_home'] else x['home_club_goals'], axis=1
    )
    chelsea_games['is_win'] = chelsea_games['own_goals'] > chelsea_games['opponent_goals']
    chelsea_games['is_draw'] = chelsea_games['own_goals'] == chelsea_games['opponent_goals']
    chelsea_games['is_loss'] = chelsea_games['own_goals'] < chelsea_games['opponent_goals']

    # Associar eventos de gols com jogadores
    goals = game_events[game_events['type'] == 'Goals']
    goals = goals.merge(players[['player_id', 'name']], on='player_id', how='left')

    # Garantir que os gols sejam agrupados corretamente por jogo e jogador
    chelsea_games['total_goals'] = chelsea_games['own_goals'] + chelsea_games['opponent_goals']
    chelsea_games['goals_scored_by'] = goals.groupby('game_id')['name'].apply(list)

    final_data = chelsea_games[[ 
        'game_id', 'date', 'is_home', 'own_goals', 'opponent_goals', 'is_win', 
        'is_draw', 'is_loss', 'attendance', 'total_goals', 'goals_scored_by'
    ]].copy()

    return final_data



## Criar novas funções aqui em baixo com base no que estamos buscando




