"""Ejercicios para practicar el dia 5 de Python"""

# crear una funcion que reciba 3 numeros y se sumen si el valor es mayor a 15 devolver el numero mayor
# si es menos a 10 devolver el numero menor, si es entre 10 y 15 devolver el numero del medio

def devolver_distintos(num1 , num2 , num3):
    """devuelve el numero mayor, menor o del medio dependiendo de la suma de los 3 numeros"""
    suma = num1 + num2 + num3
    if suma > 15:
        return max(num1, num2, num3)
    elif suma < 10:
        return min(num1, num2, num3)
    else:
        return sorted([num1, num2, num3])[1]

print(devolver_distintos(6, 7, 8)) # mayor
print(devolver_distintos(2, 2, 1)) # menor
print(devolver_distintos(4, 5, 6)) # del medio

#funcion que reciba una palabra y devuelva todas sus letras unicas sin repetir
#en orden alfabetico por ejemplo si se le pasa "banana" devolver "abn"

def letras_unicas(palabra):
    """devuelve las letras unicas de una palabra en orden alfabetico"""
    letras = set(palabra)
    return ''.join(sorted(letras))

print(letras_unicas("entretenido")) # "abn"

# funcion que reciba muchos argumentos y devuelva true si el 0 se repite 2 veces seguidas, sino devuelve false
# ejemplo: si se le pasa 1, 0, 0, 2, 3 devuelve true, si se le pasa 1, 0, 1, 0, 2 devuelve false

def ceros_seguidos(*args):
    """devuelve true si el 0 se repite 2 veces seguidas, sino devuelve false"""
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False

print(ceros_seguidos(1, 0, 0, 2, 3)) # True
print(ceros_seguidos(1, 0, 1, 0, 2)) # False 

# funcion contar primos que reciba solo 1 argumento
# esta funcion muestra en pantalla todos los numeros primos que existen en el rango que va desde 0
#hasta el numero que se le paso como argumento incluido, y devuelve la cantidad de numeros primos encontrados
def contar_primos(n):
    """muestra en pantalla todos los numeros primos que existen en el rango que va desde 0 hasta n incluido, y devuelve la cantidad de numeros primos encontrados"""
    primos = []
    for num in range(2, n + 1):
        es_primo = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    print(f"Números primos hasta {n}: {primos}")
    return len(primos)

print(contar_primos(5000)) # 669
