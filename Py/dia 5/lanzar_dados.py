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

lista_numeros = [1,2,15,7,25,9,8,3,7,12,20]
def reducir_lista(lista_numeros):
    """la funcion debe reducir la lista eliminar los duplicados y el numero mayor"""
    lista_sin_duplicados = list(set(lista_numeros))
    numero_mayor = max(lista_sin_duplicados)
    lista_reducida = [n for n in lista_sin_duplicados if n != numero_mayor]
    return lista_reducida

def promedio(reducir_lista):
    """la funcion debe calcular el promedio de la lista reducida"""
    if len(reducir_lista) == 0:
        return 0
    return sum(reducir_lista) / len(reducir_lista)

def lanzar_moneda():
    """la funcion debe decir cara o cruz al azar"""
    return random.choice(["Cara", "Cruz"])
def probar_suerte(lanzar_moneda, lista_numeros):
    """si sale cara, la lista se auto destruira y se vaciara, si sale cruz la lista debe imprimirse en pantalla"""
    resultado = lanzar_moneda()
    if resultado == "Cara":
        lista_numeros.clear()
        return "La lista se autodestruirá"
    else:
        return "La lista fue salvada"