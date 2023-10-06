#Importar a bibliteca numpy para usar na função soma e usado para lidar com grandes quantidades de dados além de deixar o código mais limpo 

import numpy as np

entradas = np.array([1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def soma(e, p):
    return e.dot(p)

#tornar o resultado disponivel caso ele precise ser utilizado para outras funções
s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0 

r = stepFunction(s)
print(r)