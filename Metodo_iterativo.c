#include <stdio.h>

int main() {
    float x1;
    printf("Digite um numero para x1: ");
    scanf("%f", &x1);

    float x2;
    printf("Digite um numero para x2: ");
    scanf("%f", &x2);

    float x3;
    printf("Digite um numero para x3: ");
    scanf("%f", &x3);

    int numIteracoes;
    printf("Digite o numero de iteracoes desejado: ");
    scanf("%d", &numIteracoes);       
    
    for (int i = 0; i < numIteracoes; i++) {
        float x1F = 1.0/4.0*(3-2*x2-x3);
        float x2F = 1.0/3.0*(-1-x1-x3);
        float x3F = 1.0/4.0*(4-x1-x2);
        
        printf("Iteracao %d:\n", i+1);
        printf("x1 = %f\n", x1F);
        printf("x2 = %f\n", x2F);
        printf("x3 = %f\n\n", x3F);

        x1 = x1F;
        x2 = x2F;
        x3 = x3F;
    }    

    system("pause");

    return 0;
}