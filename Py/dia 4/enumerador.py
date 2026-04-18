# 1. Creamos la lista de 5 letras
letras = ['a', 'b', 'c', 'd', 'e']

for indice in letras:
    print(indice)

# 2. Usamos el bucle for con enumerate
# 'indice' guardará la posición (0, 1, 2...)
# 'letra' guardará el valor ('a', 'b', 'c'...)
for indice, letra in enumerate(letras):
    print(f"En el índice {indice+1} se encuentra la letra: {letra}")

for indice, letra in enumerate(letras, start=1):
    print(f"Letra número {indice}: {letra}")
    
for indice, item in enumerate(range(45,70)):
    print(f"En el índice {indice+1} se encuentra el valor: {item}")

mis_elementos = list(enumerate(letras))
print(mis_elementos)
print(f"Primer elemento: {mis_elementos[3]}")
print(f"Último elemento: {mis_elementos[0][1]}")
