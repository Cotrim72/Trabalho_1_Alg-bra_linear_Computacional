import numpy as np
from scipy.linalg import lu_factor, lu_solve
from scipy.sparse.linalg import gmres

from utilidades import sub_vector, modulo_vector

class Matriz:
    def __init__(self, A):
        self.A = A

    def substituicao_para_tras(self, b):
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

    def substituiçao_para_a_frente(self, b):
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
        return self.substituicao_para_tras(b)

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
        y = fl.substituiçao_para_a_frente(b)
        return fu.substituicao_para_tras(y)

    def fatoraçao_lu_scipy(self, b):
        A = np.array(self.A)
        B = np.array(b)
        lu, piv = lu_factor(A)
        x = lu_solve((lu, piv), b)
        return x
    
    def jacobi(self,b,t,o,x,n=0):
        n += 1
        if n > o:
            return "Ultrapassou o número máximo de operações"
        x_novo = [0]*len(x)
        for i in range(len(x)):
            soma = 0
            for j in range(len(x)):
                if i != j:
                    soma += self.A[i][j]*x[j]
            x_novo[i] = (b[i] - soma)/self.A[i][i]
        R = modulo_vector(sub_vector(x_novo,x))/modulo_vector(x_novo)
        if R <= t:
            return (f"Iteração {n}: Erro = {R}, x = {x_novo}")
        print(f"Iteração {n}: Erro = {R}, x = {x_novo}")
        return self.jacobi(b,t,o,x_novo,n)
    
    def gauss_seidel(self,b,t,o,x,n=0):
        n += 1
        if n > o:
            return "Ultrapassou o número máximo de operações"
        x_novo = [0]*len(x)
        for i in range(len(x)):
            soma_new = 0
            soma_old = 0
            for j in range(i):
                soma_new += self.A[i][j]*x_novo[j]
            for j in range(i+1,len(x)):
                soma_old += self.A[i][j]*x[j]
            x_novo[i] = (b[i] - soma_new - soma_old)/self.A[i][i]
        R = modulo_vector(sub_vector(x_novo,x))/modulo_vector(x_novo)
        if R <= t:
            return (f"Iteração {n}: Erro = {R}, x = {x_novo}")
        print(f"Iteração {n}: Erro = {R}, x = {x_novo}")
        return self.gauss_seidel(b,t,o,x_novo,n)
    
    def gauss_seidel_scipy(self,b,t,o,n=0):
        A = np.array(self.A, dtype=float)
        B = np.array(b, dtype=float)
        x, info = gmres(A, b=B, rtol = t, maxiter=o)
        print(f"Solução: {x}")
