"""Lista de todos los numeros positivos"""

lista_numeros = [50 ,-5, 0, 100, -20, 25, 75, -10, 200]

def todos_positivos(lista_numeros):
    """ Devuelve false si hay un numero negativo y true si todos los numeros son positivos """
    for numero in lista_numeros:
        if numero < 0:
            return False
    return True
