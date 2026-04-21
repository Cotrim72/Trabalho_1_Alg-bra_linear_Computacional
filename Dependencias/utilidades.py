def soma_vetor(a,b):
    res = [0]*len(a)
    for i in range(len(a)):
        res[i] = a[i] + b[i]
    return res

def sub_vetor(a,b):
    res = [0]*len(a)
    for i in range(len(a)):
        res[i] = a[i] - b[i]
    return res

def modulo_vetor(a):
    # Foi utilizado norma euclidiana
    soma = 0
    for i in range(len(a)):
        soma += (a[i])**(2)
    mod = soma**(1/2)
    return mod

def prod_vetor_escalar(a, k):
    'Retorna o produto entre o vetor a e o escalar k'
    res = [0]*len(a)
    for i in range(len(a)):
        res[i] = a[i]*k

    return res