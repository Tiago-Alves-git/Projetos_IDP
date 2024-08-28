#include <stdio.h>
#include <stdlib.h>

// Define a estrutura cadastroAluno
struct cadastroAluno {
    char nome[150];
    int idade;
    int nota1;
    int nota2;
    int nota3;
    int nota4;
    int notaFinal;
};

// Define um typedef para a utilização da estrutura
typedef struct cadastroAluno cad;

// Função para calcular a média das notas
float calculaNota(float grades[], int numGrades) {
    int totalGrades = 0;
    for (int i = 0; i < numGrades; i++) {
        totalGrades += grades[i];
    }
    return totalGrades / numGrades;
}

// Função para cadastrar um aluno
cad signStudent(char *name, float grades[]) {
    cad novoAluno;
    // Copiando o nome do aluno
    snprintf(novoAluno.nome, sizeof(novoAluno.nome), "%s", name);
    
    // Atribuindo as notas
    novoAluno.nota1 = grades[0];
    novoAluno.nota2 = grades[1];
    novoAluno.nota3 = grades[2];
    novoAluno.nota4 = grades[3];

    // Calculando a nota final
    novoAluno.notaFinal = calculaNota(grades, 4);
    
    return novoAluno;
}

int main() {
    // Define o nome e as notas de forma manual
    char aluno[150];
    float notas[4];
    int i;

    // Pedir o nome e as notas de forma automatica
    printf("Digite o seu nome: ");
    scanf("%149[^\n]", aluno); // Captura a entrada do nome, até 149 caracteres, e permite espaços

    // Solicita as notas do aluno
    for (i = 0; i < 4; i++) {
        printf("Digite a nota %d: ", i + 1);
        scanf("%f", &notas[i]); // Captura a entrada da nota e armazena no array
    }

    // Cadastrando o aluno
    cad novoAluno = signStudent(aluno, notas);

    // Exibindo os dados do aluno
    printf("Nome: %s\n", novoAluno.nome);
    printf("Nota 1: %d\n", novoAluno.nota1);
    printf("Nota 2: %d\n", novoAluno.nota2);
    printf("Nota 3: %d\n", novoAluno.nota3);
    printf("Nota 4: %d\n", novoAluno.nota4);
    printf("Nota Final: %d\n", novoAluno.notaFinal);

    return 0;
}
