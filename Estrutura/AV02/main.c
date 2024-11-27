#include <grafo_cidades.c>

int main() {
    Grafo grafo;
    inicializar_grafo(&grafo);
    carregar_distancias(&grafo);
    exibir_grafo(&grafo);

    return 0;
}
