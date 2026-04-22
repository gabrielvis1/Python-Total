import random
import os

# 1. Optimización: Diccionario de constantes y ASCII Art en una Tupla (inmutable)
AHORCADO_ARTE = (
    """
       +---+
           |
           |
           |
          ===""", """
       +---+
       O   |
           |
           |
          ===""", """
       +---+
       O   |
       |   |
           |
          ===""", """
       +---+
       O   |
      /|   |
           |
          ===""", """
       +---+
       O   |
      /|\\  |
           |
          ===""", """
       +---+
       O   |
      /|\\  |
      /    |
          ===""", """
       +---+
       O   |
      /|\\  |
      / \\  |
          ==="""
)

def limpiar_pantalla():
    # Limpia la terminal según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def procesar_palabra(palabra):
    # Optimización: Usamos translate para quitar acentos de un tirón (más rápido que 5 replaces)
    trans = str.maketrans("ÁÉÍÓÚ", "AEIOU")
    return palabra.upper().translate(trans)

def obtener_palabra():
    palabras = ["COMPUTADORA", "PROGRAMACION", "BICICLETA", "CIUDAD", "ESTRELLA", "ESCRITORIO"]
    return procesar_palabra(random.choice(palabras))

def jugar():
    palabra_secreta = obtener_palabra()
    letras_vistas = set()
    errores = 0
    max_errores = len(AHORCADO_ARTE) - 1

    while errores < max_errores:
        limpiar_pantalla()
        print("=== ELVIS HANGMAN PRO ===")
        print(AHORCADO_ARTE[errores])
        
        # Generador de estado en una sola línea (List Comprehension)
        progreso = [l if l in letras_vistas else "_" for l in palabra_secreta]
        print(f"\nPalabra: {' '.join(progreso)}")
        print(f"Letras probadas: {' '.join(sorted(letras_vistas))}")

        # Condición de victoria instantánea
        if "_" not in progreso:
            print(f"\n¡GANASTE! La palabra era: {palabra_secreta}")
            break

        letra = input("\nIntroduce una letra: ").upper()

        if not letra.isalpha() or len(letra) != 1:
            continue
        
        if letra in letras_vistas:
            print("Ya la usaste, prestá atención.")
            continue

        letras_vistas.add(letra)

        if letra not in palabra_secreta:
            errores += 1
    else:
        limpiar_pantalla()
        print(AHORCADO_ARTE[max_errores])
        print(f"\n¡PERDISTE! El personaje de Elvis fue ahorcado. Era: {palabra_secreta}")

    if input("\n¿Otra vez? (s/n): ").lower() == 's':
        jugar()

if __name__ == "__main__":
    jugar()