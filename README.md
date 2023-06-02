# Método iterativo

![Equação](https://github.com/Gustavo-Guilherme-Wanderley/M-Iterativo/assets/77367556/b38e2cce-73fb-430f-90e8-e9e8b328f1b6)

O sistema de equações simultâneas pode ser resolvido usando um procedimento chamado de iteração.
O processo iterativo consiste em considerar um valor inicial para (x1, x2, x3). Substituindo esse valor
inicial nas equações do sistema, obter um novo valor para (x1, x2, x3); esse novo valor é substituído nas
equações do sistema para obter outro novo valor para (x1, x2, x3) e assim sucessivamente até que uma
boa solução para o sistema seja obtida. Cada substituição é uma iteração

O usuário deve entra, via teclado, com o número de iterações, n, que deseja realizar e o programa deve apresentar na tela os
valores de (x1, x2, x3) obtido em cada iteração.

```
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
```

Escolhi utilizar cerca de 30 iterações para ter certeza do comportamento exibido das variáveis x1, x2 e x3.
Após isso, coloquei todos os valores numa lista e utilizei a biblioteca matplotlib do python para fazer um gráfico.
```
import matplotlib.pyplot as plt

# Dados das iterações
iteracoes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
x1 = [0.7500000000, 0.666667, 0.984375, 0.911458, 1.015951, 0.973307, 1.010518, 0.990662, 1.004955, 0.996424,
      1.002132, 0.998573, 1.00089, 0.999421, 1.000367, 0.999763, 1.000151, 0.999903, 1.000062, 0.99996,
      1.000026, 0.999984, 1.00001, 0.999993, 1.000004, 0.999997, 1.000002, 0.999999, 1.000001, 1]
x2 = [-0.333333, -0.916667, -0.854167, -1.015625, -0.959635, -1.013997, -0.986409, -1.006897, -0.994878, -1.003005,
      -0.997968, -1.001259, -1.001259, -1.00052, -0.999664, -1.000214, -0.999863, -1.000088, -0.999944, -0.999944,
      -0.999944, -1.000015, -0.999991, -1.000006, -0.999996, -1.000003, -0.999998, -1.000001, -0.999999, -1]
x3 = [1.0000, 0.895833, 1.0625, 0.967448, 1.026042, 0.985921, 1.010172, 0.993973, 1.004059, 0.997481,
      1.001645, 0.998959, 1.000672, 0.999572, 1.000275, 0.999824, 1.000113, 0.999928, 1.000046, 0.99997,
      1.000019, 0.999988, 1.000008, 0.999995, 1.000003, 0.999998, 1.000001, 0.999999, 1.000001, 1]

# Criando o gráfico
plt.plot(iteracoes, x1, label='x1')
plt.plot(iteracoes, x2, label='x2')
plt.plot(iteracoes, x3, label='x3')
```
![grafico](https://github.com/Gustavo-Guilherme-Wanderley/M-Iterativo/assets/77367556/14bb9f39-0d46-4ced-9ba6-4831a8951123)
