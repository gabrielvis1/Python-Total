""" interacción entre funciones """
from random import shuffle
# lista inicial de palitos 
palitos = ["-", "--", "---", "----", "-----"]
# mezclar los palitos
def mezclar_palitos(lista):
    """ Mezcla los palitos de forma aleatoria """
    shuffle(lista)
    return lista
# pedir al usuario que adivine el orden de los palitos
def probar_suerte():
    """intenta adivinar el palito más largo"""
    intento = ""
    intento = input("Elige un número del 1 al 5: ")
    while intento not in ["1", "2", "3", "4", "5"]:
        intento = input("Elige un número del 1 al 5: ")
    return int(intento)
# comprobar el resultado y mostrar un mensaje al usuario
def chequear_intento(lista, intento):
    """Comprueba si el intento es correcto"""
    seleccion = intento - 1
    if lista[seleccion] == "-----":
        print("¡Correcto! Has adivinado el palito más largo.")
    else:
        print(f"Incorrecto. El palito más largo era: {lista.index('-----') + 1}")

palitos_mezclados = mezclar_palitos(palitos)
numero_elegido = probar_suerte()
chequear_intento(palitos_mezclados, numero_elegido)
