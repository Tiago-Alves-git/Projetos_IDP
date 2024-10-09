#define AP4HNOTAS_H
#define AP4HNOTAS_H


struct aluno {
    int matricula;
    char nome[30];
    float ap1, ap2, ap3, ap4, np, nf;
};
typedef struct elemento* Lista;

typedef struct elemento {
    struct aluno dados;
    struct elemento *prox;
    struct elemento *ant;
}Elem;


Lista* cria_lista();
void libera_lista(Lista* li);
int insere_lista_ordenada(Lista* li, struct aluno al);
void combinar_listas(Lista* lista1, Lista* lista2, Lista* lista_combinada);
void inverter_lista(Lista* li);
void consultar_lista(Lista* li);
float calcular_nota_final(struct aluno al);