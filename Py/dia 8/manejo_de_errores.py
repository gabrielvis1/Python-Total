def cuadrado():
    numero = int(input("ingresa un numero para hacerlo cuadrado "))
    resultado = numero * numero
    print(f"El cuadrado de {numero} es {resultado} ")
    print("muchas gracias por participar")


try:
    # el codigo que puede fallar (o no)
    cuadrado()
except ValueError: # SE CAPTURA AL ERROR DEPENDIENDO DEL TYPO DE ERROR PUEDES TENER CUANTOS QUIERAS
    # El codigo que se debe ejecutarse si falla
    print("Upss ocurrio un error intentalo de nuevo")
else:
    # El codigo a ejecutar si no falla
    print("El cuadrado ocurrio perfectamente")
finally:
    # El codigo a ejecutar de todos modos
    print("Eso es todo amigo")
