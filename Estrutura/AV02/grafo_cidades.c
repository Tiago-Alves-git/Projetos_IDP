#include <stdio.h>
#include <string.h>

#define MAX_CIDADES 27
#define INF 99999

// Estrutura para o Grafo
typedef struct {
    char cidades[MAX_CIDADES][50];
    int matriz_adj[MAX_CIDADES][MAX_CIDADES];
    int total_cidades;
} Grafo;

// Inicializa o grafo com as cidades
void inicializar_grafo(Grafo *grafo) {
    grafo->total_cidades = 0;

    // Inicializa a matriz de adjacência com infinito
    for (int i = 0; i < MAX_CIDADES; i++) {
        for (int j = 0; j < MAX_CIDADES; j++) {
            grafo->matriz_adj[i][j] = (i == j) ? 0 : INF;
        }
    }
}

// Adiciona uma cidade ao grafo
int adicionar_cidade(Grafo *grafo, const char *cidade) {
    strcpy(grafo->cidades[grafo->total_cidades], cidade);
    return grafo->total_cidades++;
}

// Retorna o índice de uma cidade no grafo
int obter_indice(Grafo *grafo, const char *cidade) {
    for (int i = 0; i < grafo->total_cidades; i++) {
        if (strcmp(grafo->cidades[i], cidade) == 0) {
            return i;
        }
    }
    return -1;
}

// Adiciona uma aresta entre duas cidades com peso (distância)
void adicionar_aresta(Grafo *grafo, const char *origem, const char *destino, int peso) {
    int indice_origem = obter_indice(grafo, origem);
    int indice_destino = obter_indice(grafo, destino);
    grafo->matriz_adj[indice_origem][indice_destino] = peso;
    grafo->matriz_adj[indice_destino][indice_origem] = peso; // Grafo não direcionado
}

// Exibe o grafo
void exibir_grafo(Grafo *grafo) {
    printf("Grafo de Capitais Brasileiras (Matriz de Adjacência):\n");
    for (int i = 0; i < grafo->total_cidades; i++) {
        printf("%-15s", grafo->cidades[i]);
        for (int j = 0; j < grafo->total_cidades; j++) {
            if (grafo->matriz_adj[i][j] == INF) {
                printf("INF\t");
            } else {
                printf("%d\t", grafo->matriz_adj[i][j]);
            }
        }
        printf("\n");
    }
}

void carregar_distancias(Grafo *grafo) {
    // Adiciona todas as cidades
    adicionar_cidade(grafo, "Rio Branco");
    adicionar_cidade(grafo, "Manaus");
    adicionar_cidade(grafo, "Porto Velho");
    adicionar_cidade(grafo, "Boa Vista");
    adicionar_cidade(grafo, "Belém");
    adicionar_cidade(grafo, "Macapá");
    adicionar_cidade(grafo, "São Luís");
    adicionar_cidade(grafo, "Fortaleza");
    adicionar_cidade(grafo, "Natal");
    adicionar_cidade(grafo, "João Pessoa");
    adicionar_cidade(grafo, "Recife");
    adicionar_cidade(grafo, "Maceió");
    adicionar_cidade(grafo, "Aracaju");
    adicionar_cidade(grafo, "Salvador");
    adicionar_cidade(grafo, "Brasília");
    adicionar_cidade(grafo, "Palmas");
    adicionar_cidade(grafo, "Teresina");
    adicionar_cidade(grafo, "Goiânia");
    adicionar_cidade(grafo, "Campo Grande");
    adicionar_cidade(grafo, "Cuiabá");
    adicionar_cidade(grafo, "São Paulo");
    adicionar_cidade(grafo, "Belo Horizonte");
    adicionar_cidade(grafo, "Vitória");
    adicionar_cidade(grafo, "Rio de Janeiro");
    adicionar_cidade(grafo, "Curitiba");
    adicionar_cidade(grafo, "Florianópolis");
    adicionar_cidade(grafo, "Porto Alegre");

    // Adiciona as arestas (distâncias reais em km)
    adicionar_aresta(grafo, "Rio Branco", "Manaus", 1448);
    adicionar_aresta(grafo, "Rio Branco", "Porto Velho", 540);
    adicionar_aresta(grafo, "Manaus", "Boa Vista", 785);
    adicionar_aresta(grafo, "Manaus", "Belém", 5294);
    adicionar_aresta(grafo, "Porto Velho", "Cuiabá", 1455);
    adicionar_aresta(grafo, "Boa Vista", "Belém", 4263);
    adicionar_aresta(grafo, "Belém", "São Luís", 806);
    adicionar_aresta(grafo, "São Luís", "Fortaleza", 1077);
    adicionar_aresta(grafo, "Fortaleza", "Natal", 537);
    adicionar_aresta(grafo, "Natal", "João Pessoa", 120);
    adicionar_aresta(grafo, "João Pessoa", "Recife", 118);
    adicionar_aresta(grafo, "Recife", "Maceió", 250);
    adicionar_aresta(grafo, "Maceió", "Aracaju", 294);
    adicionar_aresta(grafo, "Aracaju", "Salvador", 326);
    adicionar_aresta(grafo, "Salvador", "Brasília", 1440);
    adicionar_aresta(grafo, "Brasília", "Goiânia", 209);
    adicionar_aresta(grafo, "Goiânia", "Campo Grande", 935);
    adicionar_aresta(grafo, "Campo Grande", "São Paulo", 1015);
    adicionar_aresta(grafo, "São Paulo", "Rio de Janeiro", 429);
    adicionar_aresta(grafo, "São Paulo", "Curitiba", 408);
    adicionar_aresta(grafo, "Curitiba", "Florianópolis", 300);
    adicionar_aresta(grafo, "Florianópolis", "Porto Alegre", 476);
    adicionar_aresta(grafo, "Belo Horizonte", "Brasília", 716);
    adicionar_aresta(grafo, "Belo Horizonte", "Rio de Janeiro", 434);
    adicionar_aresta(grafo, "Rio de Janeiro", "Vitória", 521);
    adicionar_aresta(grafo, "Vitória", "Belo Horizonte", 524);
}

