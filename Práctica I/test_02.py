"""Prática Módulo I"""

"""Resolución pregunta 02"""

#Crear lista vacia
list = []

#Datos
nombre = "Rosa"
apellido = "Gamarra"
salario = 2500
edad = "19"
compania ="UNMSM"
bono_final = 6250125.0

#Agregar datos
list.append(nombre)
list.append(apellido)
list.append(salario)
list.append(edad)
list.append(compania)
list.append(bono_final)

print(list)

print(" ")
#Variable si esta o no trabajando
trabaja_actual = False
list.append(trabaja_actual)

print("Datos: {}".format(list))
print("Tamaño de la lista: {}".format(len(list)))

#Mensaje
if trabaja_actual:
    print(f"El trabajador {nombre} {apellido} se encuentra trabajando actualmente en la compañía")
else:
    print(f"El trabajador {nombre} {apellido} ya no se encuentra trabajando actualmente en la empresa")
