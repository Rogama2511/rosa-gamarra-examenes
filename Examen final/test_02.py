"""2. Crear un decorador conteo.

Reglas:
- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente.
- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada.
- La función que vas a crear va a capturar, la edad, nombre, hora y minuto en
que fue registrado la persona (usar la librería correspondiente)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”
- La que función que será decorada calculará la media de 4 notas.
"""

from datetime import datetime


def conteodecodador(funcB):
    def funcC(*args, **kwargs):
        arg_total = len(args) + len(kwargs)
        if arg_total <= 1:
            print("Se requiere más de un parametro para ejecutar")
        else:
            resultado = funcB(*args, **kwargs)
            print("La función fue ejecutada")
            return resultado
    return funcC


@conteodecodador
def registro(nombre, edad, **kwargs):
    ahora = datetime.now()
    hora = ahora.hour
    minuto = ahora.minute

    print(f"{nombre} de {edad} años ha sido registrado a las "
          f"{hora} horas con {minuto} minutos")

    notas = kwargs.values()
    media = sum(notas) / len(notas)
    print("El promedio de las notas es: {}".format(media))
    return media


# Registrar persona
registro("Rosa", 20, nota1=15, nota2=18, nota3=20, nota4=17)
