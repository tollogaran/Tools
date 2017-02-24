# -*- coding: utf-8 -*-

class Persona:
    Nombre = ""
    Lic_Ing = ""
    Origen = ""
    Genero = ""
    EtadoConyugal = ""

    #lo anterior fueron propiedades dentro de clase


    #constructor de la clase
    def __init__(self, nombre, Lic_Ing, origen, Genero, EtadoConyugal ):
        self.nombre = nombre
        self.sku = sku
        self.precio = precio


    def establecer_imagen(self, imagen):
        #ir por imagena internet
        #guardarla con un nombre relacionado al producto
        self.imagen = imagen


class Licenciado(Persona): #esta clase va dentro de la clase anterior Producto
      Especialidad= ""
      Experiencia = ""

    def Experiencia(self):
        return True


class Ingeniero(Persona):
      Especialidad = ""
      Experiencia = ""



Secretaria = Persona("sonia", "Licenciado", "Female")
print(Secretaria.nombre)
print(Secretaria.Origen)
print(Secretaria.Genero)
