#include <stdio.h>
#include <stdlib.h>
#include "ListaSequencial.h" //inclui os Prot�tipos

//Defini��o do tipo lista
struct lista{
    int qtd; // Quantas posicoes ja foram ocupadas?
    struct megasena dados[MAX];
};

// Retorna um ponteiro para a lista com a estrutura inicializada
Lista* cria_lista()
{
    Lista *li;
    li = (Lista*) malloc(sizeof(struct lista));
    if(li != NULL)
        li->qtd = 0;
    return li;
}

void libera_lista(Lista* li)
{
    free(li);
}

int tamanho_lista(Lista* li){
    if(li == NULL)
        return -1;
    else
        return li->qtd;
}

int lista_cheia(Lista* li){
    if(li == NULL)
        return -1;
    return (li->qtd == MAX); // Se igual a MAX returno 1, sen�o returno 0
}

int lista_vazia(Lista* li){
    if(li == NULL)
        return -1;
    return (li->qtd == 0); // Se qtd igual a 0 returno 1, sen�o returno 0
}

void imprime_lista(Lista* li){
    if(li == NULL)
        return;
    int i;
    for(i=0; i< li->qtd; i++){
        printf("Codigo: %d\n",li->dados[i].codigo);
        printf("Concurso: %d\n",li->dados[i].concurso);
        printf("Nome: %s\n",li->dados[i].nome);
        printf("Numeros: %d - %d - %d - %d - %d - %d\n",li->dados[i].n1,
                                   li->dados[i].n2,
                                   li->dados[i].n3,
                                   li->dados[i].n4,
                                   li->dados[i].n5,
                                   li->dados[i].n6);
        printf("-------------------------------\n");
    }
}

int insere_lista_vazia(Lista* li, struct megasena ms)
{
    if(li == NULL)
        return 0;
    li->dados[0] = ms; // Armazena na 1� posicao...
    li->qtd++;
    return 1;
}

int insere_lista_final(Lista* li, struct megasena ms){
    if(li == NULL)
        return 0;
    li->dados[li->qtd] = ms;
    li->qtd++;
    return 1;
}

// � necessario deslocamento
int insere_lista_inicio(Lista* li, struct megasena ms){
    if(li == NULL)
        return 0;
    int i;
    //if (lista_vazia(li))
    for(i=li->qtd-1; i>=0; i--)
        li->dados[i+1] = li->dados[i];
    li->dados[0] = ms;
    li->qtd++;
    return 1;
}

