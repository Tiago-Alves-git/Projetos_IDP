#include "fila.h"
#include "lista.h"
#include "pilha.h"
#include "grafo_cidades.h"
#include "dfs.h"
#include "config.h"
#include "grafo_cidades.h"
#include "cd.h"

void inicializar_pilha_dfs(PilhaDFS *pilha) {
    pilha->topo = -1;
}

void push_dfs(PilhaDFS *pilha, int valor) {
    if (pilha->topo < MAX_CIDADES - 1) {
        pilha->elementos[++(pilha->topo)] = valor;
    }
}

int pop_dfs(PilhaDFS *pilha) {
    if (pilha->topo >= 0) {
        return pilha->elementos[(pilha->topo)--];
    }
    return -1;
}

int pilha_vazia_dfs(PilhaDFS *pilha) {
    return pilha->topo == -1;
}

void inicializar_fila_bfs(FilaBFS *fila) {
    fila->frente = fila->tras = 0;
}

void enqueue_bfs(FilaBFS *fila, int valor) {
    if ((fila->tras + 1) % MAX_CIDADES != fila->frente) {
        fila->elementos[fila->tras] = valor;
        fila->tras = (fila->tras + 1) % MAX_CIDADES;
    }
}

int dequeue_bfs(FilaBFS *fila) {
    if (fila->frente != fila->tras) {
        int valor = fila->elementos[fila->frente];
        fila->frente = (fila->frente + 1) % MAX_CIDADES;
        return valor;
    }
    return -1;
}

int fila_vazia_bfs(FilaBFS *fila) {
    return fila->frente == fila->tras;
}

int dfs(int cidade_atual, int matriz_adj[MAX_CIDADES][MAX_CIDADES], int visitado[MAX_CIDADES], int destino) {
    visitado[cidade_atual] = 1;  // Marca a cidade como visitada
    if (cidade_atual == destino) {
        return cidade_atual;  // Encontrou o destino
    }

    for (int i = 0; i < MAX_CIDADES; i++) {
        if (matriz_adj[cidade_atual][i] != INF && !visitado[i]) {
            int resultado = dfs(i, matriz_adj, visitado, destino);
            if (resultado != -1) {
                return resultado;
            }
        }
    }
    return -1;
}

int encontrar_cd_dfs(const char *cidade_origem, 
                     int matriz_adjacencia[MAX_CIDADES][MAX_CIDADES], 
                     const char *cidade_destino, Grafo *grafo) {
    // Usando obter_indice para pegar os índices das cidades
    int cidade_origem_idx = obter_indice(grafo, cidade_origem);
    int cidade_destino_idx = obter_indice(grafo, cidade_destino);

    // Verificar se as cidades foram encontradas
    if (cidade_origem_idx == -1 || cidade_destino_idx == -1) {
        printf("Cidade não encontrada.\n");
        return -1; // Ou outro valor de erro adequado
    }

    int visitado[MAX_CIDADES] = {0};
    return dfs(cidade_origem_idx, matriz_adjacencia, visitado, cidade_destino_idx);
}


int encontrar_cd_bfs(const char *cidade_origem,
                     int matriz_adjacencia[MAX_CIDADES][MAX_CIDADES],
                     Grafo *grafo) {
    int visitados[MAX_CIDADES] = {0};
    int origem_idx = obter_indice(grafo, cidade_origem);

    if (origem_idx == -1) {
        printf("Cidade de origem inválida.\n");
        return -1;
    }

    FilaBFS fila;
    inicializar_fila_bfs(&fila);
    enqueue_bfs(&fila, origem_idx);
    visitados[origem_idx] = 1;

    while (!fila_vazia_bfs(&fila)) {
        int atual = dequeue_bfs(&fila);

        if (eh_cd(atual)) {
            return atual;
        }

        for (int i = 0; i < grafo->total_cidades; i++) {
            if (matriz_adjacencia[atual][i] && !visitados[i]) {
                enqueue_bfs(&fila, i);
                visitados[i] = 1;
            }
        }
    }

    return -1;
}
