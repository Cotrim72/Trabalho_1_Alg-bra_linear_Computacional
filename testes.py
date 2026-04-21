import time
import numpy as np
from math import log10
import matplotlib.pyplot as plt

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
        r.write(f'Matriz A ({self.n} x {self.n}):')
        r.write(self.A)

        r.skipline()
        r.write('Vetor b:')
        r.write(self.b)

        r.skipline()
        r.write('Configurações dos métodos iterativos:')
        r.write(f'Tolerância t: {self.t}')
        r.write(f'Número máximo de iterações o: {self.o}')

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
        x, logs = getattr(self.A, metodo)(self.b, self.t, self.o, self.x_inicial)
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

        # Gerar gráfico do log10 do erro em função da iteração
        iteracoes = [l.iteracao for l in logs]
        erros = [log10(l.erro) for l in logs]
        
        plt.figure()
        plt.plot(iteracoes, erros)
        plt.xlabel('Iteração')
        plt.ylabel('log10(Erro relativo)')
        plt.title(f'Convergência - {metodo}')
        
        nome_grafico = caminho_saida.replace('.txt', '.png')
        plt.savefig(nome_grafico)
        plt.close()

    def teste_metodo_iterativo_biblioteca(self, metodo, caminho_saida):
        r = Results()
        inicio = time.time()
        x = getattr(self.A, metodo)(self.b, self.t, self.o)
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
