import numpy as np

from testes import TestesUmaMatriz
from matriz import SistemaLinear

n = 3
x_inicial = [1]*n
t = 0.001
o = 100

t = TestesUmaMatriz(
    np.random.rand(n, n).tolist(),
    np.random.rand(n).tolist(),
    t,
    o,
    x_inicial,
    'Resultados3x3'
)

t.executar()