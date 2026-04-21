import time
import numpy as np

from Dependencias.results import Results
from matriz import Matriz

class TestesUmaMatriz:
    'Objetivo: executar todos os métodos em uma única matriz A e um único vetor B, e escrever os resultados em arquivos'

    def __init__(self, A: Matriz, b, t, o, x_inicial, caminho_saida):
        self.A = A
        self.n = A.tamanho()
        self.b = b

        self.t = t
        self.o = o
        self.x_inicial = x_inicial

        self.caminho_saida = caminho_saida

    def escrever_configuracoes(self):
        # Configurações
        r = Results()
        r.write('Sistema A x = b')

        r.skipline()
        r.write(f'Matriz A ({n} x {n}):')
        r.write(self.A)

        r.skipline()
        r.write('Vetor b:')
        r.write(self.b)

        r.skipline()
        r.write('Configurações dos métodos iterativos:')
        r.write(f'Tolerância t: {t}')
        r.write(f'Número máximo de iterações o: {o}')

        r.generate_file(f'{self.caminho_saida}/configuracoes.txt')

    def teste_metodo_direto(self, metodo, caminho_saida):
        r = Results()
        inicio = time.time()
        x = getattr(self.A, metodo)(self.b)
        final = time.time()
        r.write('Solução x:')
        r.write(x)

        r.skipline()
        r.write(f'Erro da solução (|Ax - b|): {self.A.erro_solucao(x, self.b)}')
        r.write(f'Tempo de execução: {final - inicio}')

        r.generate_file(caminho_saida)

    def teste_metodo_iterativo(self, metodo, caminho_saida):
        r = Results()
        inicio = time.time()
        x, logs = getattr(self.A, metodo)(self.b, t, o, x_inicial)
        final = time.time()

        r.write('Logs intermediários:')
        for l in logs: r.write(l)

        r.skipline()
        r.write('Solução x:')
        r.write(x)

        r.skipline()
        r.write(f'Erro da solução (|Ax - b|): {self.A.erro_solucao(x, self.b)}')
        r.write(f'Tempo de execução: {final - inicio}')

        r.generate_file(caminho_saida)

    def teste_metodo_iterativo_biblioteca(self, metodo, caminho_saida):
        r = Results()
        inicio = time.time()
        x = getattr(self.A, metodo)(self.b, t, o)
        final = time.time()

        r.write('Solução x:')
        r.write(x)

        r.skipline()
        r.write(f'Erro da solução (|Ax - b|): {self.A.erro_solucao(x, self.b)}')
        r.write(f'Tempo de execução: {final - inicio}')

        r.generate_file(caminho_saida)

    def executar(self):
        pasta = self.caminho_saida

        self.escrever_configuracoes()

        self.teste_metodo_direto('eliminacao_gaussiana', f'{pasta}/Resultados/eliminacao_gaussiana.txt')
        self.teste_metodo_direto('fatoracao_lu', f'{pasta}/Resultados/fatoracao_lu.txt')

        self.teste_metodo_iterativo('jacobi', f'{pasta}/Resultados/jacobi.txt')
        self.teste_metodo_iterativo('gauss_seidel', f'{pasta}/Resultados/gauss_seidel.txt')

        self.teste_metodo_direto('eliminacao_gaussiana_numpy', f'{pasta}/Bibliotecas/eliminacao_gaussiana.txt')
        self.teste_metodo_direto('fatoracao_lu_scipy', f'{pasta}/Bibliotecas/fatoracao_lu.txt')

        self.teste_metodo_iterativo_biblioteca('gauss_seidel_scipy', f'{pasta}/Bibliotecas/gauss_seidel.txt')

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