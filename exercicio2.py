import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega os dados do arquivo CSV
dados = pd.read_csv('TabelaSalarial.csv')
dados.head()
dados.describe()

# Identifica as colunas categóricas e numéricas
dados_numericos = dados.select_dtypes(include=['float64', 'int64'])
dados_categoricos = dados.select_dtypes(exclude=['float64', 'int64'])

# Exibe as colunas categóricas para verificação
print("Colunas Categóricas:")
print(dados_categoricos.head())

# 1) Calcule as medidas de centralidade e dispersão das variáveis;

media = dados_numericos.mean()
mediana = dados_numericos.median()
desvio_padrao = dados_numericos.std()
variancia = dados_numericos.var()
iqr = dados_numericos.quantile(0.75) - dados_numericos.quantile(0.25)
minimo = dados_numericos.min()
maximo = dados_numericos.max()

# Exibe os resultados
print("\nMedidas de Centralidade:")
print(f"Média:\n{media}\n")
print(f"Mediana:\n{mediana}\n")

print("Medidas de Dispersão:")
print(f"Desvio Padrão:\n{desvio_padrao}\n")
print(f"Variância:\n{variancia}\n")
print(f"Intervalo Interquartil (IQR):\n{iqr}\n")
print(f"Valor Mínimo:\n{minimo}\n")
print(f"Valor Máximo:\n{maximo}\n")

# Configura o estilo dos gráficos
sns.set_theme(style="whitegrid")

# 2) Plote histogramas de todas as variáveis;

dados_numericos.hist(bins=10, figsize=(12, 10), layout=(2, 2), edgecolor='black')
plt.suptitle('Histogramas das Variáveis Numéricas', fontsize=16)
plt.show()

# 3) Faça o boxplot de todas as variáveis.

#Variavel numero de filhos por pessoa
plt.figure(figsize=(12, 8))
sns.boxplot(data=dados_numericos['N de Filhos'], orient="h", palette="Set2")
plt.title('Boxplot do numero de pessoas', fontsize=16)
plt.show()

#Variavel salario (x Sal Min)
plt.figure(figsize=(12, 8))
sns.boxplot(data=dados_numericos['Salario (x Sal Min)'], orient="h", palette="Set2")
plt.title('Boxplot do salario (x Sal Min)', fontsize=16)
plt.show()

#Variavel idade das pessoas
plt.figure(figsize=(12, 8))
sns.boxplot(data=dados_numericos['Idade (em anos)'], orient="h", palette="Set2")
plt.title('Boxplot da idade das pessoas', fontsize=16)
plt.show()

# Colunas categóricas como variáveis dummy:
dados_dummies = pd.get_dummies(dados_categoricos)
print(dados_dummies.head())

# Resposta da pergunta
# 4) Escreva uma análise de todas as variáveis, no formato texto corrido, com as informações que vocês geraram nos itens anteriores 
# (Procurem escrever um texto como se estivessem apresentando as informações para uma pessoa leiga)

# Análise

# Salário
# Analisando o salário vemos que a Média é por volta de 11 salários mínimo e a Mediana é 10, podemos dizer que nossos dados são consistentes.

# Idade
# Analisando a idade temos que a Média é por volta dos 35 anos e a Mediana também indicando nossos dados ainda são consistentes e não variam tanto.

# Número de Filhos
# Analisando a quantidade de filhos por pessoa temos que a Média é por volta de 2 e a Mediana também indicando que não possuimos ruidos consideráveis. A variação de quantidade de filhos por volta de 1 nos indica uma variável que tem uma pouca diferença nos seus valores.
