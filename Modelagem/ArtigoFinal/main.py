import pandas as pd
from data.data_loader import load_data
from data.data_preprocessing import preprocess_club_data, data_preprocessing_game_summary
from analysis.game_analysis import game_summary
from analysis.player_analysis import player_stats, analyze_goals_by_players
from analysis.valuation_analysis import player_valuation
from utils.plotter import plot_market_trend, plot_top_players, plot_result_distribution, plot_annual_attendance_trend, plot_home_away_performance, plot_game_summary, plot_correlation ,calculate_and_plot_correlation , calculate_and_plot_goals_correlation
from analysis.market_trend import analyze_team_valuation, prepare_market_trend
from analysis.attendance_year import analyze_attendance_by_year
from analysis.season_summary import analyze_performance_by_year

def main():
    # Carregar os dados
    appearances, club_games, clubs, competitions, game_events, games, player_valuations, players, transfers, game_lineups, chelsea_valuation_in_year, chelsea_titles_in_year = load_data()

    chelsea_games, chelsea_appearances, chelsea_player_valuations, chelsea_players, chelsea_info = preprocess_club_data(
    clubs, club_games, appearances, player_valuations, players, games
)
    market_trend = prepare_market_trend(chelsea_player_valuations)

    chelsea_goals_events = data_preprocessing_game_summary(players, games, game_events, club_games)

    # Usar as váriaveis retornadas pela função que irá processar tudo que tenha haver com o clube chelsea nas funções subsequentes
    goals_data = analyze_goals_by_players(chelsea_goals_events, chelsea_appearances, game_events)


    # Análise de público por ano
    attendance_data = analyze_attendance_by_year(chelsea_games)

    # Análise de valorização do plantel
    valuation_data = analyze_team_valuation(chelsea_player_valuations)

    # Análise de desempenho por ano
    performance_data = analyze_performance_by_year(chelsea_games)

    game_summary_data = game_summary(chelsea_games)

   # Plotar gráficos
    plot_market_trend(market_trend)
    plot_top_players(goals_data)
    plot_game_summary(game_summary_data)
    plot_result_distribution(game_summary_data)
    plot_home_away_performance(game_summary_data)
    plot_annual_attendance_trend(chelsea_games)
    plot_correlation(chelsea_games, chelsea_valuation_in_year)
    calculate_and_plot_correlation(chelsea_valuation_in_year, chelsea_titles_in_year)
    calculate_and_plot_goals_correlation(chelsea_valuation_in_year, chelsea_games)


if __name__ == '__main__':
    main()
