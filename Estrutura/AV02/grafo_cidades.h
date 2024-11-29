#ifndef GRAFO_CIDADES_H
#define GRAFO_CIDADES_H

#include <stdio.h>
#include <string.h>

#define MAX_CIDADES 27
#define INF 99999

typedef struct {
    char cidades[MAX_CIDADES][50];
    int matriz_adj[MAX_CIDADES][MAX_CIDADES];
    int total_cidades;
} Grafo;

typedef struct {
    int cidade;      // Índice da cidade no grafo
    int distancia;   // Distância da cidade até a origem
} No;

void inicializar_grafo(Grafo *grafo);
int adicionar_cidade(Grafo *grafo, const char *cidade);
int obter_indice(Grafo *grafo, const char *cidade);
void adicionar_aresta(Grafo *grafo, const char *origem, const char *destino, int peso);
void exibir_grafo(Grafo *grafo);
void carregar_distancias(Grafo *grafo);

#endif
