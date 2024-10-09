// Tiago Alves - prova 1
#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Criando um nó com o valor 10
    struct Node *head = createNode(10);

    // Imprimindo o valor do nó
    printf("Valor do nó: %d\n", head->data);

    return 0;
}

struct Node
{
    int data;
    struct Node *ant;
    struct Node *prox;
};

struct Node *createNode(int data)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->prox = newNode; // O nó aponta para si mesmo inicialmente
    return newNode;
}

int trocaNós(struct Node **head, int n)
{
    // Se a lista for vazia
    if (head == NULL)
        return;

    struct Node *ant = NULL, *curr = *head;

    // Encontrar nó
    do
    {
        ant = curr;
        curr = curr->prox;
    } while (curr->data != n && curr != *head);

    // Se o nó não for encontrado
    if (curr->data != n)
    {
        printf("Nó não encontrado");
        return;
    }

    // Se o nó é o ultimo, trocar com o primeiro
    if (curr->prox == *head)
    {
        struct Node *nextNode = *head;
        ant->prox = nextNode;
        curr->prox = nextNode->prox;
        return;
    }

    // Realizar a troca normalmente caso tudo certo
    struct Node *nextNode = curr->prox;
    ant->prox = nextNode;
    curr->prox = nextNode->prox;
    nextNode->prox = curr;

    // Se o nó trocado era o primeiro, atualizar o head
    if (curr == *head)
    {
        *head = nextNode;
    }
}

// Se n existir, trocar com o proximo elemento da lista.
// Levar em conta se o elemento for o primeiro ou o ultimo da lista

// Teste

int teste()
{
    typedef struct elemento *Lista;
    typedef struct elemento
    {
        int dados;
        struct elemento *prox;
        struct elemento *ant;
    } Elem;

    struct elemento inteiros[10] = {{1}, {41}, {21}, {12}, {2}, {3}, {5}, {9}, {11}, {10}};

    Lista* *newInteiros = (Lista*)malloc(sizeof(Lista));

// testa com o numero sendo o ultimo
    printf(trocaNós(&newInteiros,10));
    // testa com o primeiro
    printf(trocaNós(&newInteiros, 1));
    // testa caso não exista
    printf(trocaNós(&newInteiros, 80));
}