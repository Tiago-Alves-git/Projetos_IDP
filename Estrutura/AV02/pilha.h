#ifndef PILHA_H
#define PILHA_H

#include "config.h"

// Estrutura para a pilha
typedef struct Pilha {
    char orgaos[MAX_CIDADES][50];  // Array para armazenar os órgãos
    int topo;                      // Índice do topo
} Pilha;

// Funções para manipular a pilha
void inicializar_pilha(Pilha *pilha);
int pilha_vazia(Pilha *pilha);
void push(Pilha *pilha, const char *orgao);
char* pop(Pilha *pilha);

#endif  // PILHA_H
