"""Practica de interaccion con funciones"""
import random

# crear funcion que arroje dos dados al azar y devuelva sus resultados
# la funcion debe debolver dos resultados entre 1 y 6

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    """la funcion debe evaluar la jugada sumada y devolver si es menor a 6, 
    entre 6 y 10, o mayor a 10"""
    suma_dados = dado1 + dado2
    if suma_dados < 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 <= suma_dados <= 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

print("Bienvenido al juego de los dados!")
dado1, dado2 = lanzar_dados()
resultado = evaluar_jugada(dado1, dado2)
print(f"Has lanzado los dados y obtuviste {dado1} y {dado2}.")
print(resultado)

