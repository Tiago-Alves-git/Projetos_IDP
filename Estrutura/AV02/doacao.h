#ifndef DOACAO_H
#define DOACAO_H

#include "fila.h"
#include "lista.h"
#include "pilha.h"
#include "grafo_cidades.h"
#include "dfs.h"
#include "config.h"
#include "cd.h"

void adicionar_doacao(const char *cidade_origem, const char *orgao, 
                      Pilha pilhas[], Fila filas[], ListaGlobal *lista_global, 
                      int matriz_adjacencia[MAX_CIDADES][MAX_CIDADES]);

void processar_doacao(const char *orgao, Pilha pilhas[], Fila filas[], 
                      ListaGlobal *lista_global);

#endif // DOACAO_H
