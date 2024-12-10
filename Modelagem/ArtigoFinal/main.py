import pandas as pd
from data.data_loader import load_data
from data.data_preprocessing import preprocess_club_data, data_preprocessing_game_summary
from analysis.game_analysis import game_summary
from analysis.player_analysis import player_stats, analyze_goals_by_players
from analysis.valuation_analysis import player_valuation
from utils.plotter import plot_market_trend, plot_top_players, plot_result_distribution, plot_annual_attendance_trend, plot_home_away_performance, plot_game_summary, plot_correlation ,calculate_and_plot_correlation , calculate_and_plot_goals_correlation , plot_valuation_goals_correlation , plot_goals_assist_impact ,plot_pie_chart_title , plot_bar_chart_club_valuation , plot_regression_plot_valuation , heat_map_title_wins
from analysis.market_trend import analyze_team_valuation, prepare_market_trend
from analysis.attendance_year import analyze_attendance_by_year
from analysis.season_summary import analyze_performance_by_year
from analysis.player_valuation_goals import calculate_player_valuation_and_goals

# Função para printar todas as variáveis
def print_all_data(**kwargs):
    for name, data in kwargs.items():
        print(f"\n=== {name} ===")
        print(data)  # Isso assume que o conteúdo é exibível como DataFrame ou lista, dependendo do formato

# Exemplo de como chamar a função com suas variáveis


def main():
    # Carregar os dados
    appearances, club_games, clubs, competitions, game_events, games, player_valuations, players, transfers, game_lineups, chelsea_valuation_in_year, chelsea_titles_in_year = load_data()

    chelsea_games, chelsea_appearances, chelsea_player_valuations, chelsea_players, chelsea_info = preprocess_club_data(
    clubs, club_games, appearances, player_valuations, players, games
)
    
    print_all_data(
        chelsea_games=chelsea_games,
        chelsea_appearances=chelsea_appearances,
        chelsea_player_valuations=chelsea_player_valuations,
        chelsea_valuation_in_year=chelsea_valuation_in_year,
        chelsea_titles_in_year=chelsea_titles_in_year,
        chelsea_players=chelsea_players
    )

    market_trend = prepare_market_trend(chelsea_player_valuations)

    chelsea_goals_events = data_preprocessing_game_summary(players, games, game_events, club_games)

    goals_data = analyze_goals_by_players(chelsea_goals_events, chelsea_appearances, game_events)
    
    player_data = calculate_player_valuation_and_goals(chelsea_player_valuations, chelsea_appearances, players)

    game_summary_data = game_summary(chelsea_games)

   # Plotar gráficos
    plot_pie_chart_title(chelsea_titles_in_year)
    plot_bar_chart_club_valuation(chelsea_valuation_in_year)
    plot_regression_plot_valuation(chelsea_valuation_in_year)
    calculate_and_plot_correlation(chelsea_valuation_in_year, chelsea_titles_in_year)
    heat_map_title_wins(chelsea_valuation_in_year, chelsea_titles_in_year)
    plot_market_trend(market_trend)
    plot_top_players(goals_data)
    plot_game_summary(game_summary_data)
    plot_result_distribution(game_summary_data)
    plot_home_away_performance(game_summary_data)
    plot_annual_attendance_trend(chelsea_games)
    plot_correlation(chelsea_games, chelsea_valuation_in_year)
    calculate_and_plot_goals_correlation(chelsea_valuation_in_year, chelsea_games)
    plot_valuation_goals_correlation(player_data)
    plot_goals_assist_impact(appearances, player_valuations)


if __name__ == '__main__':
    main()
