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
    
def plot_valuation_goals_correlation(player_data):
    """
    Plota a correlação entre o valor médio de mercado dos jogadores e o número de gols.
    """
    # Calcular a correlação de Pearson
    correlation, _ = pearsonr(player_data['avg_market_value'], player_data['total_goals'])

    # Criar o gráfico de dispersão
    plt.figure(figsize=(10, 6))
    sns.regplot(
        data=player_data,
        x='total_goals',
        y='avg_market_value',
        color='green',
        line_kws={"color": "red", "alpha": 0.7, "lw": 2}
    )
    plt.title(f'Correlação entre Valor de Mercado Médio e Gols\nCorrelação de Pearson: {correlation:.2f}')
    plt.xlabel('Total de Gols (por ano)')
    plt.ylabel('Valor Médio de Mercado (€)')
    plt.grid(True)
    plt.tight_layout()

    # Exibir o gráfico
    plt.show()

def plot_goals_assist_impact(appearances, player_valuations):
    # Filtrar jogadores do Chelsea (player_club_id = 631)
    chelsea_appearances = appearances[appearances["player_club_id"] == 631]
    
    # Fazer o merge para adicionar o valor de mercado aos dados de performance
    merged_data = pd.merge(chelsea_appearances, player_valuations, on="player_id", how="inner")
    
    # Plotando o gráfico
    plt.figure(figsize=(14, 10))

    # Plot aprimorado com melhor estética
    scatter = sns.scatterplot(
        data=merged_data,
        x="goals",
        y="market_value_in_eur",
        size="minutes_played",
        hue="assists",
        sizes=(50, 300),
        palette="coolwarm",
        edgecolor="black",
        alpha=0.8,  # Transparência para sobreposição mais clara
    )
    
    # Adicionando título, rótulos e legenda customizada
    scatter.set_title(
        "Impacto de Gols, Assistências e Minutos Jogados no Valor de Mercado (Chelsea)",
        fontsize=18,
        weight="bold",
    )
    scatter.set_xlabel("Gols Marcados", fontsize=14)
    scatter.set_ylabel("Valor de Mercado (€)", fontsize=14)
    
    # Ajustando escala do eixo Y (se necessário)
    scatter.set_yscale("log")  # Logaritmo para valores amplos (opcional)
    
    # Personalizando a legenda
    handles, labels = scatter.get_legend_handles_labels()
    legend_labels = [
        f"{label} Assistências" if label.isdigit() else label for label in labels
    ]
    plt.legend(
        handles=handles,
        labels=legend_labels,
        title="Legenda",
        title_fontsize=14,
        fontsize=12,
        loc="upper left",
        bbox_to_anchor=(1, 1),
    )
    
    # Adicionando linhas de tendência para indicar possíveis padrões
    sns.regplot(
        data=merged_data,
        x="goals",
        y="market_value_in_eur",
        scatter=False,
        color="gray",
        line_kws={"linestyle": "--", "alpha": 0.7},
    )
    
    # Habilitando grid para facilitar leitura
    plt.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.7)
    plt.tight_layout()
    plt.show()

## Plotagens profissas


def plot_pie_chart_title(chelsea_titles_in_year):
    sns.set_theme(style="whitegrid")
    title_counts = chelsea_titles_in_year['did_win_big_title'].value_counts()
    
    # Criar figura e eixo corretamente
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Usar o eixo para o gráfico de pizza
    ax.pie(title_counts, labels=['Won Titles', 'No Titles'], autopct='%1.1f%%', 
           startangle=90, colors=['#4CAF50', '#FFC107'])
    ax.set_title("Chelsea's Title Wins Distribution (2015-2023)", fontsize=14, fontweight='bold')
    
    plt.show()


def plot_bar_chart_club_valuation(chelsea_valuation_in_year):
    sns.set_theme(style="whitegrid")    
    
    # Criar a figura e o eixo corretamente
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Passar apenas o eixo para o Seaborn
    sns.barplot(x='year', y='value', data=chelsea_valuation_in_year, palette='Blues_d', ax=ax)
    
    # Adicionar título e rótulos
    ax.set_title("Chelsea's Valuation Over Years (2015-2023)", fontsize=14, fontweight='bold')
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Value (€ Million)", fontsize=12)
    
    plt.show()


def plot_regression_plot_valuation(chelsea_valuation_in_year):
    sns.set_theme(style="whitegrid")
    
    # Criar figura e eixo corretamente
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Gerar gráfico de regressão
    sns.regplot(
        x='year', 
        y='value', 
        data=chelsea_valuation_in_year, 
        scatter_kws={'s': 50}, 
        line_kws={'color': 'red'}, 
        ax=ax
    )
    
    # Configurar título e rótulos
    ax.set_title("Regression Analysis of Chelsea's Valuation (2015-2023)", fontsize=14, fontweight='bold')
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Value (€ Million)", fontsize=12)
    
    plt.show()


def heat_map_title_wins(chelsea_valuation_in_year, chelsea_titles_in_year):
    sns.set_theme(style="whitegrid")

    # Limpar nomes das colunas
    chelsea_titles_in_year.columns = chelsea_titles_in_year.columns.str.strip()
    chelsea_valuation_in_year.columns = chelsea_valuation_in_year.columns.str.strip()

    print(chelsea_titles_in_year.columns)
    print(chelsea_valuation_in_year.columns)


    # Verificar novamente a existência das colunas
    if 'year' not in chelsea_valuation_in_year.columns:
        raise KeyError("A coluna 'year' não está presente na tabela de valuations.")
    if 'year' not in chelsea_titles_in_year.columns:
        raise KeyError("A coluna 'ano' não está presente na tabela de títulos.")

    # Realizar o merge utilizando as colunas específicas
    merged_data = chelsea_valuation_in_year.merge(
        chelsea_titles_in_year,
        left_on='year',
        right_on='year'
    )

    # Converter a coluna did_win_big_title para numérico
    merged_data['did_win_big_title'] = merged_data['did_win_big_title'].astype(int)

    # Calcular a matriz de correlação
    corr_matrix = merged_data[['value', 'did_win_big_title']].corr()

    # Plotar o mapa de calor
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap='coolwarm',
        fmt=".2f",
        linewidths=0.5
    )
    plt.title("Correlation Between Valuation and Title Wins (2015-2023)")
    plt.show()

