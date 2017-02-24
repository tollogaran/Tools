# -*- coding: utf-8 -*-

class Producto:
    precio = 0
    calidad = "buena"
    origen = ""
    sku = ""
    nombre = ""
    imagen = ""
    #lo anterior fueron propiedades dentro de clase


    #constructor de la clase
    def __init__(self, nombre, sku, precio):
        self.nombre = nombre
        self.sku = sku
        self.precio = precio


    def establecer_imagen(self, imagen):
        #ir por imagena internet
        #guardarla con un nombre relacionado al producto
        self.imagen = imagen


class ProductoFisico(Producto): #esta clase va dentro de la clase anterior Producto
    fecha_de_caducidad = ""

    def esta_caduco(self):
        return True


class ProdcutoVirtual(Producto):
    tamano_mb = 0.0


tele = ProductoFisico("tv sony", "1900474675", 100.90)
print(tele.nombre)
print(tele.sku)
print(tele.precio)

radio = ProductoFisico("motorola", "160", 10.50)
print(radio.nombre)
print(radio.sku)
print(radio.precio)
