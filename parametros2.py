# -*- coding: utf-8 -*-



#detecccion de palindromo
def es_palindromo(palabra):
    #true si es palindromo
    #false si no es palindromo

    palabra = palabra.lower()
    #quitar espacios
    palabra = palabra.replace(" ","")
    palabra = palabra.replace("á","a")
    palabra = palabra.replace("é","e")
    palabra = palabra.replace("í","i")
    palabra = palabra.replace("ó","o")
    palabra = palabra.replace("ú","u")


#quitar acentos
#transformar a minuscula
    #comparar con reverso
    return palabra == palabra[::-1]

print "palindromo"
print(es_palindromo("anita lava la tina"))
