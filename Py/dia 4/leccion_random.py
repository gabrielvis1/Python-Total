"""Demostración de la importación de módulos. Y la función random para generar aleatorios. """
from random import *

aleatorio_randint = randint(1, 100)  # Genera un número aleatorio entre 1 y 100
print(f"El número aleatorio generado es: {aleatorio_randint}")

aleatorio_uniform = round(uniform(1.0, 100.0),2)  # Genera un número aleatorio de punto flotante entre 1.0 y 100.0
print(f"El número aleatorio de punto flotante generado es: {aleatorio_uniform}")

aleatorio_ramdom = random()  # Genera un número aleatorio de punto flotante entre 0.0 y 1.0
print(f"El número aleatorio entre 0.0 y 1.0 generado es: {aleatorio_ramdom}")

colores = ["rojo", "verde", "azul", "amarillo", "naranja", "morado", "rosa", "negro", "blanco", "gris"]
aleatorio_choice = choice(colores)  # Selecciona un elemento aleatorio de la lista de colores
print(f"El color aleatorio seleccionado es: {aleatorio_choice}")

numeros = list(range(1, 101))  # Crea una lista de números del 1 al 100
aleatorio_sample = sample(numeros, 5)  # Selecciona 5 números aleatorios de la lista sin repetición
print(f"Los números aleatorios seleccionados son: {aleatorio_sample}")

numerosx = list(range(1, 101))  # Crea una lista de números del 1 al 100
aleatorio_shuffle = numerosx.copy()  # Copia la lista para mezclarla sin modificar la original
shuffle(aleatorio_shuffle)  # Mezcla la lista de números aleatoriamente
print(f"Los números aleatorios mezclados son: {aleatorio_shuffle}")
