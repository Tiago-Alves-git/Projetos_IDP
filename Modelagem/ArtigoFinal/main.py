import pandas as pd
from data.data_loader import load_data
from data.data_preprocessing import preprocess_club_data, data_preprocessing_game_summary
from analysis.game_analysis import game_summary
from analysis.player_analysis import player_stats, analyze_goals_by_players
from analysis.valuation_analysis import player_valuation
from utils.plotter import plot_market_trend, plot_top_players, plot_result_distribution, plot_attendance_trend, plot_home_away_performance
from analysis.market_trend import analyze_team_valuation
from analysis.attendance_year import analyze_attendance_by_year
from analysis.season_summary import analyze_performance_by_year

def main():
    # Carregar os dados
    appearances, club_games, clubs, competitions, game_events, games, player_valuations, players, transfers, game_lineups, chelsea_valuation_in_year = load_data()

    chelsea_games, chelsea_appearances, chelsea_player_valuations, chelsea_players, chelsea_info = preprocess_club_data(
    clubs, club_games, appearances, player_valuations, players, games
)

    # Usar as váriaveis retornadas pela função que irá processar tudo que tenha haver com o clube chelsea nas funções subsequentes

    # Analise dos dados de publico total por ano divididos por jogos em casa e jogos fora
    attendance_data = analyze_attendance_by_year(chelsea_games)
    # print("Média de público por temporada:", attendance_data.head())

    # Analise de Valorização do Plantel ao Longo dos Anos Para identificar tendências de valorização do time.
    valuation_data = analyze_team_valuation(chelsea_player_valuations)
    # print("Valorização média por ano:", valuation_data.head())
    # Análise de desempenho
    performance_data = analyze_performance_by_year(chelsea_games)
    # print("Desempenho por temporada:", performance_data.head())

    # Análise de gols por jogador
    goals_data = analyze_goals_by_players(chelsea_games, chelsea_appearances, game_events)
    print("Data de gols" , game_events.columns)
    # print("Gols por jogador por temporada:", goals_data.head())

    # A ideia é que essas funções retornem as coisas em um formato mais organizado para aquilo que propusemos a analisar.
if __name__ == '__main__':
    main()
