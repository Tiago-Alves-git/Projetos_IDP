#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "grafo_cidades.h"
#include "pilha.h"
#include "fila.h"
#include "lista.h"
#include "doacao.c"
#include "dfs.h"
#include "relatorio.c"
#include "config.h"
#include "cd.h"

int cds[MAX_CDS];

// Função para exibir o menu de opções
void menu()
{
    printf("\n=== Sistema de Gerenciamento de Doações ===\n");
    printf("1. Adicionar Doação\n");
    printf("2. Processar Doação\n");
    printf("3. Exibir Estado das Estruturas\n");
    printf("4. Sair\n");
    printf("Escolha uma opção: ");
}

int main()
{
    Grafo grafo;
    inicializar_grafo(&grafo);
    carregar_distancias(&grafo);

    cds[0] = obter_indice(&grafo, "Brasília");
    cds[1] = obter_indice(&grafo, "São Paulo");
    cds[2] = obter_indice(&grafo, "Fortaleza");

    // Inicialização das estruturas
    ListaGlobal lista_global;
    inicializar_lista_global(&lista_global);

    Pilha pilhas[MAX_CDS];
    Fila filas[MAX_CDS];
    for (int i = 0; i < MAX_CDS; i++)
    {
        inicializar_pilha(&pilhas[i]);
        inicializar_fila(&filas[i]);
    }

    int opcao;
    do
    {
        menu();
        scanf("%d", &opcao);

        switch (opcao)
        {
        case 1:
        {
            char origem[50], tipo[10];
            printf("Digite a capital de origem: ");
            scanf("%s", origem);
            printf("Digite o tipo de órgão (CORAÇÃO, MEDULA, CÓRNEA): ");
            scanf("%s", tipo);

            adicionar_doacao(origem, tipo, pilhas, filas, &lista_global, grafo.matriz_adj, &grafo);
            break;
        }

        case 2:
        {
            char tipo[10];
            printf("Digite o tipo de órgão a processar (CORAÇÃO, MEDULA, CÓRNEA): ");
            scanf("%s", tipo);

            processar_doacao(tipo, pilhas, filas, &lista_global);
            break;
        }

        case 3:
        {
            printf("\n=== Estado das Estruturas ===\n");

            imprimir_relatorio(pilhas, filas, &lista_global);

            break;
        }

        case 4:
            printf("Saindo...\n");
            break;

        default:
            printf("Opção inválida!\n");
        }
    } while (opcao != 4);

    return 0;
}
