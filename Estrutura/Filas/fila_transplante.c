#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CORACAO 0
#define CORNEA 1
#define MEDULA 2

typedef struct Paciente {
    char nome[50];
    int idade;
    int tipoTransplante;
    struct Paciente* prox;
} Paciente;

typedef struct Fila {
    Paciente* frente;
    Paciente* tras;
} Fila;

Fila* criaFila() {
    Fila* f = (Fila*)malloc(sizeof(Fila));
    f->frente = f->tras = NULL;
    return f;
}

void insereFila(Fila* f, char nome[], int idade, int tipoTransplante) {
    Paciente* novo = (Paciente*)malloc(sizeof(Paciente));
    strcpy(novo->nome, nome);
    novo->idade = idade;
    novo->tipoTransplante = tipoTransplante;
    novo->prox = NULL;

    if (!f->frente || f->frente->idade < idade) {
        novo->prox = f->frente;
        f->frente = novo;
        if (!f->tras) f->tras = novo;
    } else {
        Paciente* atual = f->frente;
        while (atual->prox && atual->prox->idade >= idade)
            atual = atual->prox;
        novo->prox = atual->prox;
        atual->prox = novo;
        if (!novo->prox) f->tras = novo;
    }
}

Paciente* removeFila(Fila* f) {
    if (!f->frente) return NULL;
    Paciente* removido = f->frente;
    f->frente = f->frente->prox;
    if (!f->frente) f->tras = NULL;
    return removido;
}

void imprimeFila(Fila* f) {
    Paciente* atual = f->frente;
    while (atual) {
        printf("Nome: %s, Idade: %d, Tipo: %d\n", atual->nome, atual->idade, atual->tipoTransplante);
        atual = atual->prox;
    }
}
