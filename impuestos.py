# -*- coding: utf-8 -*-



def aplicar_impuestos(precio, **kwargs):
    total_impuestos = 0
    for impuesto, tasa in kwargs.iteritems():
        impuesto_actual = precio * tasa
        total_impuestos = total_impuestos + impuesto_actual
        print (impuesto + " es " + str(impuesto_actual))
        print(total_impuestos)
    return precio + total_impuestos



aplicar_impuestos(1000, iva = .16, ipss = .04, isr = .18)

#tutorial: hackerrank.com , codeeval.com, codewars.com, codefights.com
