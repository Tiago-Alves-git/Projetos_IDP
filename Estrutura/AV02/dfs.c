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

int dfs(int cidade_atual, int matriz_adj[MAX_CIDADES][MAX_CIDADES], 
        int visitado[MAX_CIDADES], int destino) {
    visitado[cidade_atual] = 1;
    printf("Visitando cidade: %d\n", cidade_atual);  // Imprime a cidade visitada

    if (cidade_atual == destino) {
        printf("Destino alcançado: %d\n", destino);
        return cidade_atual;
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

    int cidade_origem_idx = obter_indice(grafo, cidade_origem);
    int cidade_destino_idx = obter_indice(grafo, cidade_destino);

    if (cidade_origem_idx == -1 || cidade_destino_idx == -1) {
        printf("Cidade não encontrada.\n");
        return -1;
    }

    int visitado[MAX_CIDADES] = {0};
    int prev[MAX_CIDADES];
    int dist[MAX_CIDADES];
    
    for (int i = 0; i < MAX_CIDADES; i++) {
        prev[i] = -1;  // Inicializa os anteriores como -1
        dist[i] = INF; // Inicializa as distâncias com valor muito alto
    }
    dist[cidade_origem_idx] = 0;

    int resultado = dfs(cidade_origem_idx, matriz_adjacencia, visitado, cidade_destino_idx);

    // Se o caminho foi encontrado, imprime o caminho, a distância e o número de nós
    if (resultado != -1) {
        printf("Menor caminho de %s a %s: ", grafo->cidades[cidade_origem_idx], grafo->cidades[cidade_destino_idx]);
        
        int cidade_atual = cidade_destino_idx;
        int num_nos = 0;
        while (cidade_atual != -1) {
            printf("%s <- ", grafo->cidades[cidade_atual]);
            cidade_atual = prev[cidade_atual];
            num_nos++;
        }
        
        printf("\nDistância total: %d km\n", dist[cidade_destino_idx]);
        printf("Número de nós no caminho: %d\n", num_nos);
    }

    return resultado;
}




int encontrar_cd_bfs(const char *cidade_origem,
                     int matriz_adjacencia[MAX_CIDADES][MAX_CIDADES],
                     Grafo *grafo) {

    int visitados[MAX_CIDADES] = {0};
    int prev[MAX_CIDADES];    // Para armazenar o caminho
    int dist[MAX_CIDADES];    // Para armazenar as distâncias
    int origem_idx = obter_indice(grafo, cidade_origem);

    if (origem_idx == -1) {
        printf("Cidade de origem inválida.\n");
        return -1;
    }

    // Inicializa os vetores
    for (int i = 0; i < MAX_CIDADES; i++) {
        prev[i] = -1; // Nenhuma cidade foi visitada inicialmente
        dist[i] = INF; // Inicializa as distâncias como um valor alto (infinito)
    }
    dist[origem_idx] = 0;  // A distância da cidade de origem para ela mesma é 0

    FilaBFS fila;
    inicializar_fila_bfs(&fila);
    enqueue_bfs(&fila, origem_idx);
    visitados[origem_idx] = 1;

    static int num_visitados = 0;  // Variável para contar o número de grafos visitados

    printf("Iniciando BFS da cidade: %d\n", origem_idx);

    while (!fila_vazia_bfs(&fila)) {
        int atual = dequeue_bfs(&fila);
        num_visitados++;  // Incrementa o número de grafos visitados
        printf("Visitando cidade: %d\n", atual);

        if (eh_cd(atual)) {
            printf("Centro de Doação encontrado: %d\n", atual);
            printf("Número total de grafos visitados (BFS): %d\n", num_visitados);

            // Imprimir o caminho e a distância
            printf("Menor caminho de %s a %s: ", grafo->cidades[origem_idx], grafo->cidades[atual]);
            int cidade_atual = atual;
            int num_nos = 0;

            // Imprime o caminho da origem ao destino
            while (cidade_atual != -1) {
                printf("%s <- ", grafo->cidades[cidade_atual]);
                cidade_atual = prev[cidade_atual];
                num_nos++;
            }

            printf("\nDistância total: %d km\n", dist[atual]);
            printf("Número de nós no caminho: %d\n", num_nos);

            return atual;
        }

        for (int i = 0; i < grafo->total_cidades; i++) {
            if (matriz_adjacencia[atual][i] && !visitados[i]) {
                enqueue_bfs(&fila, i);
                visitados[i] = 1;
                prev[i] = atual;  // Armazena o nó anterior
                dist[i] = dist[atual] + matriz_adjacencia[atual][i];  // Atualiza a distância
            }
        }
    }

    printf("Número total de grafos visitados (BFS): %d\n", num_visitados);

    return -1;
}
