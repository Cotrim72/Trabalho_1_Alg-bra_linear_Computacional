import numpy as np

from testes import TestesUmaMatriz
from Dependencias.utilidades import gera_matriz_diagonal_dominante

n = 3
x_inicial = [1]*n
t = 0.001
o = 50

t = TestesUmaMatriz(
    gera_matriz_diagonal_dominante(np.random.rand(n, n).tolist()),
    np.random.rand(n).tolist(),
    t,
    o,
    x_inicial,
    'Resultados3x3'
)

t.executar()