import pandas as pd

def player_valuation(chelsea_player_valuations):
    
    player_avg_valuation = chelsea_player_valuations.groupby('name').agg({
        'market_value_in_eur': 'mean',
        'highest_market_value_in_eur': 'max'
    }).reset_index()

    player_avg_valuation.rename(columns={
        'market_value_in_eur': 'avg_market_value',
        'highest_market_value_in_eur': 'peak_market_value'
    }, inplace=True)

    return player_avg_valuation
