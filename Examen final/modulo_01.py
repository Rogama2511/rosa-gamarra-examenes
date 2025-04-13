"""
- Crear una función que le permitirá almacenar 10 números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
- Crear una función para indicar cuál es mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola.
- Crear el archivo principal.py, donde solo llamarás las anteriores funciones
que se encontrarán alojadas en un módulo
"""

import random


def num_aleatorios():
    lista = []
    for numero in range(10):
        while numero not in lista and len(lista) < 10:
            lista.append(numero)
            numero = random.randint(0, 100)
    print("Lista: {}".format(lista))
    return lista


def borrar_repetidos(lista):
    list_valores_unicos = list(set(lista))
    print("Lista sin números repetidos: {}".format(list_valores_unicos))
    return list


def ordenar(lista):
    lista1 = lista.copy()
    lista1.sort()
    lista2 = lista1.copy()
    lista2.reverse()
    print("Lista ordenada de menor a mayor: {}".format(lista1))
    print("Lista ordenada de mayor a menor: {}".format(lista2))
    return


def num_mayor(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    if pares:
        mayor = max(pares)
        print("El número par mayor es: {}".format(mayor))
        return mayor
    else:
        print("No hay números pares en la lista")
        return
