"""Prática Módulo I"""
"""Resolución pregunta 01"""

#Definir Variables
nombre = "Rosa"
salario = 2500
edad = "19"
compania ="UNMSM"

#Identificar los tipos de variables
print("Tipo de variables")
print("Nombre es tipo: {}".format(type(nombre)))
print("Salario es tipo: {}".format(type(salario)))
print("Edad es tipo: {}".format(type(edad)))
print("Compañia es tipo: {}".format(type(compania)))

print(" ")
#Verificar el bono que adquiere
if int(edad) > 30:
    bono = 0.10
    print("Usted tiene un bono de 10% en el mes de diciembre")
else :
    bono = 0.05
    print("Usted tiene un bono del 5% en el mes diciembre")

#Calculo del Bono final correspondiente
bono_final = (salario ** 2) + (salario * bono)
print("El valor de su bono final es: {}".format(bono_final))


