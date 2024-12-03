#include "lista.h"
#include <stdio.h>
#include <string.h>

// Inicializa a lista global
void inicializar_lista_global(ListaGlobal *lista_global) {
    lista_global->total = 0;
}

// Adiciona um órgão na lista global
void adicionar_na_lista_global(ListaGlobal *lista_global, const char *orgao, const char *cidade, const char *status) {
    if (lista_global->total < MAX_CIDADES * 10) {
        strcpy(lista_global->lista[lista_global->total].orgao, orgao);
        strcpy(lista_global->lista[lista_global->total].cidade, cidade);
        strcpy(lista_global->lista[lista_global->total].status, status);
        lista_global->total++;
    } else {
        printf("Lista global cheia! Não é possível adicionar mais órgãos.\n");
    }
}

// Atualiza o status de um órgão na lista global
void atualizar_status(ListaGlobal *lista_global, const char *orgao, const char *novo_status) {
    int encontrado = 0;
    for (int i = 0; i < lista_global->total; i++) {
        if (strcmp(lista_global->lista[i].orgao, orgao) == 0) {
            strcpy(lista_global->lista[i].status, novo_status);
            encontrado = 1;
            break;
        }
    }
    if (!encontrado) {
        printf("Órgão não encontrado na lista global.\n");
    }
}
