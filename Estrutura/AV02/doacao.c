#include "fila.h"
#include "lista.h"
#include "pilha.h"
#include "grafo_cidades.h"
#include "dfs.h"
#include "config.h"
#include "cd.h"

void adicionar_doacao(const char *cidade_origem, const char *orgao,
                      Pilha pilhas[], Fila filas[], ListaGlobal *lista_global, Grafo *grafo)
{
    // Obter o índice da cidade de origem
    int origem_idx = obter_indice(grafo, cidade_origem);
    if (origem_idx == -1)
    {
        printf("Cidade de origem invalida.\n");
        return;
    }

    // Encontrar o CD mais próximo usando Dijkstra
    int cd_mais_proximo = -1;
    int menor_distancia = INF;

    for (int i = 0; i < grafo->total_cidades; i++)
    {
        if (eh_cd(i))
        { // Verifique se é um CD (Centro de Doação)
            int distancia = dijkstra(grafo, origem_idx, i);

            if (distancia != INF && distancia < menor_distancia)
            {
                menor_distancia = distancia;
                cd_mais_proximo = i;
            }
        }
    }

    if (cd_mais_proximo == -1)
    {
        printf("Nao foi possível encontrar um CD valido ou acessivel.\n");
        return;
    }

    char tipo[50];
    printf("Digite o tipo de órgão (CORACAO, MEDULA, CORNEA): ");
    scanf("%49[^\n]", tipo);
    tipo[strcspn(tipo, "\n")] = '\0';       // Limpa a string de caracteres extras
    printf("Entrada recebida: %s\n", tipo); // Debug da entrada

    // Adicionar o órgão à estrutura correta
    if (strcmp(orgao, "CORACAO") == 0)
    {
        push(&pilhas[cd_mais_proximo], orgao);
    }
    else if (strcmp(orgao, "MEDULA") == 0 || strcmp(orgao, "CORNEA") == 0)
    {
        enqueue(&filas[cd_mais_proximo], orgao);
    }
    else
    {
        printf("Tipo de orgao invalido!\n");
        return;
    }

    adicionar_na_lista_global(lista_global, orgao, cidade_origem, "Em espera para transplante");
    printf("Doacao adicionada com sucesso! CD mais proximo: %s. Distancia: %d km\n",
           grafo->cidades[cd_mais_proximo], menor_distancia);
}

void processar_doacao(const char *orgao, Pilha pilhas[], Fila filas[],
                      ListaGlobal *lista_global)
{
    printf("Iniciando processamento da doação para o orgao: %s\n", orgao);

    for (int i = 0; i < MAX_CDS; i++)
    {
        char *orgao_transplantado = NULL;

        if (strcmp(orgao, "CORACAO") == 0)
        {
            if (!pilha_vazia(&pilhas[i]))
            {
                orgao_transplantado = pop(&pilhas[i]);
                printf("CORACAO retirado da pilha do CD %d.\n", i + 1);
            }
        }
        else
        {
            if (!fila_vazia(&filas[i]))
            {
                orgao_transplantado = dequeue(&filas[i]);
                printf("%s retirado da fila do CD %d.\n", orgao, i + 1);
            }
        }

        if (orgao_transplantado)
        {
            atualizar_status(lista_global, orgao_transplantado, "Orgao transplantado");
            printf("Orgao %s transplantado com sucesso do CD %d!\n", orgao, i + 1);
            return;
        }
    }

    printf("Nenhum orgao disponivel para transplante.\n");
}
