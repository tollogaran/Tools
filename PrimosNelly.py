# -*- coding: utf-8 -*-



def numeros_primos(n, p):
    x = 0
    lista =[]
    while x < n:
        for numero in range(2, p):
            if p % numero == 0:
                p = p+1
                break

        else:
            print p
            lista.append(p)
            p = p+1
            x = x+1

    return lista

print(numeros_primos(100, 2))
