#include "grafo_cidades.h"

int main() {
    Grafo grafo;
    inicializar_grafo(&grafo);
    carregar_distancias(&grafo);
    exibir_grafo(&grafo);
    dijkstra(&grafo, obter_indice(&grafo, "Brasília"), obter_indice(&grafo, "São Paulo"));


    return 0;
}
