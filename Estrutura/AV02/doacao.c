#include "fila.h"
#include "lista.h"
#include "pilha.h"
#include "grafo_cidades.h"
#include "dfs.h"
#include "config.h"
#include "cd.h"


void adicionar_doacao(const char *cidade_origem, const char *orgao, 
                      Pilha pilhas[], Fila filas[], ListaGlobal *lista_global, 
                      int matriz_adjacencia[MAX_CIDADES][MAX_CIDADES], Grafo *grafo) {
    // Obter o índice da cidade de origem
    int origem_idx = obter_indice(grafo, cidade_origem);
    if (origem_idx == -1) {
        printf("Cidade de origem inválida.\n");
        return;
    }

    // Declarar o vetor de distâncias
    int dist[MAX_CIDADES];

    // Encontrar o CD mais próximo usando Dijkstra
    int cd_mais_proximo = -1;
    int menor_distancia = INF;
    int destino;

    // Rodar Dijkstra para encontrar o CD mais próximo
    for (int i = 0; i < grafo->total_cidades; i++) {
        if (eh_cd(i)) {  // Verifique se é um CD (Centro de Doação)
            // Rodar Dijkstra de cidade_origem para i (CD)
            destino = dijkstra(grafo, origem_idx, i);

            // Verifique se a distância calculada para o CD é a menor
            if (destino < menor_distancia) {
                menor_distancia = destino;
                cd_mais_proximo = i;
            }
        }
    }

    if (cd_mais_proximo == -1) {
        printf("Não foi possível encontrar um CD válido.\n");
        return;
    }

    if (strcmp(orgao, "CORAÇÃO") == 0) {
        push(&pilhas[cd_mais_proximo], orgao);
    } else if (strcmp(orgao, "MEDULA") == 0 || strcmp(orgao, "CÓRNEA") == 0) {
        enqueue(&filas[cd_mais_proximo], orgao);
    } else {
        printf("Tipo de órgão inválido!\n");
        return;
    }

    adicionar_na_lista_global(lista_global, orgao, cidade_origem, "Em espera para transplante");

    printf("Doação adicionada com sucesso!\n");
}





void processar_doacao(const char *orgao, Pilha pilhas[], Fila filas[], 
                      ListaGlobal *lista_global) {
    printf("Iniciando processamento da doação para o órgão: %s\n", orgao);

    for (int i = 0; i < MAX_CDS; i++) {
        char *orgao_transplantado = NULL;

        if (strcmp(orgao, "CORAÇÃO") == 0) {
            if (!pilha_vazia(&pilhas[i])) {
                orgao_transplantado = pop(&pilhas[i]);
                printf("CORAÇÃO retirado da pilha do CD %d.\n", i + 1);
            }
        } else {
            if (!fila_vazia(&filas[i])) {
                orgao_transplantado = dequeue(&filas[i]);
                printf("%s retirado da fila do CD %d.\n", orgao, i + 1);
            }
        }

        if (orgao_transplantado) {
            atualizar_status(lista_global, orgao_transplantado, "Órgão transplantado");
            printf("Órgão %s transplantado com sucesso do CD %d!\n", orgao, i + 1);
            return;
        }
    }

    printf("Nenhum órgão disponível para transplante.\n");
}

