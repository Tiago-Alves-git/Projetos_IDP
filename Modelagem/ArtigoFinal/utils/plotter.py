import matplotlib.pyplot as plt
import seaborn as sns

def plot_market_trend(market_trend):
    """
    Plota um gráfico separado para cada ano, mostrando a evolução do valor de mercado médio do Chelsea.
    """
    # Garantir que a coluna 'year' esteja presente para separar os dados por ano
    market_trend['year'] = market_trend['date'].dt.year

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
    # Seleciona os top 10 jogadores por gols
    top_players = chelsea_player_stats.nlargest(10, 'total_goals')

    # Visualização
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_players, x='total_goals', y='name', palette='Blues_r', hue='name', dodge=False)
    plt.title('Top 10 Jogadores do Chelsea por Gols')
    plt.xlabel('Total de Gols')
    plt.ylabel('Jogadores')
    plt.tight_layout()
    plt.show()

def plot_game_summary(game_summary):
    """
    Plota gráficos de desempenho do Chelsea por jogos.
    """
    # Gráfico de barras para vitórias, empates e derrotas
    plt.figure(figsize=(12, 6))
    sns.barplot(x=['Vitórias', 'Empates', 'Derrotas'], 
                y=[game_summary['wins'], game_summary['draws'], game_summary['losses']], 
                palette='pastel')
    plt.title('Desempenho do Chelsea')
    plt.ylabel('Número de Jogos')
    plt.tight_layout()
    plt.show()

    # Gráfico de barras para gols marcados e sofridos
    plt.figure(figsize=(12, 6))
    sns.barplot(x=['Gols Marcados', 'Gols Sofridos'], 
                y=[game_summary['total_goals'], game_summary['total_goals_conceded']], 
                palette='coolwarm')
    plt.title('Gols Marcados e Sofridos pelo Chelsea')
    plt.ylabel('Quantidade de Gols')
    plt.tight_layout()
    plt.show()

def plot_result_distribution(summary):
    """
    Plota a distribuição de vitórias, empates e derrotas.
    
    Parâmetros:
    - summary (dict): Dicionário com métricas do desempenho.
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
    Plota o desempenho em casa e fora do Chelsea.
    
    Parâmetros:
    - summary (dict): Dicionário com métricas do desempenho.
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
    Plota a tendência de público nos jogos.
    
    Parâmetros:
    - game_details (DataFrame): DataFrame com detalhes dos jogos.
    """
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=game_details, x='date', y='attendance', label='Público', marker='o')
    plt.title('Tendência de Público nos Jogos do Chelsea')
    plt.xlabel('Data')
    plt.ylabel('Público')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
