"""Juego de adivinar el número de Elvis """
import random
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}, vamos a jugar a adivinar el número de Elvis")
print(f"{nombre}, tienes 8 intentos para adivinar el número de Elvis, que está entre 1 y 100")
numero_random = random.randint(1, 100)
intentos = 8
intentos_usados = 0
while intentos > 0:
    numero_usuario = int(input("Introduce un número entre 1 y 100: "))
    intentos_usados += 1
    if numero_usuario < 1 or numero_usuario > 100:
        print("Por favor, introduce un número válido entre 1 y 100")
    elif numero_usuario < numero_random:
        print("El número secreto es mayor que tu número")
    elif numero_usuario > numero_random:
        print("El número secreto es menor que tu número")
    else:
        print(f"¡Felicidades {nombre}! Has adivinado el número secreto en {intentos_usados} intentos")
        break
    intentos -= 1
    print(f"Te quedan {intentos} intentos")
else:
    print(f"Lo siento {nombre}, has agotado tus intentos. El número secreto era {numero_random}")
    