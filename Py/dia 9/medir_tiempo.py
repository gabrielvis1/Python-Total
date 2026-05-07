"""medir tiempo"""
import timeit
import time

def prueba_for(numero):
    """Crea una lista desde 1 hasta 'numero' usando un bucle for."""
    mi_lista = []

    # Recorremos desde el 1 hasta el número indicado (inclusive)
    for i in range(1, numero + 1):
        mi_lista.append(i)

    return mi_lista

# Ejemplo de uso:
# print(prueba_for(5))  # Resultado: [1, 2, 3, 4, 5]

def prueba_while(numero):
    """Crea una lista desde 1 hasta 'numero' usando un bucle while."""
    mi_lista = []
    i = 1  # Iniciamos nuestro contador en 1
    # Mientras 'i' sea menor o igual al número indicado...
    while i <= numero:
        mi_lista.append(i)
        i += 1  # ¡Importante! Aumentamos el contador en 1 en cada vuelta

    return mi_lista

# Ejemplo de uso:
# print(prueba_while(5))  # Resultado: [1, 2, 3, 4, 5]
inicio = time.time()
prueba_for(1000)
final = time.time()
print(final-inicio)

inicio2 = time.time()
prueba_while(1000)
final2 = time.time()
print(final2-inicio2)

# 1. Definimos los fragmentos de código como TEXTO (strings)
codigo_con_for = """
mi_lista = []
for i in range(1000):
    mi_lista.append(i)
"""

codigo_comprension = """
mi_lista = [i for i in range(1000)]
"""

print("Midiendo la velocidad... (esto tomará un segundito)\n")

# 2. Usamos timeit.timeit() para medir
# stmt: El código que queremos evaluar.
# number: La cantidad de veces que lo va a ejecutar para sacar el promedio.

tiempo_for = timeit.timeit(stmt=codigo_con_for, number=10000)
tiempo_comprension = timeit.timeit(stmt=codigo_comprension, number=10000)

# 3. Mostramos los resultados
print(f"Tiempo usando bucle FOR:      {tiempo_for:.4f} segundos")
print(f"Tiempo usando COMPRENSIÓN:    {tiempo_comprension:.4f} segundos")

if tiempo_comprension < tiempo_for:
    print("\n🏆 ¡La comprensión de listas es la ganadora!")

def contar_numeros():
    total = 0
    for i in range(1000):
        total += i
    return total

# Le decimos a timeit que ejecute la función "contar_numeros()" 10,000 veces
# globals=globals() le da permiso a timeit para ver las funciones de este archivo
tiempo_funcion = timeit.timeit("contar_numeros()", globals=globals(), number=10000)

print(f"La función tardó {tiempo_funcion:.4f} segundos en ejecutarse 10,000 veces.")
