# -*- coding: utf-8 -*-

def obtener_anagramas(palabra):
    if len(palabras) == 1:
        return list(palabra)

    letras = list(palabra)
    unique_letras = list(set(letras))
    anagramas = []
    for letra in unique_letras:
        n_lista = letras[:]
        n_lista = remove(letra)
        # TODO eliminar duplicados
        for anagrama in obtener_anagramas(n_lista):
            anagramas.append(letra + anagrama)
    return anagramas

# singulait = obtener_anagramas("singulait")
print(len(singulait))
