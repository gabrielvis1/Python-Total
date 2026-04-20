""" Ejemplo de compresión de listas """

palabra = "compresion"
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

palabra1 = "compresion"
lista1 = [letra for letra in palabra1]
print(lista1)

lista2 = [ n for n in range(0,31,3)]
print(lista2)

lista3 = [ n * 2 for n in range(0,11)]
print(lista3)

lista4 = [ n for n in range(0,11) if n * 2 > 5]
print(lista4)

lista5 = [ n if n * 2 > 5 else "NO" for n in range(0,11)]
print(lista5)

pies = [10, 20, 30, 40, 50]
metros = [pie * 0.3048 for pie in pies]
print(metros)
