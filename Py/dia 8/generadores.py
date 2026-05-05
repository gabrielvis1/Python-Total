""" Ejemplos de generadores """
def mi_funcion():
    """funcion devuelve 4"""
    lista = []
    for x in range(1,5):
        lista.append(x*10)
    return lista

#ejemplo de generador
def mi_generador():
    """ funcion que devuelve 4 con un generador """
    for x in range(1,10):
        yield x * 10

print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

def mi_generador2():
    """funcion que continua cuando pedimos el siguiente parametro"""
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x
    x += 1
    yield x

g = mi_generador2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

def secuencia_infinita():
    """Genera una secuencia infinita de números a partir del 1."""
    n = 1
    while True:
        yield n
        n += 1

# Almacenamos el generador en la variable solicitada
generador = secuencia_infinita()

print(next(generador)) # Entrega el 1 y se pausa
print(next(generador)) # Retoma, suma 1, entrega el 2 y se pausa
print(next(generador)) # Retoma, suma 1, entrega el 3 y se pausa...

def contador_vidas():
    """Generador que simula perder vidas en un juego paso a paso."""
    yield "Te quedan 3 vidas"
    yield "Te quedan 2 vidas"
    yield "Te queda 1 vida"
    yield "Game Over"

# Almacenamos el generador en la variable solicitada
perder_vida = contador_vidas()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
