""" aprendiendo a usar kwargs """
def suma(**kwargs):
    print(type(kwargs))

suma(a=1, b=2, c=3)

def suma_kwargs(**kwargs):
    total=0
    for clave, valor in kwargs.items():
        total += valor
        print(f"{clave} = {valor}")
    return total

print(suma_kwargs(a=1, b=2, c=3))

def prueba(num1, num2, *args, **kwargs):
    """mostrar todos los argumentos en consola por tipo y contenidos"""
    print(f"mi primer numero es tipo {type(num1)} y su valor es {num1}")
    print(f"mi segundo numero es tipo {type(num2)} y su valor es {num2}")
    print(f"mis argumentos son tipo {type(args)} y su valor es {args}")
    print(f"mis argumentos con clave son tipo {type(kwargs)} y su valor es {kwargs}")

lista_args = [3, 4, 5]
dic_kwargs = {"a": 6, "b": 7, "c": 8}
prueba(1, 2, *lista_args, **dic_kwargs)

def cantidad_atributos(**kwargs):
    """cuenta la cantidad de atributos que se le pasan a la función"""
    return len(kwargs)

def lista_atributos(**kwargs):
    """devuelve una lista con los nombres de los atributos que se le pasan a la función"""
    return list(kwargs.values())

def describir_persona(nombre, **kwargs):
    """imprime el nombre y sus atributos como características de la persona"""
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")