"""Práctica n°2 - Python Módulo I"""

"""Ejercicio 1 - Clases

Reglas:
- Crear una clase llamada Empleado donde sus atributos deben ser nombre, edad, 
sueldo y de nacionalidad peruana, tendrá un método para solicitar su nombre y 
otro para solicitar su edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en un año la
 edad de la persona.
- Crear la instancia de la clase Persona y usar su nuevo método aumentoSueldo para 
incrementar su sueldo en un 30% (mínimo instanciar la clase 2 veces, mostrar por 
pantalla dicho sueldo ya incrementado).
- Crear un siguiente método que retorne un mensaje donde indique que: “En el año 
2025 tendrá XX años”, el año se ingresará por parámetro y la edad es la edad que 
ya se ingresó (Mostrar por pantalla este valor)
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

#Instanciar uns persona
persona_1 = Empleado(" ",0, 1500 )
persona_2 = Empleado(" ",  0, 2000 )

print("Datos primera persona")
print(persona_1.solicitar_nombre())
print(persona_1.solicitar_edad())

#Aumento de sueldo
print("Sueldo actual: {}".format(persona_1.sueldo))
persona_1.aumentoSueldo()
persona_1.aumentoSueldo()
print("Sueldo incrementado: {}".format(persona_1.sueldo))

persona_1.cumplea_20xx(2025, 22)

print(" ")

print("Datos segunda persona")
print(persona_2.solicitar_nombre())
print(persona_2.solicitar_edad())
print(persona_2.cumple())
print(persona_2.aumentoSueldo())
persona_2.cumplea_20xx(2026, 19)
