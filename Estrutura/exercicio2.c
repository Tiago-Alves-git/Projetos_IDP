#include <stdio.h>

// Definindo a estrutura para armazenar os dados do cliente
struct Emprestimo {
    char nome[100];
    float salario;
    float valorEmprestimo;
    int meses;
};

typedef struct Emprestimo Emprestimo;

int main() {
    Emprestimo clientes[10];  // Array para armazenar dados de 10 clientes
    int aprovados = 0;  // Contador para empréstimos aprovados
    int reprovados = 0; // Contador para empréstimos reprovados

    // Loop para capturar os dados dos clientes
    for (int i = 0; i < 10; i++) {
        printf("Digite o nome do cliente %d: ", i + 1);
        scanf("%99s", clientes[i].nome);  // Le o nome do cliente

        printf("Digite o salário do cliente %d: ", i + 1);
        scanf("%f", &clientes[i].salario);  // Le o salário do cliente

        printf("Digite o valor do empréstimo do cliente %d: ", i + 1);
        scanf("%f", &clientes[i].valorEmprestimo);  // Le o valor do empréstimo

        printf("Digite o número de meses para quitação do empréstimo do cliente %d: ", i + 1);
        scanf("%d", &clientes[i].meses);  // Le o número de meses para quitação

        // Calcula o valor da parcela
        float valorParcela = clientes[i].valorEmprestimo / clientes[i].meses;

        // Verifica se a parcela é maior que 20% do salário
        if (valorParcela > (clientes[i].salario * 0.2)) {
            printf("Empréstimo do cliente %s REPROVADO.\n", clientes[i].nome);
            reprovados++;  // Incrementa o contador de reprovados
        } else {
            printf("Empréstimo do cliente %s APROVADO.\n", clientes[i].nome);
            aprovados++;  // Incrementa o contador de aprovados
        }

        printf("\n");  // Linha em branco para separar a entrada de cada cliente
    }

    // Exibe o resultado final
    printf("Quantidade de empréstimos aprovados: %d\n", aprovados);
    printf("Quantidade de empréstimos reprovados: %d\n", reprovados);

    return 0;
}
