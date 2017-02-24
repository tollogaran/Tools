# -*- coding: utf-8 -*-

#funciones, def declara funciones

#grupo = [
#   "toño": {"nombre":"anotnio", "edad";41},
#    "jimy": {"nombre":"ximena", "edad":24}
#]
def imprmir_grupo(grupo):

    #guarda codigo y lo ejecutas cuanspo lo llamas
    for alumno in grupo:
        for dato, valor in alumno.iteritems():
            print(dato + " es " + str(valor))

batch_13 = [
    {"nombre":"antonio", "edad":41},
    {"nombre":"ximena", "edad":24}
]

imprmir_grupo(batch_13)
