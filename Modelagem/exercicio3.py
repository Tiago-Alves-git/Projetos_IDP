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

# Distribuição de Salários por Grau de Instrução:

# Ensino Fundamental: A maioria dos funcionários com ensino fundamental parece ter salários entre 5 a 10 salários mínimos. Isso sugere uma distribuição de salários mais concentrada em faixas salariais mais baixas.
# Ensino Médio: Os funcionários com ensino médio mostram uma faixa de salário mais ampla, embora ainda com uma concentração significativa entre 7.5 e 12.5 salários mínimos.
# Ensino Superior: A distribuição salarial para funcionários com ensino superior é mais dispersa, com alguns alcançando mais de 20 salários mínimos. Isso indica que o grau de instrução está positivamente correlacionado com salários mais altos.

# Comparação com Kernel Density Estimate (KDE):

# O uso do KDE ajuda a visualizar a distribuição suavizada dos dados. 
# Para o ensino superior, a linha KDE é mais dispersa, o que indica uma maior variabilidade nos salários para esse grupo.
#  Já para o ensino fundamental, a curva é mais concentrada, refletindo uma menor variação salarial.