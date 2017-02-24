# -*- coding: utf-8 -*-

#Crear una función que calcule los primeros 20
#números primos (Número primo: sólo divisible entre 1 y si mismo). -> primeros_veinte_primos()

def primeros_20_primos():
    primos = [2]
    contador = 3
    while(len(primos) < 20):
        es_primo = True
        for primo in primos:
            if contador % primo == 0:
                es_primo = False
                break;
        if es_primo:
            primos.append(contador)
        contador += 2;
    return primos

print(primeros_20_primos())

#func que calcula primeros 20

#def primeros_n_primos(n):
