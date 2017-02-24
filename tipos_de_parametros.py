# -*- coding: utf-8 -*-

def precio_final(precio=0, tasa_iva=0.16):
    return precio * (1 + tasa_iva)
#aunque ya hay valores ppor default, los valores a utilizar son las que apenas estan por darse
#en python siempre debe ir primero la la función "def"
p = 10000
t = 0.16

print(precio_final(precio=p, tasa_iva=t))


def imprimir_lista_de_productos(*args):
    #args es una lista [], de todos los parametros que recibe
    for producto in args:
        print(producto)

imprimir_lista_de_productos("silla", "mesa", "sillón")


def aplicar_impuestos(precio, **kwargs):
    lista_impuestos=[]
    for impuesto, porcentaje in kwargs.iteritems():
        valor_impuesto = precio * porcentaje
        print(impuesto + " = " + str(valor_impuesto))
        print(valor_impuesto + precio)



aplicar_impuestos(1000, iva=.16, ipss=.04, isr=.18)
