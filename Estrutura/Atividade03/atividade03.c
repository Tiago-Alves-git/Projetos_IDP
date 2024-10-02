#include <stdio.h>
#include <stdlib.h>

typedef struct aluno {
    int matricula;
    char nome[30];
    float ap1, ap2, ap3, ap4, np, av; // Nota final
} Aluno;

typedef struct no {
    Aluno aluno;
    struct no *prox;
} No;

// Função para criar um novo nó
No* criarNo(Aluno aluno) {
    No* novoNo = (No*) malloc(sizeof(No));
    novoNo->aluno = aluno;
    novoNo->prox = NULL;
    return novoNo;
}

// Função para inserir um nó em ordem decrescente pela nota final
void inserirOrdenado(No** lista, No* novoNo) {  
    No* aux = *lista;
    No* ant = NULL;

    while (aux != NULL && aux->aluno.av > novoNo->aluno.av) {
        ant = aux;
        aux = aux->prox;
    }

    novoNo->prox = aux;
    if (ant == NULL) {
        *lista = novoNo;
    } else {
        ant->prox = novoNo;
    }
}

// Função para imprimir a lista
void imprimirLista(No* lista) {
    while (lista != NULL) {
        printf("Matrícula: %d, Nome: %s, Nota Final: %.2f\n",
               lista->aluno.matricula, lista->aluno.nome, lista->aluno.av);
        lista = lista->prox;
    }
}

int main() {
    struct aluno estrutura_de_dados[10] = {{16350,"Joao",5.0,5.0,5.5,3.5,4.5,0.0},
{17890,"Ricardo",7.0,8.0,6.2,4.3,5.8,0.0},
{16350,"Bianca",1.0,1.1,2.2,2.7,4.1,0.0},
{16350,"Jose",1.0,1.1,2.5,2.9,3.1,0.0},
{11234,"Marcelo",2.0,7.0,2.5,2.9,4.6,0.0},
{17890,"Carla",7.0,2.3,2.4,3.6,4.3,0.0},
{17823,"Fabiano",1.0,1.7,2.8,3.0,3.1,0.0},
{15212,"Ana",8.0,1.6,2.9,3.1,3.5,0.0},
{15542,"Joaquim",5.0,8.6,9.9,8.1,6.5,0.0},
{13452,"Gabriel",8.0,6.4,9.5,7.5,5.7,0.0}};
struct aluno fabrica_de_projetos2[10] = {{16340,"Fábio",8.0,9.0,7.5,5.5,9.5,0.0},
{17390,"Rafael",9.0,8.0,8.5,7.5,5.0,0.0},
{12350,"Luana",8.0,9.1,8.2,7.7,6.5,0.0},
{15350,"Carlos",5.0,7.1,8.5,9.9,8.1,0.0},
{12244,"Maria",8.0,7.0,8.5,9.9,8.5,0.0},
{14560,"Luiza",9.0,6.5,7.5,8.5,7.5,0.0},
{12523,"Roberto",8.0,7.7,8.8,8.0,6.1,0.0},
{15514,"Tiago",9.0,8.0,9.9,8.1,7.5,0.0},
{13542,"Humberto",8.0,6.0,8.9,7.1,8.5,0.0},
{16432,"Samuel",6.0,6.0,9.5,8.5,7.0,0.0}};

    // Criar as listas encadeadas
    No* listaED = NULL;
    No* listaFP = NULL;

    // Inserir os alunos nas listas, ordenando pela nota final
    for (int i = 0; i < 10; i++) {
        No* novoNo = criarNo(estrutura_de_dados[i]);
        inserirOrdenado(&listaED, novoNo);

        novoNo = criarNo(fabrica_de_projetos2[i]);
        inserirOrdenado(&listaFP, novoNo);
    }

    // Imprimir as listas
    printf("Lista da disciplina Estrutura de Dados:\n");
    imprimirLista(listaED);

    printf("\nLista da disciplina Fábrica de Projetos 2:\n");
    imprimirLista(listaFP);

    // Liberar a memória alocada (não implementado neste exemplo)

    return 0;
}