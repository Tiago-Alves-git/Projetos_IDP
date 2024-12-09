import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import pearsonr
from analysis.calculate_avg_goals_year import calculate_average_goals_per_year


def plot_market_trend(market_trend):
    """
    Plota um gráfico mostrando a evolução anual do valor de mercado médio do Chelsea.
    """
    # Garantir que a coluna 'year' esteja presente para separar os dados por ano
    market_trend['year'] = pd.to_datetime(market_trend['date']).dt.year

    # Calcular o valor médio anual
    annual_avg_market_value = market_trend.groupby('year')['avg_market_value'].mean().reset_index()

    # Criar o gráfico
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=annual_avg_market_value, x='year', y='avg_market_value', marker='o', color='b')

    # Ajustes do gráfico
    plt.title('Evolução Anual do Valor de Mercado Médio do Chelsea')
    plt.xlabel('Ano')
    plt.ylabel('Valor de Mercado Médio (€)')
    plt.grid(True)

    # Formatação dos ticks do eixo X
    plt.xticks(annual_avg_market_value['year'], rotation=45)  # Garantir que todos os anos apareçam
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
    sns.barplot(x='Categoria', y='Jogos', data=game_summary_df, palette='pastel', hue='Categoria', legend=False)
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
    sns.barplot(x='Categoria', y='Gols', data=goals_df, palette='coolwarm', hue='Categoria', legend=False)
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
    sns.barplot(x=categories, y=values, palette='Blues_d', hue=categories, legend=False)
    plt.title('Desempenho em Casa vs Fora')
    plt.xlabel('Categoria')
    plt.ylabel('Valores (%)')
    plt.tight_layout()
    plt.show()

def plot_annual_attendance_trend(game_details):
    """
    Plota a tendência da média de público nos jogos do Chelsea, por ano.
    """
    # Adicionar coluna de ano
    game_details['year'] = pd.to_datetime(game_details['date']).dt.year

    # Calcular a média de público por ano
    annual_avg_attendance = game_details.groupby('year')['attendance'].mean().reset_index()

    # Criar o gráfico
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=annual_avg_attendance, x='year', y='attendance', marker='o', color='b')

    # Ajustes do gráfico
    plt.title('Média Anual de Público nos Jogos do Chelsea')
    plt.xlabel('Ano')
    plt.ylabel('Público Médio')
    plt.grid(True)

    # Formatação dos ticks do eixo X
    plt.xticks(annual_avg_attendance['year'], rotation=45)  # Mostrar todos os anos
    plt.tight_layout()

    # Exibir o gráfico
    plt.show()

def plot_correlation(attendance_data, valuation_data):
    """
    Calcula e plota a correlação entre o valor estimado do Chelsea e o público médio anual.
    """
    # Adicionar coluna de ano para o público
    attendance_data['year'] = pd.to_datetime(attendance_data['date']).dt.year

    # Calcular a média de público por ano
    annual_avg_attendance = attendance_data.groupby('year')['attendance'].mean().reset_index()

    # Combinar os dois DataFrames pelo ano
    merged_data = pd.merge(annual_avg_attendance, valuation_data, on='year', how='inner')

    # Calcular a correlação
    correlation, _ = pearsonr(merged_data['attendance'], merged_data['value'])

    # Criar o gráfico de dispersão
    plt.figure(figsize=(10, 6))
    sns.regplot(data=merged_data, x='attendance', y='value', color='g', line_kws={"color": "r", "alpha": 0.7, "lw": 2})
    plt.title(f'Correlação entre Público Médio e Valor Estimado do Chelsea\nCorrelação de Pearson: {correlation:.2f}')
    plt.xlabel('Público Médio (por ano)')
    plt.ylabel('Valor Estimado (€ milhões)')
    plt.grid(True)
    plt.tight_layout()

    # Exibir o gráfico
    plt.show()
    
def calculate_and_plot_correlation(valuation_data, titles_data):
    """
    Calcula e plota a correlação entre o valor estimado do Chelsea e a variável "ganhou títulos relevantes".
    """
    # Renomear a coluna "ano" para "year" para facilitar o merge
    titles_data.rename(columns={"ano": "year"}, inplace=True)

    # Combinar os dois DataFrames pelo ano
    merged_data = pd.merge(valuation_data, titles_data, on="year", how="inner")

    # Converter valores booleanos para numéricos (True = 1, False = 0)
    merged_data['did_win_big_title'] = merged_data['did_win_big_title'].astype(int)

    # Calcular a correlação
    correlation, _ = pearsonr(merged_data['did_win_big_title'], merged_data['value'])

    # Criar o gráfico de dispersão
    plt.figure(figsize=(10, 6))
    sns.regplot(
        data=merged_data,
        x='did_win_big_title',
        y='value',
        color='b',
        line_kws={"color": "r", "alpha": 0.7, "lw": 2}
    )
    plt.title(f'Correlação entre Ganhar Títulos Relevantes e Valor Estimado do Chelsea\nCorrelação de Pearson: {correlation:.2f}')
    plt.xlabel('Ganhou Títulos Relevantes (1 = Sim, 0 = Não)')
    plt.ylabel('Valor Estimado (€ milhões)')
    plt.xticks([0, 1], labels=["Não", "Sim"])  # Personalizar os ticks do eixo X
    plt.grid(True)
    plt.tight_layout()
    
    plt.show()

def calculate_and_plot_goals_correlation(valuation_data, chelsea_games):
    """
    Calcula e plota a correlação entre o valor estimado do Chelsea e os gols médios marcados por ano.
    """
    # Obter a média de gols por ano
    average_goals_per_year = calculate_average_goals_per_year(chelsea_games)

    # Combinar os dois DataFrames pelo ano
    merged_data = pd.merge(valuation_data, average_goals_per_year, left_on='year', right_on='year', how='inner')

    # Calcular a correlação
    correlation, _ = pearsonr(merged_data['value'], merged_data['average_goals'])

    # Criar o gráfico de dispersão
    plt.figure(figsize=(10, 6))
    sns.regplot(
        data=merged_data,
        x='average_goals',
        y='value',
        color='purple',
        line_kws={"color": "red", "alpha": 0.7, "lw": 2}
    )
    plt.title(f'Correlação entre Gols Médios Marcados e Valor Estimado do Chelsea\nCorrelação de Pearson: {correlation:.2f}')
    plt.xlabel('Gols Médios Marcados (por ano)')
    plt.ylabel('Valor Estimado (€ milhões)')
    plt.grid(True)
    plt.tight_layout()

    # Exibir o gráfico
    plt.show()