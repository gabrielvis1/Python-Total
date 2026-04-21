"""Suma en una funcion con muchos argumentos"""

def suma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(suma(1, 2, 3, 4, 5, 9, 10, 20))  # Output: 54

def suma_mejor(*args):
    return sum(args)

print(suma_mejor(1, 2, 3, 4, 5, 9, 10, 20))  # Output: 54

def suma_cuadrados(*args):
    total = 0
    for numero in args:
        total += numero ** 2
    return total

print(suma_cuadrados(1, 2, 3))  # Output: 55

def suma_absolutos(*args):
    """suma los valores de absolutos hasta los negativos"""
    total = 0
    for n in args:
        total += abs(n)
    return total

print(suma_absolutos(-1, -2, 3, 4))  # Output: 10

def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    return f"{nombre}, la suma de tus números es {suma_numeros}"
