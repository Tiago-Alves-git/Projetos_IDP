import pandas as pd

def load_data():
    appearances = pd.read_csv('C:/Users/24101255/Documents/Tiago-Alves-Git/Projetos_IDP/Modelagem/ArtigoFinal/data/appearances.csv')
    club_games = pd.read_csv('C:/Users/24101255/Documents/Tiago-Alves-Git/Projetos_IDP/Modelagem/ArtigoFinal/data/club_games.csv')
    clubs = pd.read_csv('C:/Users/24101255/Documents/Tiago-Alves-Git/Projetos_IDP/Modelagem/ArtigoFinal/data/clubs.csv')
    competitions = pd.read_csv('C:/Users/24101255/Documents/Tiago-Alves-Git/Projetos_IDP/Modelagem/ArtigoFinal/data/competitions.csv')
    game_events = pd.read_csv('C:/Users/24101255/Documents/Tiago-Alves-Git/Projetos_IDP/Modelagem/ArtigoFinal/data/game_events.csv')
    games = pd.read_csv('C:/Users/24101255/Documents/Tiago-Alves-Git/Projetos_IDP/Modelagem/ArtigoFinal/data/games.csv')
    player_valuations = pd.read_csv('C:/Users/24101255/Documents/Tiago-Alves-Git/Projetos_IDP/Modelagem/ArtigoFinal/data/player_valuations.csv')
    players = pd.read_csv('C:/Users/24101255/Documents/Tiago-Alves-Git/Projetos_IDP/Modelagem/ArtigoFinal/data/players.csv')
    transfers = pd.read_csv('C:/Users/24101255/Documents/Tiago-Alves-Git/Projetos_IDP/Modelagem/ArtigoFinal/data/transfers.csv')
    game_lineups = pd.read_csv('C:/Users/24101255/Documents/Tiago-Alves-Git/Projetos_IDP/Modelagem/ArtigoFinal/data/game_lineups.csv')
    chelsea_valuation_in_year = pd.read_csv('C:/Users/24101255/Documents/Tiago-Alves-Git/Projetos_IDP/Modelagem/ArtigoFinal/data/chelsea_valuation.csv')
    chelsea_titles_in_year = pd.read_csv('C:/Users/24101255/Documents/Tiago-Alves-Git/Projetos_IDP/Modelagem/ArtigoFinal/data/chelsea_titles_2015_2023.csv')

    return appearances, club_games, clubs, competitions, game_events, games, player_valuations, players, transfers, game_lineups, chelsea_valuation_in_year,chelsea_titles_in_year
