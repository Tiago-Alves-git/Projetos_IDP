#ifndef DFS_H
#define DFS_H

#include "grafo_cidades.h"

#define MAX_CIDADES 27

typedef struct PilhaDFS {
    int elementos[MAX_CIDADES];
    int topo;
} PilhaDFS;

typedef struct FilaBFS {
    int elementos[MAX_CIDADES];
    int frente, tras;
} FilaBFS;

// Funções de Pilha para DFS
void inicializar_pilha_dfs(PilhaDFS *pilha);
void push_dfs(PilhaDFS *pilha, int valor);
int pop_dfs(PilhaDFS *pilha);
int pilha_vazia_dfs(PilhaDFS *pilha);

// Funções de Fila para BFS
void inicializar_fila_bfs(FilaBFS *fila);
void enqueue_bfs(FilaBFS *fila, int valor);
int dequeue_bfs(FilaBFS *fila);
int fila_vazia_bfs(FilaBFS *fila);

// Funções para busca
int dfs(int cidade_atual, int matriz_adj[MAX_CIDADES][MAX_CIDADES], int visitado[MAX_CIDADES], int destino);
int encontrar_cd_dfs(const char *cidade_origem, int matriz_adjacencia[MAX_CIDADES][MAX_CIDADES], const char *cidade_destino, Grafo *grafo);
// Função para encontrar a cidade de destino usando BFS
int encontrar_cd_bfs(const char *cidade_origem, 
                     int matriz_adjacencia[MAX_CIDADES][MAX_CIDADES], 
                     Grafo *grafo);


#endif
