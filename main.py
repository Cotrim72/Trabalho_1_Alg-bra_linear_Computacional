import time
import numpy as np

from matriz import Matriz

n = 10
B = np.random.rand(n, n).tolist() #matriz aleatória gerada
b = np.random.rand(n).tolist()
x = [1]*len(b)
t = 0.001
o = 20

# Gauss sem biblioteca
A = Matriz(B)
inicio_gauss = time.time()
print(A.eliminaçao_gaussiana(b))
final_gauss = time.time()
print("Tempo gauss sem biblioteca:")
print(final_gauss-inicio_gauss)

# Lu sem biblioteca
A = Matriz(B)
inicio_lu = time.time()
print(A.fatoraçao_lu(b))
final_lu = time.time()
print("Tempo lu sem biblioteca:")
print(final_lu-inicio_lu)

# Gauss com bibioteca
A = Matriz(B)
inicio_gauss_bib = time.time()
print(A.eliminaçao_gaussiana_numpy(b))
final_gauss_bib = time.time()
print("Tempo gauss com biblioteca:")
print(final_gauss_bib-inicio_gauss_bib)

# Lu com biblioteca
A = Matriz(B)
inicio_lu_bib = time.time()
print(A.fatoraçao_lu_scipy(b))
final_lu_bib = time.time()
print("Tempo lu com biblioteca:")
print(final_lu_bib-inicio_lu_bib)

# Jacobi sem biblioteca
A = Matriz(B)
inicio_jacobi = time.time()
print(A.jacobi(b,t,o,x))
final_jacobi = time.time()
print("Tempo jacobi sem biblioteca:")
print(final_jacobi-inicio_jacobi)

# Gauss_Seidel sem biblioteca
A = Matriz(B)
inicio_Gauss_Seidel = time.time()
print(A.gauss_seidel(b,t,o,x))
final_Gauss_Seidel = time.time()
print("Tempo Gauss_seidel sem biblioteca:")
print(final_Gauss_Seidel-inicio_Gauss_Seidel)

# Gauss_Seidel com biblioteca
inicio_Gauss_Seidel_bib = time.time()
A = Matriz(B)
print(A.gauss_seidel_scipy(b,t,o))
final_Gauss_Seidel_bib = time.time()
print("Tempo Gauss_seidel com biblioteca:")
print(final_Gauss_Seidel_bib-inicio_Gauss_Seidel_bib)