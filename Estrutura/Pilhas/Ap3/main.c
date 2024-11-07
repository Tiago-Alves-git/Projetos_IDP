#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 32 // Tamanho máximo da pilha

typedef struct {
    char itens[MAX];
    int topo;
} Pilha;

// Funções da pilha
void inicializaPilha(Pilha *p) {
    p->topo = -1;
}

int pilhaVazia(Pilha *p) {
    return p->topo == -1;
}

int pilhaCheia(Pilha *p) {
    return p->topo == MAX - 1;
}

void empilha(Pilha *p, char valor) {
    if (pilhaCheia(p)) {
        printf("Erro: pilha cheia!\n");
        return;
    }
    p->itens[++(p->topo)] = valor;
}

char desempilha(Pilha *p) {
    if (pilhaVazia(p)) {
        printf("Erro: pilha vazia!\n");
        return -1;
    }
    return p->itens[(p->topo)--];
}

void converteParaBase(int numero, int base) {
    Pilha pilha;
    inicializaPilha(&pilha);
    char simbolos[] = "0123456789ABCDEF";

    while (numero > 0) {
        int resto = numero % base;
        empilha(&pilha, simbolos[resto]);
        numero /= base;
    }

    printf("Resultado: ");
    while (!pilhaVazia(&pilha)) {
        printf("%c", desempilha(&pilha));
    }
    printf("\n");
}

int main() {
    int opcao, numero;

    printf("Conversão de bases numéricas usando pilha:\n");
    printf("1. Decimal para Binário\n");
    printf("2. Decimal para Octal\n");
    printf("3. Decimal para Hexadecimal\n");
    printf("Escolha uma opção: ");
    scanf("%d", &opcao);

    printf("Digite o número decimal: ");
    scanf("%d", &numero);

    switch (opcao) {
        case 1:
            printf("Convertendo para Binário...\n");
            converteParaBase(numero, 2);
            break;
        case 2:
            printf("Convertendo para Octal...\n");
            converteParaBase(numero, 8);
            break;
        case 3:
            printf("Convertendo para Hexadecimal...\n");
            converteParaBase(numero, 16);
            break;
        default:
            printf("Opção inválida!\n");
    }

    return 0;
}
