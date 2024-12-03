#ifndef FILA_H
#define FILA_H

#include "config.h"

typedef struct Fila {
    char orgaos[MAX_CIDADES][50];  // Armazena os órgãos
    int frente, tras, tamanho;      // Controle da fila
} Fila;

// Funções de operação na fila
void inicializar_fila(Fila *fila);
void enqueue(Fila *fila, const char *orgao);
char* dequeue(Fila *fila);
int fila_vazia(Fila *fila);

#endif  // FILA_H
