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
