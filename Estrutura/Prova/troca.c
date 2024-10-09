// Tiago Alves - prova 1
#include <stdio.h>
#include <stdlib.h>

    typedef struct elemento* Lista;
    typedef struct elemento
    {
        int data;
        struct elemento *prox;
        struct elemento *ant;
    } Elem;

    int inteiros[10] = {{1}, {41}, {21}, {12}, {2}, {3}, {5}, {9}, {11}, {10}};

int main()
{
    // criando a lista
    Lista* lista = cria_lista();
    // inserindo a lista
    for (int i = 0; i < 10; i++)
    {
        insere_lista_ordenada(lista, inteiros[i]);
    }

    teste();
    return 0;
}

int trocaNós(struct elemento **head, int n)
{
    // Se a lista for vazia
    if (head == NULL)
        return;

    struct elemento *ant = NULL, *curr = *head;

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
        struct elemento *nextNode = *head;
        ant->prox = nextNode;
        curr->prox = nextNode->prox;
        return;
    }

    // Realizar a troca normalmente caso tudo certo
    struct elemento *nextNode = curr->prox;
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

    Lista* cria_lista() {
    Lista* li = (Lista*)malloc(sizeof(Lista));  // aloca memória para o ponteiro da lista
    if (li != NULL) {
        *li = NULL;  // inicializa a lista como vazia
    }
    return li;  // retorna o ponteiro da lista
}

void libera_lista(Lista* li) {
    if (li != NULL) {  // verifica se a lista foi criada
        Elem *no;
        while (*li != NULL) { 
            no = *li;  // armazena o nó atual
            *li = (*li)->prox;  // avança para o próximo nó
            free(no);  // libera a memória do nó atual
        }
        free(li);  // libera a memória do ponteiro da lista
    }
}


// Inserir de forma ordenada na lista 
int insere_lista_ordenada(Lista* li, int valor) {
    if (li == NULL) return 0;  // verifica se a lista foi criada corretamente

    Elem *no = (Elem*)malloc(sizeof(Elem));  // aloca memoria pra um novo nó
    if (no == NULL) return 0;  // verifica se a alocação funcionou

    no->data = valor;  // atribui os dados ao novo nó

    if (*li == NULL) {  
        no->prox = NULL;  // como é o único nó, o próximo é NULL
        no->ant = NULL;  // como é o único nó, o anterior também é NULL
        *li = no;  // o novo nó se torna o primeiro nó da lista
        return 1;  // retorna sucesso
    } else {
        Elem *ant = NULL, *atual = *li;  // ponteiro aterior e atual

        // percorre a lista para encontrar a posição correta
        while (atual != NULL) {
            ant = atual;  // o ponteiro que apontava para o anterior aponta pro atual para avançarmos na lista
            atual = atual->prox;  // avança para o próximo nó (agora o anterior aponta pro atual anterior)
        }

        no->prox = atual;  // o novo nó aponta para o atual (próximo na lista)
        no->ant = ant;  // o novo nó aponta para o anterior

        if (ant != NULL) {
            ant->prox = no;  // se não for o primeiro nó, o anterior aponta para o novo nó
        } else {
            *li = no;  // se for o primeiro nó, a cabeça da lista aponta para ele
        }

        if (atual != NULL) {
            atual->ant = no;  // se não for o último nó, o nó atual aponta para o novo nó como anterior
        }
        return 1;  // retorna sucesso
    }
}

// Teste

int teste()
{
    // testa com o numero sendo o ultimo
    // printf(trocaNós(Lista*, 10));
    // // testa com o primeiro
    // printf(trocaNós(elemento*, 1));
    // // testa caso não exista
    // printf(trocaNós(struct elemento*, 80));

    // Era pra chamar essa função e testas os casos, mas não sei o que errei.
}