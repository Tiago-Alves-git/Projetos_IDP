#include <stdio.h>
#include <stdlib.h>

// Estrutura de um nó
struct Node {
    int data;
    struct Node *next;
};

// Função para criar um novo nó
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

int main() {
    // Criando um nó com o valor 10
    struct Node* head = createNode(10);

    // Imprimindo o valor do nó
    printf("Valor do nó: %d\n", head->data);

    return 0;
}

#include <stdio.h>
#include <stdlib.h>

// Criando nós e liberando toda a memória da lista

struct Node {
    int data;
    struct Node *next;
};

// Função para criar um novo nó
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Erro ao alocar memória.\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Função para liberar toda a memória alocada para a lista
void freeList(struct Node* head) {
    struct Node* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

int main2() {
    struct Node* head = createNode(10);
    head->next = createNode(20);
    head->next->next = createNode(30);

    // ... usar a lista ...

    freeList(head); // Libera toda a memória da lista

    return 0;
}

// ... (código da estrutura Node e da função createNode)

// Função para inserir um nó no início da lista
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

// Criando uma lista Circular encadeada

struct Node {
    int data;
    struct Node *next;
};

#include <stdio.h>
#include <stdlib.h>

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

void printList(struct Node* head) {
    if (head == NULL) {
        printf("Lista vazia\n");
        return;
    }
    struct Node* temp = head;
    do {
        printf("%d ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("\n");
}

#include <stdio.h>
#include <stdlib.h>

// ... (estruturas e funções anteriores)

int main() {
    struct Node* head = NULL;

    insertAtEnd(&head, 10);
    insertAtEnd(&head, 20);
    insertAtEnd(&head, 30);

    printList(head);

    // Liberar a memória (não abordado neste exemplo simplificado)

    return 0;
}