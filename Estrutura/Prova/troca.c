// Tiago Alves - prova 1
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Criando um nó com o valor 10
    struct Node* head = createNode(10);

    // Imprimindo o valor do nó
    printf("Valor do nó: %d\n", head->data);

    return 0;
}

struct Node {
    int data;
    struct Node *next;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = newNode; // O nó aponta para si mesmo inicialmente
    return newNode;
}

void insertAtEnd(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        struct Node* temp = *head;
        while (temp->next != *head) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->next = *head;
    }
}

void insertAtBeginning(struct Node** head_ref, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = *head_ref;
    *head_ref = newNode;
}

// Função para remover o primeiro nó da lista
void deleteNode(struct Node** head_ref) {
    if (*head_ref == NULL)
        return;
    struct Node* temp = *head_ref;
    *head_ref = (*head_ref)->next;
    free(temp);
}

int troca(struct Node* li, int n) {
    if (li == NULL)
    return;
}

// Se n existir, trocar com o proximo elemento da lista.
// Levar em conta se o elemento for o primeiro ou o ultimo da lista