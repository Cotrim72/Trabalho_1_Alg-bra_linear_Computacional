import time
import numpy as np
from scipy.linalg import lu_factor, lu_solve


class Matriz:
    def __init__(self, A):
        self.A = A

    def retro_substituiçao_para_atras(self, b):
        res = [0]*len(b)
        res[len(res)-1] = b[len(b)-1]/(self.A[len(self.A)-1][len(self.A[0])-1])
        i = len(b) - 2
        while i >= 0:
            soma = 0
            for j in range(i+1, len(b)):
                soma += (self.A[i][j]*res[j])
            res[i] = (b[i] - soma)/self.A[i][i]
            i -= 1
        return res

    def retro_substituiçao_para_frente(self, b):
        res = [0]*len(b)
        res[0] = b[0]/(self.A[0][0])
        i = 1
        while i < len(b):
            soma = 0
            for j in range(0, i):
                soma += (self.A[i][j]*res[j])
            res[i] = (b[i] - soma)/self.A[i][i]
            i += 1
        return res

    def eliminaçao_gaussiana(self, b):
        n = len(b)
        for i in range(n):
            pivo = self.A[i][i]
            for j in range(i+1, n):
                multiplicador = self.A[j][i]/pivo
                for k in range(i, n):
                    self.A[j][k] -= self.A[i][k]*multiplicador
                b[j] -= multiplicador*b[i]
        return self.retro_substituiçao_para_atras(b)

    def eliminaçao_gaussiana_numpy(self, b):
        A = np.array(self.A)
        B = np.array(b)
        x = np.linalg.solve(A, B)
        return x

    def fatoraçao_lu(self, b):
        n = len(self.A)
        L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
        U = [line[:] for line in self.A]

        for i in range(n):
            for j in range(i + 1, n):
                multiplicador = U[j][i] / U[i][i]
                L[j][i] = multiplicador
                for k in range(i, n):
                    U[j][k] -= multiplicador * U[i][k]
        fl = Matriz(L)
        fu = Matriz(U)
        y = fl.retro_substituiçao_para_frente(b)
        return fu.retro_substituiçao_para_atras(y)

    def fatoraçao_lu_scify(self, b):
        A = np.array(self.A)
        B = np.array(b)
        lu, piv = lu_factor(A)
        x = lu_solve((lu, piv), b)
        return x


n = 4
B = np.random.rand(n, n).tolist()
b = np.random.rand(n).tolist()
A = Matriz(B)
# Gauss sem biblioteca
inicio_gauss = time.time()
print(A.eliminaçao_gaussiana(b))
final_gauss = time.time()
print("Tempo gauss sem biblioteca:")
print(final_gauss-inicio_gauss)

# Lu sem biblioteca
inicio_lu = time.time()
print(A.fatoraçao_lu(b))
final_lu = time.time()
print("Tempo lu sem biblioteca:")
print(final_lu-inicio_lu)

# Gauss com bibioteca
inicio_gauss_bib = time.time()
print(A.eliminaçao_gaussiana_numpy(b))
final_gauss_bib = time.time()
print("Tempo gauss com biblioteca:")
print(final_gauss_bib-inicio_gauss_bib)

# Lu com biblioteca
inicio_lu_bib = time.time()
print(A.fatoraçao_lu_scify(b))
final_lu_bib = time.time()
print("Tempo lu com biblioteca:")
print(final_lu_bib-inicio_lu_bib)
