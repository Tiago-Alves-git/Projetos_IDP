import pandas as pd

def load_data():
    appearances = pd.read_csv('C:/Users/Tiago/Documents/Tiago-Alves/Idp-Codes/Projetos_IDP/Projetos_IDP/Modelagem/ArtigoFinal/data/appearances.csv')
    club_games = pd.read_csv('C:/Users/Tiago/Documents/Tiago-Alves/Idp-Codes/Projetos_IDP/Projetos_IDP/Modelagem/ArtigoFinal/data/club_games.csv')
    clubs = pd.read_csv('C:/Users/Tiago/Documents/Tiago-Alves/Idp-Codes/Projetos_IDP/Projetos_IDP/Modelagem/ArtigoFinal/data/clubs.csv')
    competitions = pd.read_csv('C:/Users/Tiago/Documents/Tiago-Alves/Idp-Codes/Projetos_IDP/Projetos_IDP/Modelagem/ArtigoFinal/data/competitions.csv')
    game_events = pd.read_csv('C:/Users/Tiago/Documents/Tiago-Alves/Idp-Codes/Projetos_IDP/Projetos_IDP/Modelagem/ArtigoFinal/data/game_events.csv')
    games = pd.read_csv('C:/Users/Tiago/Documents/Tiago-Alves/Idp-Codes/Projetos_IDP/Projetos_IDP/Modelagem/ArtigoFinal/data/games.csv')
    player_valuations = pd.read_csv('C:/Users/Tiago/Documents/Tiago-Alves/Idp-Codes/Projetos_IDP/Projetos_IDP/Modelagem/ArtigoFinal/data/player_valuations.csv')
    players = pd.read_csv('C:/Users/Tiago/Documents/Tiago-Alves/Idp-Codes/Projetos_IDP/Projetos_IDP/Modelagem/ArtigoFinal/data/players.csv')
    
    return appearances, club_games, clubs, competitions, game_events, games, player_valuations, players
