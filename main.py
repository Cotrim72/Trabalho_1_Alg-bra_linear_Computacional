import numpy as np

from testes import TestesUmaMatriz
from matriz import Matriz

n = 10
x_inicial = [1]*n
t = 0.001
o = 20

t = TestesUmaMatriz(
    Matriz(np.random.rand(n, n).tolist()),
    np.random.rand(n).tolist(),
    t,
    o,
    x_inicial,
    'Resultados10x10'
)

t.executar()