# -*- coding: utf-8 -*-

batch_13 = ["alejandro", "frank", "sebastián", "nelly", "cynthia"]


elementos = "aire", "agua", "fuego","tierra"

# iterables... repetir sobre algo, ciclo de repeticiones

for alumno in batch_13:
    print(alumno)

# range [1,2,3,4,5,6,7,8,9]
# range ->inicio, fin(exluye el último valor de la lista),step(opcional)
for i in range(1,10,2):
    print(i)

#para tuplas utilizando "elementos"

for elemento in elementos:
    print(elemento)

persona = {
    "nombre": "héctor",
    "apellido": "pat",
    "edad": 27,
}

print("diccionario =====")
for dato,valor in persona.iteritems():
    print(dato + ":" + str(valor))
