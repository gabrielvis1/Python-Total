""" Ejemplo de función """

lista_cafe = [("capuchino", 2.5), ("latte", 3.0), ("americano", 2.0), ("espresso", 1.5), ("mocha", 3.5)]
for elemento in lista_cafe:
    print(elemento)

for c, p in lista_cafe:
    print(f"El café {c} cuesta {p} euros")

def cafe_mas_caro(lista):
    """ Devuelve el café más caro de la lista """
    cafe, precio = lista[0]
    for c, p in lista:
        if p > precio:
            cafe, precio = c, p
    return (cafe, precio)
cafe, precio = cafe_mas_caro(lista_cafe)

print(f"El café más caro es {cafe} y cuesta {precio} euros")
