"""Práctica n°2 - Python Módulo I"""

"""Ejercicio 3 - Gestión Billetera
Reglas:
- El programa deberá considerar 2 cuentas bancarias para el constructor: 
1 en soles y otra en dólares. Considerar el nombre y apellido del titular
- Deberá tener un método para transferir entre sus cuentas, pero para 
realizar esto debe hacer una conversión de monedas.
- Tendrá otro método para retirar dinero, esto debe actualizar ambas cuentas 
y mostrar en pantalla los montos actualizados, a su vez validar si tiene 
fondos suficientes o no para el retiro, mostrar un mensaje que indique no 
tiene suficientes en caso fuera el caso.
- Instanciar 3 veces los casos de transferencias para ver reflejado el uso 
de tus métodos creados.
"""

class Billetera:
    def __init__(self, nombre, apellido, cuenta_soles, cuenta_dolares):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta_soles = cuenta_soles
        self.cuenta_dolares = cuenta_dolares

    def conversion(self):
        self.cuenta_dolares = self.cuenta_soles * 3.48

    def transferencia_cuenta(self, monto):
        print("Seleccione el tipo de transferencia ")
        opcion = input("(a) De soles a dolares (b) De dólares a soles: ")
        if opcion == "a":
            if monto > self.cuenta_soles:
                print("Salso insuficiente")
            else:
                self.cuenta_dolares += monto * 3.48
                self.cuenta_soles -= monto
                print("Transferencia de S/. {} a cuenta en dólares realizada".format(monto))
                print("Cuenta soles actualizada: S/. {}".format(self.cuenta_soles))
                print("Cuenta dolares actualizada: S/. {}".format(self.cuenta_dolares))
        elif opcion == "b":
            if monto > self.cuenta_dolares:
                print("Salso insuficiente")
            else:
                self.cuenta_dolares -= monto
                self.cuenta_soles += monto/3.48
                print("Transferencia de $/. {} a cuenta en soles realizada".format(monto))
                print("Cuenta soles actualizada: S/. {}".format(self.cuenta_soles))
                print("Cuenta dolares actualizada: S/. {}".format(self.cuenta_dolares))
        else:
            print("Ingrese una opción valida, por favor")

    def retirar(self, monto):
        print("Seleccione la cuenta de la que quiere realizar el retiro:")
        opcion = input("(a) Cuenta en SOLES (b) Cuenta en dolares: ")
        if opcion == "a":
            if monto > self.cuenta_soles:
                print("No tiene fondos suficientes para retirar")
            else:
                self.cuenta_soles -= monto
                print("Retiro realizado de s/.{}".format(monto))
                print("Saldo de cuenta en soles actualizada S/.{}".format(self.cuenta_soles))
        elif opcion == "b":
            if monto > self.cuenta_dolares:
                print("No tiene fondos suficientes para retirar")
            else:
                self.cuenta_dolares -= monto
                print("Retiro realizado de s/.{}".format(monto))
                print("Saldo de cuenta en dolares actualizada $/.{}".format(self.cuenta_dolares))
        else:
            print("Ingrese una opción valida, por favor")

#Intanciamos 1 persona
persona_1 = Billetera("Rosa", "Gamarra", 1000, 0)
persona_2 = Billetera("Maria", "Espinoza", 540, 0)
persona_3 =Billetera("Luciano", "Lopez", 255, 0)

persona_1.conversion()
persona_1.conversion()
persona_2.conversion()

print("Saldos iniciales: {}".format(persona_1.nombre))
print("Cuenta en soles:{}".format(persona_1.cuenta_soles))
print("Cuenta en dolares: {}".format(persona_1.cuenta_dolares))

print("Saldos iniciales: {}".format(persona_2.nombre))
print("Cuenta en soles:{}".format(persona_2.cuenta_soles))
print("Cuenta en dolares: {}".format(persona_2.cuenta_dolares))

print(" ")
#Transferencias entre cuentas
persona_1.transferencia_cuenta(300)
persona_2.transferencia_cuenta(250)
persona_3.transferencia_cuenta(150)

#Retirar
persona_3.retirar(150)
persona_1.retirar(240)

