#ifndef CD_H
#define CD_H

#include "grafo_cidades.h"

// Função que verifica se a cidade é um CD
int eh_cd(int cidade_idx);

// Função para encontrar a cidade de destino usando BFS
int encontrar_cd_bfs(const char *cidade_origem, 
                     int matriz_adjacencia[MAX_CIDADES][MAX_CIDADES], 
                     const char *cidades[], int num_cidades, Grafo* grafo);

#endif // CD_H
