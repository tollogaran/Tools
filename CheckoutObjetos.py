# -*- coding: utf-8 -*-
#para importar info de otra ventana
from ObjetoProductos import ProductoFisico
from metodos import Stripe, Bitcoin
#antes se crea un archivo en la carpeta madre __init_.py
class Checkout:

    def __init__(self, metodo_de_pago):
        self.metodo_de_pago = metodo_de_pago



    def obtener_total(self, lista_productos):
        total = 0
        for producto in lista_productos:
            total += producto.precio
        return total


    def imprimir_lista(self, lista_productos):
            for producto in lista_productos:
                print("Nombre: %s, sku: %s, Precio: %s" % (producto.nombre,
                producto.sku, producto.precio))

    def cobrar(self, lista_productos):
        total = self.obtener_total(lista_productos)
        self.metodo_de_pago.cobrar(total)
        print("He cobrado %s" % total)



tele = ProductoFisico("tele", "100", 100)
radio = ProductoFisico("radio", "160", 1050)
compu = ProductoFisico("compu", "990", 10330)
lista_productos = [tele, radio, compu,]

stripe = Stripe()
checkout_stripe = Checkout(Stripe)
checkout_stripe.cobrar(lista_productos)
help(Stripe)

#checkout.imprimir_lista(lista_productos)
#print(checkout.obtener_total(lista_productos))
