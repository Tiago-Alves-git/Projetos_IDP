import ctypes
import random
import time


# Carregar a biblioteca compilada em C
lib = ctypes.CDLL(r'C:\Users\24101255\OneDrive - Instituto Brasileiro de Ensino, Desenvolvimento e Pesquisa (IDP)\Documentos\Tiago-GitHub\Projetos_IDP\Estrutura\Filas\fila_transplante.dll')

# Definir as funções e estruturas de dados
lib.criaFila.restype = ctypes.POINTER(ctypes.c_void_p)
lib.insereFila.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
lib.removeFila.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
lib.removeFila.restype = ctypes.POINTER(ctypes.c_void_p)

class Transplante:
    CORACAO = 0
    CORNEA = 1
    MEDULA = 2

# Criar as filas de prioridade
fila_coracao = lib.criaFila()
fila_cornea = lib.criaFila()
fila_medula = lib.criaFila()

# Função para simular inserções e remoções
def simula_fila(fila, tipo):
    for _ in range(1000):
        idade = random.randint(1, 100)
        nome = f"Paciente_{idade}".encode('utf-8')
        lib.insereFila(fila, nome, idade, tipo)
        
        # Remover aleatoriamente um paciente
        if random.random() > 0.5:
            removido = lib.removeFila(fila)

# Simulação com as filas
inicio = time.time()
simula_fila(fila_coracao, Transplante.CORACAO)
simula_fila(fila_cornea, Transplante.CORNEA)
simula_fila(fila_medula, Transplante.MEDULA)
fim = time.time()
print("Tempo de execução da Fila: ", fim - inicio)

# Simulação usando listas para comparar desempenho
def simula_lista(lista):
    for _ in range(1000):
        idade = random.randint(1, 100)
        lista.append(idade)
        lista.sort(reverse=True)
        
        # Remover aleatoriamente um paciente
        if random.random() > 0.5 and lista:
            lista.pop(0)

inicio = time.time()
lista_coracao, lista_cornea, lista_medula = [], [], []
simula_lista(lista_coracao)
simula_lista(lista_cornea)
simula_lista(lista_medula)
fim = time.time()
print("Tempo de execução da Lista: ", fim - inicio)
