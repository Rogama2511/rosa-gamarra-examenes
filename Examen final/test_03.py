"""3. Crear un programa usando decoradores para mostrar solo la hora
y el minuto del momento que se usa el decorador

Reglas:
- Al ejecutar el decorador mostrará un mensaje: “El decorador está siendo
ejecutado a las H con minutos”
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados usando el decorador implementado
con un mínimo tres ejemplos.
"""

from datetime import datetime


def func_decodaror(funcB):
    def funcC(*args, **kwargs):
        ahora = datetime.now()
        hora = ahora.hour
        minuto = ahora.minute
        print(f"El decorador está siendo ejecutado a las "
              f"{hora} con {minuto} minutos")

        suma = sum(args) + sum(kwargs.values())
        print(f"La suma total de valores es: {suma}")

        return funcB(*args, **kwargs)
    return funcC


@func_decodaror
def num_mayor(*args, **kwargs):
    valores = list(args) + list(kwargs.values())
    mayor = max(valores)
    print("El número mayor de los números ingresados "
          "es: {}".format(mayor))


# Tres Ejemplos
num_mayor(a=1, b=34, c=6, d=48, e=11, f=5)

print(" ")
num_mayor(10, 20, 5, a=47, b=189, c=32)

print(" ")
num_mayor(23, 40, 54, 85, 12, a=6, b=75, c=1)
