""" Funciones dinámicas en Python """
def chequear_3_cifras(numero):
    return numero in range(100, 1000)
resultado1 = chequear_3_cifras(123)  # True
resultado2 = chequear_3_cifras(99)   # False

print(resultado1)
print(resultado2)

def chequear_4_cifras(numero1, numero2):
    suma = numero1 + numero2
    return suma in range(1000, 10000)

resultado3 = chequear_4_cifras(500, 600)  # True
resultado4 = chequear_4_cifras(100, 200)  # False
print(resultado3)
print(resultado4)

mi_lista = [1, 2, 10, 12, 15]
def chequear_en_lista(lista):
    for l in lista:
        if l in range(3, 10):
            return True
    return False
resultado5 = chequear_en_lista(mi_lista)  # True
print(f"resultado5: {resultado5}")

mi_lista2 = [25, 300, 38, 4000, 589, 10000, 456, 789, 9999]
def devolver_numeros_3_cifras(lista):
    numeros_3_cifras = []
    for numero in lista:
        if numero in range(100, 1000):
            numeros_3_cifras.append(numero)
    lista_ordenada = sorted(numeros_3_cifras)
    return lista_ordenada
resultado6 = devolver_numeros_3_cifras(mi_lista2)  # [300, 456, 789]
print(f"resultado6: {resultado6}")
