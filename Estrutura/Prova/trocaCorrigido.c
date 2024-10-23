void trocaNos(Lista* head, int n) {
    // Se a lista for vazia
    if (*head == NULL) {
        printf("Lista vazia\n");
        return;
    }

    Elem* curr = *head;
    Elem* ant = NULL;

    // Encontrar nó
    do {
        if (curr->data == n) break;
        ant = curr;
        curr = curr->prox;
    } while (curr != NULL);

    // Se o nó não for encontrado
    if (curr == NULL) {
        printf("Nó %d não encontrado\n", n);
        return;
    }

    // Realizar a troca se houver nó seguinte
    if (curr->prox != NULL) {
        Elem* nextNode = curr->prox;
        if (ant != NULL) ant->prox = nextNode;
        curr->prox = nextNode->prox;
        nextNode->prox = curr;

        // Atualizar o head se necessário
        if (curr == *head) {
            *head = nextNode;
        }
    } else {
        printf("O nó %d já é o último\n", n);
    }
}