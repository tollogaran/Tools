# -*- coding: utf-8 -*-

def es_primo(n):
    #es el que ns es duvisible entre los numeros anteriores
    lista_numeros_menores = range(2, n)

    for numero in lista_numeros_menores:
        if n % numero == 0:
            return False
    return True

print(es_primo(11))
