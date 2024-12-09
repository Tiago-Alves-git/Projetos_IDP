import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_market_trend(market_trend):
    """
    Plota um gráfico separado para cada ano, mostrando a evolução do valor de mercado médio do Chelsea.
    """
    # Garantir que a coluna 'year' esteja presente para separar os dados por ano
    market_trend['year'] = pd.to_datetime(market_trend['date']).dt.year

    # Obter a lista de anos únicos
    unique_years = market_trend['year'].unique()

    # Gerar um gráfico para cada ano
    for year in unique_years:
        yearly_data = market_trend[market_trend['year'] == year]
        
        # Criar o gráfico para o ano
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=yearly_data, x='date', y='avg_market_value', marker='o', color='b')
        
        # Ajustes do gráfico
        plt.title(f'Evolução do Valor de Mercado Médio do Chelsea - {year}')
        plt.xlabel('Data')
        plt.ylabel('Valor de Mercado Médio (€)')
        plt.grid(True)
        
        # Formatação dos ticks do eixo X
        plt.xticks(rotation=45)  # Rotaciona as datas para facilitar a leitura
        plt.tight_layout()
        
        # Exibir o gráfico
        plt.show()


def plot_top_players(chelsea_player_stats):
    """
    Plota os top 10 jogadores do Chelsea por gols marcados.
    """
    top_players = chelsea_player_stats.nlargest(10, 'total_goals')

    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_players, x='total_goals', y='player_name', palette='Blues_r', hue='player_name', dodge=False)
    plt.title('Top 10 Jogadores do Chelsea por Gols')
    plt.xlabel('Total de Gols')
    plt.ylabel('Jogadores')
    plt.tight_layout()
    plt.show()

def plot_game_summary(summary):
    """
    Plota gráficos de desempenho do Chelsea por jogos a partir do resumo (dicionário).
    """
    # Gráfico de barras para vitórias, empates e derrotas
    game_summary_data = {
        'Categoria': ['Vitórias', 'Empates', 'Derrotas'],
        'Jogos': [summary['Vitórias'], summary['Empates'], summary['Derrotas']]
    }
    game_summary_df = pd.DataFrame(game_summary_data)

    plt.figure(figsize=(12, 6))
    sns.barplot(x='Categoria', y='Jogos', data=game_summary_df, palette='pastel')
    plt.title('Desempenho do Chelsea')
    plt.ylabel('Número de Jogos')
    plt.tight_layout()
    plt.show()

    # Gráfico de barras para gols marcados e sofridos
    goals_data = {
        'Categoria': ['Gols Marcados', 'Gols Sofridos'],
        'Gols': [summary['Média de Gols Marcados'], summary['Média de Gols Sofridos']]
    }
    goals_df = pd.DataFrame(goals_data)

    plt.figure(figsize=(12, 6))
    sns.barplot(x='Categoria', y='Gols', data=goals_df, palette='coolwarm')
    plt.title('Gols Marcados e Sofridos pelo Chelsea')
    plt.ylabel('Quantidade de Gols')
    plt.tight_layout()
    plt.show()

def plot_result_distribution(summary):
    """
    Plota a distribuição de vitórias, empates e derrotas a partir do resumo (dicionário).
    """
    results = ['Vitórias', 'Empates', 'Derrotas']
    values = [summary['Vitórias'], summary['Empates'], summary['Derrotas']]
    
    plt.figure(figsize=(8, 6))
    plt.bar(results, values, color=['green', 'yellow', 'red'])
    plt.title('Distribuição de Resultados')
    plt.xlabel('Resultados')
    plt.ylabel('Quantidade')
    plt.tight_layout()
    plt.show()

def plot_home_away_performance(summary):
    """
    Plota o desempenho em casa e fora do Chelsea a partir do resumo (dicionário).
    """
    categories = ['Vitórias', 'Taxa de Vitória em Casa (%)', 'Taxa de Vitória Fora (%)']
    values = [summary['Vitórias'], summary['Taxa de Vitória em Casa (%)'], summary['Taxa de Vitória Fora (%)']]
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=categories, y=values, palette='Blues_d')
    plt.title('Desempenho em Casa vs Fora')
    plt.xlabel('Categoria')
    plt.ylabel('Valores (%)')
    plt.tight_layout()
    plt.show()

def plot_attendance_trend(game_details):
    """
    Plota a tendência de público nos jogos do Chelsea.
    """
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=game_details, x='date', y='attendance', label='Público', marker='o')
    plt.title('Tendência de Público nos Jogos do Chelsea')
    plt.xlabel('Data')
    plt.ylabel('Público')
    plt.grid(True)
    plt.tight_layout()
    plt.show()