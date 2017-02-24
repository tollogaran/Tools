# -*- coding: utf-8 -*-

#funciones sin parametros


def saludar():
    print "hola"

#asi se llama a la funcion para ejecutarse
saludar()

#funciones con parametros posicionales
def saludar_a(nombre):
    print "hola  " + nombre

saludar_a("Ian")

def componer_nombres(nombre, apellido):
    return nombre.capitalize() + " " + apellido.capitalize()


    #solo hgace el calculo y no lo muestra en la terminal, pere ejecuta algun codigo, a diferencia del print que si tiene efecto secundario

componer_nombres("cinthya", "remolina")

#asi ya lo muestra
nombre_completo = componer_nombres("cinthya", "remolina")
    print(nombre_completo)

#tarea funciones para strings en python 2,para retonar lo nombres ocn mayusucula la primera



#detecccion de palindromo
def es_palindromo(palabra):
    #true si es palindromo
    #false si no es palindromo
    return palabra == palabra[::-1]
