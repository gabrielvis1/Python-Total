"""Leccion para limpiar la consola"""
from os import system

nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad? ")
system("cls")  # Para Windows
print(f"Hola {nombre}, tienes {edad} años.")
