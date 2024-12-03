#include "fila.h"
#include <string.h>
#include <stdio.h>
#include "config.h"


// Inicializa a fila
void inicializar_fila(Fila *fila) {
    fila->frente = fila->tras = fila->tamanho = 0;
}

// Enqueue: adiciona um órgão na fila
void enqueue(Fila *fila, const char *orgao) {
    if (fila->tamanho < MAX_CIDADES) {
        strcpy(fila->orgaos[fila->tras], orgao);
        fila->tras = (fila->tras + 1) % MAX_CIDADES;  // Circular
        fila->tamanho++;
    } else {
        printf("Fila cheia! Não é possível adicionar mais elementos.\n");
    }
}

// Dequeue: remove um órgão da fila
char* dequeue(Fila *fila) {
    if (fila->tamanho > 0) {
        char *orgao = fila->orgaos[fila->frente];
        fila->frente = (fila->frente + 1) % MAX_CIDADES;  // Circular
        fila->tamanho--;
        return orgao;
    }
    return NULL;  // Fila vazia
}

// Verifica se a fila está vazia
int fila_vazia(Fila *fila) {
    return fila->tamanho == 0;
}
