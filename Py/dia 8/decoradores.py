""" ejemplo de decoradores """
def decorar_saludo(funcion):
    """funcion decorador"""
    def otra_funcion(palabra):
        print("Hola!!")
        funcion(palabra)
        print("Adios :(")
    return otra_funcion

def mayuscula(texto):
    """funcion saluda y devuelve mayuscula """
    print(texto.upper())

def minuscula(texto):
    """funcion saluda y devuelve minuscula """
    print(texto.lower())

def una_funcion(funcion):
    """funcion que devuelve una funcion """
    return funcion

mi_funcion = mayuscula
mi_funcion("hola mundo")
una_funcion(minuscula("chao mundo"))

def cambiar_letras(tipo):
    """funcion de funciones"""
    def may(texto):
        print(texto.upper())
    def minu(texto):
        print(texto.lowe())
    if tipo == "may":
        return may
    elif tipo == "min":
        return minu

operacion = cambiar_letras("may")
operacion("palabra")

mayuscula_decorada = decorar_saludo(mayuscula)
minuscula_decorara = decorar_saludo(minuscula)



mayuscula_decorada("Alegria pero con anemia")
