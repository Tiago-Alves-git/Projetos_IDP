#include "pilha.h"
#include <stdio.h>
#include <string.h>

// Inicializa a pilha
void inicializar_pilha(Pilha *pilha) {
    pilha->topo = -1;  // A pilha começa vazia
}

// Verifica se a pilha está vazia
int pilha_vazia(Pilha *pilha) {
    return pilha->topo == -1;  // Retorna 1 se vazia, 0 caso contrário
}

// Adiciona um órgão no topo da pilha
void push(Pilha *pilha, const char *orgao) {
    if (pilha->topo < MAX_CIDADES - 1) {
        strcpy(pilha->orgaos[++pilha->topo], orgao);  // Incrementa o topo e adiciona o órgão
    } else {
        printf("Pilha cheia! Não é possível adicionar mais órgãos.\n");
    }
}

// Remove o órgão do topo da pilha
char* pop(Pilha *pilha) {
    if (!pilha_vazia(pilha)) {
        return pilha->orgaos[pilha->topo--];  // Retorna o órgão e decrementa o topo
    }
    return NULL;  // Retorna NULL se a pilha estiver vazia
}
