#include <stdio.h>
#include <stdlib.h>
#include "structs.h"

// Função para criar uma lista 
Lista* cria_lista() {
    Lista* li = (Lista*)malloc(sizeof(Lista));  // aloca memória para o ponteiro da lista
    if (li != NULL) {
        *li = NULL;  // inicializa a lista como vazia
    }
    return li;  // retorna o ponteiro da lista
}


// função para calcular a média do  aluno
float calcular_nota_final(struct aluno al) {
return al.np * 0.6 + ((al.ap1 + al.ap2 + al.ap3 + al.ap4) / 4) * 0.4;  // esse aqui dispensa comentários
}

// Função para liberar a lista 
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
int insere_lista_ordenada(Lista* li, struct aluno al) {
    if (li == NULL) return 0;  // verifica se a lista foi criada corretamente

    Elem *no = (Elem*)malloc(sizeof(Elem));  // aloca memoria pra um novo nó
    if (no == NULL) return 0;  // verifica se a alocação funcionou

    no->dados = al;  // atribui os dados do aluno ao novo nó
    float nota_aluno = calcular_nota_final(al);  // calcula a nota final do aluno

    if (*li == NULL) {  
        no->prox = NULL;  // como é o único nó, o próximo é NULL
        no->ant = NULL;  // como é o único nó, o anterior também é NULL
        *li = no;  // o novo nó se torna o primeiro nó da lista
        return 1;  // retorna sucesso
    } else {
        Elem *ant = NULL, *atual = *li;  // ponteiro aterior e atual

        // percorre a lista para encontrar a posição correta
        while (atual != NULL && nota_aluno < calcular_nota_final(atual->dados)) {
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


// Combinar as listas ordenadamente
void combinar_listas(Lista* lista1, Lista* lista2, Lista* lista_combinada) {
    Elem* no = *lista1;  // aponta para o primeiro nó da primeira lista
    while (no != NULL) {  // percorre a primeira lista
        insere_lista_ordenada(lista_combinada, no->dados); //insere na lista combinada 
        no = no->prox;  // avança para o próximo nó
    }
    
    no = *lista2;  // aponta para o primeiro nó da segunda lista
    while (no != NULL) {  // percorre a segunda lista
        insere_lista_ordenada(lista_combinada, no->dados); //  insere na lista combinada
        no = no->prox;  // avança para o próximo nó
    }
}


// Inverter a lista 
void inverter_lista(Lista* li) {
    if (li == NULL || *li == NULL) return ;  // verifica se a lista está vazia

    Elem* atual = *li; // 'atual' agora aponta para o primeiro nó da lista
    Elem* temp = NULL; // declara 'temp' como um ponteiro nulo

    while (atual != NULL) {
        temp = atual->ant;  // Armazena o anterior
        atual->ant = atual->prox;  // Inverte anterior para próximo
        atual->prox = temp;  // Inverte próximo para anterior
        atual = atual->ant;  // Avança para o próximo nó (invertido)
    }

    if (temp != NULL) {
        *li = temp->ant;  // Ajusta o início da lista
    }
}

// Consultar a lista
void consultar_lista(Lista* li) {
    if (li == NULL || *li == NULL) {// verifica se a lista está vazia
        printf("Lista vazia!\n");  
        return ;
    }
    
    Elem* no = *li; // 'no' agora aponta para o primeiro nó da lista
    while (no != NULL) {
        printf("Matrícula: %d, Nome: %s, Nota Final: %.2f\n", 
                no->dados.matricula, no->dados.nome, calcular_nota_final(no->dados));  // printa os dados do aluno
        no = no->prox;  // Avança para o próximo nó
    }
}