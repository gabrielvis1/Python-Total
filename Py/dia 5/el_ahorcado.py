"""ESTE ES EL JUEGO DEL AHORCADO, EN EL CUAL EL USUARIO DEBE ADIVINAR UNA PALABRA SECRETA, LETRA POR LETRA, ANTES DE QUE SE COMPLETE EL DIBUJO DEL AHORCADO."""
import random

def obtener_palabra_secreta():
    """Esta función selecciona una palabra secreta al azar de una lista predefinida."""
    # la palabra va toda en mayuscula para facilitar la comparacion y sin acentos para evitar problemas de entrada
    palabras = ["Perro","Barco","Lampara","Gato","Casa","Computadora",
                "Montaña","Reloj","Avión","Libro","Teléfono","Coche",
                "Bicicleta","Árbol","Flor","Silla","Mesa","Puerta","Ventana","Cielo","Mar",
                "Sol","Luna","Estrella","Nube","Río","Bosque","Playa","Isla","Ciudad","Campo"]
    return random.choice(palabras).upper().replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")

def pedir_letra():
    """Esta función solicita al usuario que ingrese una letra y valida la entrada."""
    while True:
        letra = input("Ingresa una letra: ").upper()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("Entrada inválida. Por favor, ingresa una sola letra.")

def volver_a_jugar():
    """Esta función pregunta al usuario si desea volver a jugar."""
    while True:
        respuesta = input("¿Quieres volver a jugar? (s/n): ").lower()
        if respuesta in ['s', 'n']:
            return respuesta == 's'
        else:
            print("Entrada inválida. Por favor, ingresa 's' para sí o 'n' para no.")

def juego_ahorcado():
    """Esta función contiene la lógica principal del juego del ahorcado."""
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = set()
    intentos_restantes = 6
    letras_incorrectas = set()

    print("¡Bienvenido al juego del Ahorcado!")
    print("Adivina la palabra secreta letra por letra.")
    
    while intentos_restantes > 0:
        # Mostrar el estado actual de la palabra
        estado_palabra = " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta])
        print(f"Palabra: {estado_palabra}")
        print(f"Vidas restantes: {intentos_restantes}")
        print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")

        letra = pedir_letra()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.add(letra)

        if letra in palabra_secreta:
            print("¡Correcto!")
            if all(letra in letras_adivinadas for letra in palabra_secreta):
                print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
                if not volver_a_jugar():
                    break
                else:
                    juego_ahorcado()
                    break
        else:
            print("¡Incorrecto!")
            letras_incorrectas.add(letra)
            intentos_restantes -= 1

    if intentos_restantes == 0:
        print(f"¡Has perdido! La palabra secreta era: {palabra_secreta}")
        print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")
        if volver_a_jugar():
            juego_ahorcado()


if __name__ == "__main__":    juego_ahorcado()
