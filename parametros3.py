# -*- coding: utf-8 -*-



#detecccion de palindromo
def es_palindromo(palabra):
    #true si es palindromo
    #false si no es palindromo

    palabra = palabra.lower()
    #quitar espacios de manera compacta

    reemplazos = {
        " ": "",
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
    }

    for viejo, nuevo in reemplazos.iteritems():
        palabra = palabra.replace(viejo, nuevo)
#quitar acentos
#transformar a minuscula
    #comparar con reverso
    return palabra == palabra[::-1]

print "palindromo"
print(es_palindromo("anita lava la tiná"))
