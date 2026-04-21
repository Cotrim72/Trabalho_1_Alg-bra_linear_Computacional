def sub_vector(a,b):
    res = [0]*len(a)
    for i in range(len(a)):
        res[i] = a[i] - b[i]
    return res

def modulo_vector(a):
    # Foi utilizado norma euclidiana
    soma = 0
    for i in range(len(a)):
        soma += (a[i])**(2)
    mod = soma**(1/2)
    return mod