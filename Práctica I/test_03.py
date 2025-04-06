"""Prática Módulo I"""

"""Resolución pregunta 03"""

#Lista de la pregunta 2
print("Nombre, Apellido, Salario, Edad, Compañia, Bono final, Trabaja Actualmente")
list_2 = ['Rosa', 'Gamarra', 2500, '19', 'UNMSM', 6250125.0, False]
print(list_2)

print(" ")
#Definir variable cant hijos
cant_hijos = 0
list_2.append(cant_hijos)
print("Nombre, Apellido, Salario, Edad, Compañia, Bono final, Trabaja Actualmente, Hijos")
print(list_2)

if cant_hijos > 0 :
    bono_familiar = salario *0.08
    print("Obtiene el bono familiar el cuál es de: {}".format(bono_familiar))
    list_2.append(bono_familiar)
else :
    print("No cumple para obtener el bono familiar")
    list_2.append("sin bono")

print(" ")
#Mostrar lista final
print("La lista actualizada es: {}".format(list_2))
