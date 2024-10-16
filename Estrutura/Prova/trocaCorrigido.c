// Tiago Alves - prova 1
#include <stdio.h>
#include <stdlib.h>

typedef struct elemento* Lista;
typedef struct elemento {
    int data;
    struct elemento *prox;
    struct elemento *ant;
} Elem;

int inteiros[10] = {1, 41, 21, 12, 2, 3, 5, 9, 11, 10};

// Funções declaradas antes do uso
Lista* cria_lista();
void libera_lista(Lista* li);
int insere_lista_ordenada(Lista* li, int valor);
void teste(Lista* lista);
void trocaNos(Lista* head, int n);

int main() {
    // criando a lista
    Lista* lista = cria_lista();
    
    // inserindo os inteiros na lista
    for (int i = 0; i < 10; i++) {
        insere_lista_ordenada(lista, inteiros[i]);
    }

    // Testando os nós
    teste(lista);
    return 0;
}

// Função que troca nós
void trocaNos(Lista* head, int n) {
    // Se a lista for vazia
    if (*head == NULL) {
        printf("Lista vazia\n");
        return;
    }

    Elem* curr = *head;
    Elem* ant = NULL;

    // Encontrar nó
    do {
        if (curr->data == n) break;
        ant = curr;
        curr = curr->prox;
    } while (curr != NULL);

    // Se o nó não for encontrado
    if (curr == NULL) {
        printf("Nó %d não encontrado\n", n);
        return;
    }

    // Realizar a troca se houver nó seguinte
    if (curr->prox != NULL) {
        Elem* nextNode = curr->prox;
        if (ant != NULL) ant->prox = nextNode;
        curr->prox = nextNode->prox;
        nextNode->prox = curr;

        // Atualizar o head se necessário
        if (curr == *head) {
            *head = nextNode;
        }
    } else {
        printf("O nó %d já é o último\n", n);
    }
}

// Criar lista
Lista* cria_lista() {
    Lista* li = (Lista*)malloc(sizeof(Lista));
    if (li != NULL) {
        *li = NULL;
    }
    return li;
}

// Libera lista
void libera_lista(Lista* li) {
    if (li != NULL) {
        Elem *no;
        while (*li != NULL) {
            no = *li;
            *li = (*li)->prox;
            free(no);
        }
        free(li);
    }
}

// Inserir de forma ordenada na lista
int insere_lista_ordenada(Lista* li, int valor) {
    if (li == NULL) return 0;

    Elem* no = (Elem*)malloc(sizeof(Elem));
    if (no == NULL) return 0;

    no->data = valor;

    if (*li == NULL) {
        no->prox = NULL;
        no->ant = NULL;
        *li = no;
    } else {
        Elem *ant = NULL, *atual = *li;

        while (atual != NULL && atual->data < valor) {
            ant = atual;
            atual = atual->prox;
        }

        no->prox = atual;
        no->ant = ant;

        if (ant != NULL) {
            ant->prox = no;
        } else {
            *li = no;
        }

        if (atual != NULL) {
            atual->ant = no;
        }
    }
    return 1;
}

// Teste de troca de nós
void teste(Lista* lista) {
    printf("Testando troca de nós\n");

    trocaNos(lista, 10);  // Testa com o último
    trocaNos(lista, 1);   // Testa com o primeiro
    trocaNos(lista, 80);  // Testa com número não existente
}
