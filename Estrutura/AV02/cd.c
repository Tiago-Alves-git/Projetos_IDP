#include "cd.h"
#include "grafo_cidades.h"
#include "fila.h"
#include "lista.h"
#include "pilha.h"
#include "dfs.h"
#include "config.h"

// Lista de CDs definidos em main.c
extern int cds[MAX_CDS];

// Função que verifica se a cidade é um CD (destino)
int eh_cd(int cidade_idx)
{
    for (int i = 0; i < MAX_CDS; i++)
    {
        if (cds[i] == cidade_idx)
        {
            printf("Cidade verificada: %d\n", cidade_idx);
            return 1; // A cidade é um CD
        }
    }
    return 0; // A cidade não é um CD
}
