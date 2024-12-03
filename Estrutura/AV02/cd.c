#include "cd.h"
#include "grafo_cidades.h"
#include "fila.h"
#include "lista.h"
#include "pilha.h"
#include "dfs.h"
#include "config.h"

// Lista de CDs definidos em main.c
extern int cds[MAX_CDS];

// Função que verifica se a cidade é um CD (destino)
int eh_cd(int cidade_idx)
{
    for (int i = 0; i < MAX_CDS; i++)
    {
        if (cds[i] == cidade_idx)
        {
            return 1; // A cidade é um CD
        }
    }
    return 0; // A cidade não é um CD
}

int encontrar_cd_bfs(const char *cidade_origem,
                     int matriz_adjacencia[MAX_CIDADES][MAX_CIDADES],
                     int num_cidades, Grafo *grafo)
{
    int visitados[MAX_CIDADES] = {0};
    int origem_idx = obter_indice(grafo, cidade_origem);

    if (origem_idx == -1)
    {
        printf("Cidade de origem inválida.\n");
        return -1;
    }

    FilaBFS fila;
    inicializar_fila_bfs(&fila);
    enqueue_bfs(&fila, origem_idx);
    visitados[origem_idx] = 1;

    while (!fila_vazia_bfs(&fila))
    {
        int atual = dequeue_bfs(&fila);

        if (eh_cd(atual))
        {
            return atual;
        }

        for (int i = 0; i < num_cidades; i++)
        {
            if (matriz_adjacencia[atual][i] && !visitados[i])
            {
                enqueue_bfs(&fila, i);
                visitados[i] = 1;
            }
        }
    }

    return -1;
}
