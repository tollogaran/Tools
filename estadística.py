# -*- coding: utf-8 -*-

#lista de valores = [10, 100, 90.9, 100]
#suma_total / numero_elementos
def promedio(lista_valores):
    promedio = sum(lista_valores) / len(lista_valores)
    return promedio


def moda(lista_valores):
    valores = {}
    for valor in lista_valores:
        if valores.get(valor):           #asi se le pregunta al diccionario
            valores[valor] += 1
        else:
            valores[valor] = 1

    print(valores)

    v_max = 0
    moda = 0
    for valor, repeticiones in valores.iteritems():
        if repeticiones > v_max:
            v_max = repeticiones
            moda = valor

    return moda
#sacar mediana
def mediana(lista_valores):
    #ordenar lista_valores,
    #detactar si es par o impar
    #par: devolver prom centrales
    #impar: valor centrales

    lista_valores.sort()
    n = len(lista_valores)
    if n % 2:
        return lista_valores[n/2]
    else:
        return (lista_valores[n/2] + lista_valores[n/2 + 1])/2
    return mediana


lista_valores = [10, 100, 90.9, 100, 3, 3, 3]
print(mediana(lista_valores))
