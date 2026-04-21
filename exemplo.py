from matriz import Matriz

A = Matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = [30, 36, 42]

x = A.eliminacao_gaussiana(b)
print(x)

t = 0.001 # tolerância
o = 20 # número máximo de iterações
x_inicial = [1, 1, 1] # ponto de partida das iterações
x, logs = A.jacobi(b, t, o, x_inicial)

for log in logs: print(log)
print(x)