#include "fila.h"
#include "lista.h"
#include "pilha.h"
#include "grafo_cidades.h"
#include "dfs.h"
#include "config.h"

void imprimir_relatorio(Pilha pilhas[], Fila filas[], ListaGlobal *lista_global)
{
    printf("\nRelatório das Estruturas de Dados:\n");

    // Exibir conteúdo das pilhas
    printf("\nPILHAS:\n");
    for (int i = 0; i < MAX_CDS; i++)
    {
        printf("CD %d (Pilha): ", i + 1);
        for (int j = pilhas[i].topo; j >= 0; j--)
        {
            printf("%s ", pilhas[i].orgaos[j]);
        }
        printf("\n");
    }

    // Exibir conteúdo das filas
    printf("\nFILAS:\n");
    for (int i = 0; i < MAX_CDS; i++)
    {
        printf("CD %d (Fila): ", i + 1); // Corrigido para usar i + 1 para imprimir o número correto da cidade
        for (int j = 0; j < filas[i].tamanho; j++)
        {
            int idx = (filas[i].frente + j) % MAX_CIDADES;
            printf("%s ", filas[i].orgaos[idx]);
        }
        printf("\n");
    }

    // Exibir lista global
    printf("\nLISTA GLOBAL:\n");
    for (int i = 0; i < lista_global->total; i++)
    {
        printf("Órgão: %s | Cidade: %s | Status: %s\n",
               lista_global->lista[i].orgao,
               lista_global->lista[i].cidade,
               lista_global->lista[i].status);
    }
}
