entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(e, p):
    s = 0
    #o loop sabe que deve itear sobre os dois vetores, já que foi passado os argunmentos para a função soma
    for i in range(3):  
        print(entradas[i])
        print(pesos[i])

        s += e[i] * p[i]

    print(s)
    return s

#tornar o resultado disponivel caso ele precise ser utilizado para outras funções
s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0 

r = stepFunction(s)
print(r)