import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Carrega os dados do arquivo CSV
dados = pd.read_csv('TabelaSalarial.csv')
dados.head()
dados.describe()

# Identifica as colunas categóricas e numéricas
dados_numericos = dados.select_dtypes(include=['float64', 'int64'])
dados_categoricos = dados.select_dtypes(exclude=['float64', 'int64'])

sns.histplot(dados, x="Salario (x Sal Min)", hue="Grau de Instrução", multiple="stack")
plt.suptitle('Histogramas das Variáveis Salario e Instrução', fontsize=16)
plt.show()

sns.histplot(dados, x = "Salario (x Sal Min)", kde = True, hue = "Grau de Instrução")
plt.suptitle('Histogramas das Variáveis Salario e Instrução com HUE ativada', fontsize=16)
plt.show()


# Não tive muita criatividade em 1 dia para pensar em uma analise diferente das que foram apresentadas em sala. Então fiz essa simples
# Usando tabelas e gráficos de dados de Intrução e Salario, percebemos que normalmente funcionarios que apresentam ensinos superiores tendem a ganhar mais.