#ifndef GRAFO_CIDADES_H
#define GRAFO_CIDADES_H

#include <stdio.h>
#include <string.h>
#include "config.h"

// Definição da estrutura Grafo
typedef struct {
    char cidades[MAX_CIDADES][50];           // Nome das cidades
    int matriz_adj[MAX_CIDADES][MAX_CIDADES]; // Matriz de adjacência para as distâncias entre as cidades
    int total_cidades;                       // Contador de cidades adicionadas
} Grafo;

// Definição da estrutura No (usada no algoritmo de Dijkstra)
typedef struct {
    int cidade;      // Índice da cidade no grafo
    int distancia;   // Distância da cidade até a origem
} No;

// Funções do Grafo
void inicializar_grafo(Grafo *grafo);                            // Inicializa o grafo
int adicionar_cidade(Grafo *grafo, const char *cidade);          // Adiciona uma nova cidade ao grafo
int comparar(const void *a, const void *b);                      // Função de comparação usada para ordenação
int obter_indice(Grafo *grafo, const char *cidade);              // Obtém o índice de uma cidade no grafo
void adicionar_aresta(Grafo *grafo, const char *origem, const char *destino, int peso);  // Adiciona uma aresta entre duas cidades
void exibir_grafo(Grafo *grafo);                                  // Exibe o grafo (matriz de adjacência)
void carregar_distancias(Grafo *grafo);                           // Carrega as cidades e distâncias no grafo
void dijkstra(Grafo *grafo, int origem, int destino);             // Executa o algoritmo de Dijkstra para encontrar o caminho mais curto entre duas cidades

#endif
