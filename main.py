import time
import numpy as np

from Dependencias.results import Results
from matriz import Matriz

def teste_metodo_direto(A: Matriz, b, metodo, caminho_saida):
    r = Results()
    inicio = time.time()
    x = getattr(A, metodo)(b)
    final = time.time()
    r.write('Solução x:')
    r.write(x)

    r.skipline()
    r.write(f'Erro da solução (|Ax - b|): {A.erro_solucao(x, b)}')
    r.write(f'Tempo de execução: {final - inicio}')

    r.generate_file(caminho_saida)

def teste_metodo_iterativo(A: Matriz, b, t, o, x_inicial, metodo, caminho_saida):
    r = Results()
    inicio = time.time()
    x, logs = getattr(A, metodo)(b, t, o, x_inicial)
    final = time.time()

    r.write('Logs intermediários:')
    for l in logs: r.write(l)

    r.skipline()
    r.write('Solução x:')
    r.write(x)

    r.skipline()
    r.write(f'Erro da solução (|Ax - b|): {A.erro_solucao(x, b)}')
    r.write(f'Tempo de execução: {final - inicio}')

    r.generate_file(caminho_saida)

def teste_metodo_iterativo_biblioteca(A: Matriz, b, t, o, metodo, caminho_saida):
    r = Results()
    inicio = time.time()
    x = getattr(A, metodo)(b, t, o)
    final = time.time()

    r.write('Solução x:')
    r.write(x)

    r.skipline()
    r.write(f'Erro da solução (|Ax - b|): {A.erro_solucao(x, b)}')
    r.write(f'Tempo de execução: {final - inicio}')

    r.generate_file(caminho_saida)

def testes_uma_matriz(n, t, o, x_inicial, caminho_saida):
    'Gera uma matriz aleatória n x n, executa todos os métodos e escreve na pasta caminho_saida os resultados'
    matriz = np.random.rand(n, n).tolist() #matriz aleatória gerada
    A = Matriz(matriz)
    b = np.random.rand(n).tolist()

    # Configurações
    r = Results()
    r.write('Sistema A x = b')

    r.skipline()
    r.write(f'Matriz A ({n} x {n}:')
    r.write(A)

    r.skipline()
    r.write('Vetor b:')
    r.write(b)

    r.skipline()
    r.write('Configurações dos métodos iterativos:')
    r.write(f'Tolerância t: {t}')
    r.write(f'Número máximo de iterações o: {o}')

    r.generate_file(f'{caminho_saida}/configuracoes.txt')

    teste_metodo_direto(A, b, 'eliminacao_gaussiana', f'{caminho_saida}/Resultados/eliminacao_gaussiana.txt')
    teste_metodo_direto(A, b, 'fatoracao_lu', f'{caminho_saida}/Resultados/fatoracao_lu.txt')

    teste_metodo_iterativo(A, b, t, o, x_inicial, 'jacobi', f'{caminho_saida}/Resultados/jacobi.txt')
    teste_metodo_iterativo(A, b, t, o, x_inicial, 'gauss_seidel', f'{caminho_saida}/Resultados/gauss_seidel.txt')

    # Métodos implementados por bibliotecas, para comparação
    teste_metodo_direto(A, b, 'eliminacao_gaussiana_numpy', f'{caminho_saida}/Bibliotecas/eliminacao_gaussiana.txt')
    teste_metodo_direto(A, b, 'fatoracao_lu_scipy', f'{caminho_saida}/Bibliotecas/fatoracao_lu.txt')
    teste_metodo_iterativo_biblioteca(A, b, t, o, 'gauss_seidel_scipy', f'{caminho_saida}/Bibliotecas/gauss_seidel.txt')

n = 10
x_inicial = [1]*n
t = 0.001
o = 20

testes_uma_matriz(n, t, o, x_inicial, 'Resultados10x10')