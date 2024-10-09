import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv('TabelaSalarial.csv')
dados.head()
dados.describe()

# Identifica as colunas categóricas e numéricas
dados_numericos = dados.select_dtypes(include=['float64', 'int64'])
dados_categoricos = dados.select_dtypes(exclude=['float64', 'int64'])

# Exibe as colunas categóricas para verificação
print("Colunas Categóricas:")
print(dados_categoricos.head())

# Medidas de Centralidade e Dispersão para colunas numéricas
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

# Colunas categóricas como variáveis dummy:
dados_dummies = pd.get_dummies(dados_categoricos)
print(dados_dummies.head())

# Configura o estilo dos gráficos
sns.set(style="whitegrid")

# 2) Plotar Histogramas para todas as variáveis numéricas
dados_numericos.hist(bins=10, figsize=(12, 10), layout=(2, 2), edgecolor='black')
plt.suptitle('Histogramas das Variáveis Numéricas', fontsize=16)
plt.show()

# 3) Fazer Boxplot para todas as variáveis numéricas
plt.figure(figsize=(12, 8))
sns.boxplot(data=dados_numericos, orient="h", palette="Set2")
plt.title('Boxplot das Variáveis Numéricas', fontsize=16)
plt.show()

# Plotando Histogramas para as variaves Dummies
dados_dummies.hist(bins=10, figsize=(12,10), layout=(2,2), edgecolor='black')
plt.suptitle('Histogramas das variaveis Dummies', fontsize=16)
plt.show()

# Boxplot para as variaveis Dummies

plt.figure(figsize=(12,8))
