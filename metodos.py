# -*- coding: utf-8 -*-

class MetodoDePago:
    def cobrar(self, cantidad):
        pass

class Stripe(MetodoDePago):
    """
        Esta es la calse encargada de cobrar con stripe
        implementa la interface de metodo de pago
    """
    token = "fjekbvekjvne"
    mail = "jnverjnvetonetgv"


    @classmethod
    def cobrar(cls, cantidad):
    """
        Esta es la func que cobra
    """
        #hice todos los pasos necesarios para cobrar
        print("Cobre con stripe %s" % cantidad)

    @staticmethod
    def un_metodo_statico():
        pass



class Efectivo(MetodoDePago):
    def cobrar(self, cantidad):
        print("Envíe corre al clinete para que prepare el dinmero")

class Bitcoin(MetodoDePago):
    def cobrar(self, cantidad):
        print("convertirwjwjwjknevnef")
