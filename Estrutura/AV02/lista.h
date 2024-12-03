#ifndef LISTA_H
#define LISTA_H

#include "config.h"

// Estrutura para armazenar os dados de um órgão
typedef struct EntradaLista {
    char orgao[50];
    char cidade[50];
    char status[50];
} EntradaLista;

// Estrutura que representa a lista global
typedef struct ListaGlobal {
    EntradaLista lista[MAX_CIDADES * 10]; // Tamanho máximo da lista
    int total; // Total de elementos na lista
} ListaGlobal;

// Funções de operação na lista global
void inicializar_lista_global(ListaGlobal *lista_global);
void adicionar_na_lista_global(ListaGlobal *lista_global, const char *orgao, const char *cidade, const char *status);
void atualizar_status(ListaGlobal *lista_global, const char *orgao, const char *novo_status);

#endif  // LISTA_H
