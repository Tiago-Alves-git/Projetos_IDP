import pandas as pd

def preprocess_club_data(clubs, club_games, appearances, player_valuations, players, games):
    """
    Pré-processa dados relacionados a um clube específico, neste caso o Chelsea FC.

    Args:
        clubs (DataFrame): Informações gerais sobre clubes.
        club_games (DataFrame): Jogos relacionados aos clubes.
        appearances (DataFrame): Informações sobre as participações dos jogadores nos jogos.
        player_valuations (DataFrame): Dados sobre a valorização dos jogadores.
        players (DataFrame): Informações gerais sobre os jogadores.
        games (DataFrame): Dados detalhados dos jogos.

    Returns:
        Tuple[DataFrame, DataFrame, DataFrame, DataFrame, DataFrame]: 
            Dados pré-processados sobre jogos, participações, avaliações, jogadores e informações gerais do Chelsea.
    """
    chelsea_id = 631

    # Processar jogos do Chelsea
    chelsea_games = club_games[club_games['club_id'] == chelsea_id].merge(
        games[['game_id', 'date', 'home_club_id', 'away_club_id', 'attendance', 'competition_id']],
        on='game_id',
        how='inner'
    )

    chelsea_games['is_home'] = chelsea_games['home_club_id'] == chelsea_id
    chelsea_games['is_win'] = chelsea_games['own_goals'] > chelsea_games['opponent_goals']
    chelsea_games['is_loss'] = chelsea_games['own_goals'] < chelsea_games['opponent_goals']
    chelsea_games['is_draw'] = chelsea_games['own_goals'] == chelsea_games['opponent_goals']

    # Processar aparições de jogadores do Chelsea
    chelsea_appearances = appearances[appearances['player_club_id'] == chelsea_id][[
        'appearance_id', 'game_id', 'player_id', 'player_club_id', 'date', 'player_name',
        'yellow_cards', 'red_cards', 'goals', 'assists', 'minutes_played'
    ]]
    
    # Processar avaliações de mercado de jogadores do Chelsea
    chelsea_player_valuations = player_valuations[
        player_valuations['current_club_id'] == chelsea_id
    ][['player_id', 'date', 'market_value_in_eur', 'current_club_id', 'player_club_domestic_competition_id']]

    # Filtrar jogadores do Chelsea
    chelsea_players = players[players['current_club_id'] == chelsea_id]
    
    # Remover colunas desnecessárias
    columns_to_drop = [
        'agent_name', 'image_url', 'player_code', 'first_name', 
        'last_name', 'city_of_birth', 'country_of_citizenship', 
        'contract_expiration_date', 'url'
    ]
    chelsea_players = chelsea_players.drop(columns=columns_to_drop)
    
    # Remover registros com dados inconsistentes nas colunas essenciais
    chelsea_players = chelsea_players.dropna(subset=['name', 'player_id', 'market_value_in_eur', 'highest_market_value_in_eur'])
    
    # Opcional: remover valores negativos ou fora do esperado (se aplicável)
    chelsea_players = chelsea_players[(chelsea_players['market_value_in_eur'] >= 0) & (chelsea_players['highest_market_value_in_eur'] >= 0)]
    
    # Tratar valores NaN em colunas restantes
    chelsea_players = chelsea_players.fillna({
        'height_in_cm': chelsea_players['height_in_cm'].mean(),  # Substituir por média
        'foot': 'unknown'  # Substituir valores ausentes por 'unknown'
    })
    

    # Obter informações gerais do clube Chelsea
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




