def soma_vetor(a: list, b: list):
    res = [0]*len(a)
    for i in range(len(a)):
        res[i] = a[i] + b[i]
    return res

def sub_vetor(a: list, b: list):
    res = [0]*len(a)
    for i in range(len(a)):
        res[i] = a[i] - b[i]
    return res

def modulo_vetor(a: list):
    # Foi utilizado norma euclidiana
    soma = 0
    for i in range(len(a)):
        soma += (a[i])**(2)
    mod = soma**(1/2)
    return mod

def prod_vetor_escalar(a: list, k):
    'Retorna o produto entre o vetor a e o escalar k'
    res = [0]*len(a)
    for i in range(len(a)):
        res[i] = a[i]*k

    return res

def coluna(A: list[list], j: int):
    'Retorna uma cópia da j-ésima coluna de A.'
    return [A[i][j] for i in range(len(A))]

def prod_matriz_vetor(A: list[list], y: list):
    'Retorna o produto entre A e o vetor y'
    res = [0]*len(A)
    for i in range(len(y)):
        prod = prod_vetor_escalar(coluna(A, i), y[i])
        res = soma_vetor(res, prod)

    return res

def erro_solucao(A: list[list], x: list, b: list):
    'Retorna uma métrica para o erro de x enquanto solução do sistema A x = b. Exatamente, retorna o módulo de b - A x; quanto mais próximo de 0, melhor.'
    Ax = prod_matriz_vetor(A, x)
    erro = sub_vetor(b, Ax)
    
    return modulo_vetor(erro)

def gera_matriz_diagonal_dominante(A:list[list]):
    for i in range(len(A)):
        soma = 0
        for j in range(len(A[0])):
            if i != j:
                soma += abs(A[i][j])
        A[i][i] = abs(A[i][i]) + soma
    return A

def check_matriz_diagonal_dominante(A:list[list]):
    for i in range(len(A)):
        soma = 0
        for j in range(len(A[0])):
            if i != j:
                soma += abs(A[i][j])
        if abs(A[i][i]) < soma:
            return "Não é uma matriz diagonal dominante"
    return "A matriz é diagonal dominante"