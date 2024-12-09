import pandas as pd
from data.data_loader import load_data
from data.data_preprocessing import preprocess_club_data, data_preprocessing_game_summary
from analysis.game_analysis import game_summary
from analysis.player_analysis import player_stats
from analysis.valuation_analysis import player_valuation
from utils.plotter import plot_market_trend, plot_top_players, plot_result_distribution, plot_attendance_trend, plot_home_away_performance
from analysis.market_trend import prepare_market_trend

def main():
    # Carregar os dados
    appearances, club_games, clubs, competitions, game_events, games, player_valuations, players = load_data()

    # Pré-processamento dos dados
    chelsea_id, chelsea_games, chelsea_appearances, chelsea_valuations, clubs_cleaned = preprocess_club_data(
        clubs, club_games, appearances, player_valuations, players,
    )


    print("Dados gerais")
    print(chelsea_games.keys())
    print(chelsea_appearances.keys())
    print(chelsea_valuations.keys())
    print(clubs_cleaned.keys())

    final_data = data_preprocessing_game_summary(players, games, game_events, club_games, 631)

    # Criar DataFrame de tendência de mercado
    market_trend = prepare_market_trend(chelsea_valuations)

    # Merge entre games e club_games
    chelsea_game_details = pd.merge(chelsea_games, games, on='game_id', how='inner')
    chelsea_game_details = chelsea_game_details[['game_id', 'date', 'own_goals', 'opponent_goals', 'is_win', 'home_club_id', 'away_club_id', 'home_club_name', 'away_club_name', 'attendance']]

    # Resumo dos jogos
    chelsea_game_summary = game_summary(chelsea_game_details)

    # Análise de jogadores
    chelsea_player_stats = player_stats(chelsea_appearances, players)

    # Análise de valorização
    player_avg_valuation = player_valuation(chelsea_valuations)

    print("Preparo Market trend")
    print(market_trend.head())
    print(market_trend.columns)

    # chelsea_game_summary = game_summary(final_data)
    print("Final Data colunas e head")
    print(final_data.head())
    print(final_data.columns)

    print("Resumo do Desempenho do Chelsea:")
    for key, value in chelsea_game_summary.items():
        print(f"{key}: {value}")
    
    # Plotando gráficos
    plot_result_distribution(chelsea_game_summary)
    plot_home_away_performance(chelsea_game_summary)
    plot_attendance_trend(chelsea_game_details)


    # Gráficos
    plot_market_trend(market_trend)
    plot_top_players(chelsea_player_stats)

if __name__ == '__main__':
    main()
