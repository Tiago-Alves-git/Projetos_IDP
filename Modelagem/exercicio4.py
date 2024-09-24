import numpy as np
import matplotlib.pyplot as plt

# Definir o número de simulações
num_simulacoes = 10000

# Simulando jogadas para 1 dado de 12 faces
jogadas_d12 = np.random.randint(1, 13, num_simulacoes)

# Simulando jogadas para 2 dados de 6 faces
jogadas_d6_1 = np.random.randint(1, 7, num_simulacoes)
jogadas_d6_2 = np.random.randint(1, 7, num_simulacoes)
jogadas_2d6 = jogadas_d6_1 + jogadas_d6_2

# Calculando o valor esperado para cada opção
valor_esperado_d12 = np.mean(jogadas_d12)
valor_esperado_2d6 = np.mean(jogadas_2d6)

# Plotando os gráficos de barras
plt.figure(figsize=(12, 6))

# Gráfico para 1 dado de 12 faces
plt.subplot(1, 2, 1)
plt.hist(jogadas_d12, bins=np.arange(1, 14) - 0.5, edgecolor='black', color='skyblue', rwidth=0.8)
plt.xticks(np.arange(1, 13))
plt.title(f'1 Dado de 12 Faces (Valor Esperado = {valor_esperado_d12:.2f})')
plt.xlabel('Resultado')
plt.ylabel('Frequência')

# Gráfico para 2 dados de 6 faces
plt.subplot(1, 2, 2)
plt.hist(jogadas_2d6, bins=np.arange(2, 13) - 0.5, edgecolor='black', color='lightgreen', rwidth=0.8)
plt.xticks(np.arange(2, 13))
plt.title(f'2 Dados de 6 Faces (Valor Esperado = {valor_esperado_2d6:.2f})')
plt.xlabel('Resultado')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()


# #Simulacoes
# num_simulacoes = 10000


# # Joga dado 1

# # Joga dado 2

# # Soma dados

# # Joga dado 3
