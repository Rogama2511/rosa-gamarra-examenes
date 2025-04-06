"""Práctica n°2 - Python Módulo I"""

"""Ejercicio 2 - Herencia y encapsulación
Reglas:
- Crear una clase llamada Persona y agregar un atributo saldo a esta clase 
(ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual 
que tiene la persona) para la clase mencionada
- El método transferencia hace que la clase Empleado que llame al método 
pueda transferir la cantidad monto al objeto Empleado2 por consiguiente 
deberá ir actualizando también el saldo o monto que tiene el otro empleado 
en su cuenta cada vez que use el método transferencia
- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e 
imprimir “Saldo insuficiente”. Comprobar instanciado la clase realizando una 
transferencia y con dos personas.
"""

#Clase empleado
class Empleado:
    nacionalidad = "Peruana"
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def solicitar_nombre(self):
        nombre = input("Ingrese el nombre: ")
        self.nombre = nombre
        return "Nombre: {}".format(self.nombre)

    def solicitar_edad(self):
        edad = int(input("Ingrese el edad: "))
        self.edad = edad
        return "Edad es actual: {}".format(self.edad)

    def cumple(self):
        self.edad = self.edad + 1
        return "Edad aumentada: {}".format(self.edad)

    def aumentoSueldo(self):
        self.sueldo = self.sueldo + self.sueldo * 0.3
        return "Sueldo incrementado es: {}".format(self.sueldo)

    def cumplea_20xx(self, year, edad_new):
        if edad_new < self.edad:
            return print("No es posible realizar la operación")
        else:
            return print(f"En el año {year} tendra {edad_new} años")

class Persona(Empleado):
    def __init__(self, nombre, edad, sueldo, saldo):
        super().__init__(nombre, edad, sueldo)
        self.__saldo = saldo

    def mostrar_saldo(self):
        return "{} tiene un saldo actual de S/.{}".format(self.nombre, self.__saldo)

    def modificar_saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo

    def transferencia(self, persona ,monto):
        if monto <= self.__saldo:
            monto_transferido = self.__saldo - monto
            self.modificar_saldo(monto_transferido)
            print("Transferencia exitosa: S/. {}".format(monto))
            monto_recibido =  persona.__saldo + monto
            persona.modificar_saldo(monto_recibido)
            print("Saldo de {} es de s/. {}" .format(self.nombre, self.__saldo))
            print("Saldo de {} es de s/: {}".format(persona.nombre, persona.__saldo))
        else:
            print("Saldo insuficiente")


#Transferencia entre dos personas
persona_1 = Persona(" ", 0, 1500, 550)
persona_2 = Persona(" ", 0, 1450, 200)


#Solicitar datos
print(persona_1.solicitar_nombre())
print(persona_2.solicitar_nombre())
print(" ")

#Transferencia saldo suficiente
persona_1.transferencia(persona_2, 50)
persona_2.transferencia(persona_1, 70)
print(" ")

#Tranferencia con saldo insuficiente
persona_2.transferencia(persona_1, 500)
