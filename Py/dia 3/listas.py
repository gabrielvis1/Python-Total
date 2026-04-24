# Definición de listas de lenguajes
lenguajes_1 = ["C", "C++", "Python", "Java"]
lenguajes_2 = ["PHP", "SQL", "Visual Basic"]

# 1. Concatenación y Longitud
total_lenguajes = lenguajes_1 + lenguajes_2
print(f"Total de lenguajes: {len(total_lenguajes)}") # [cite: 290, 293]

# 2. Agregar y quitar elementos
lenguajes_1.append("R") # Agregamos al final [cite: 301]
quitado = lenguajes_1.pop(1) # Quitamos "C++" [cite: 306]
print(f"Quitamos: {quitado}")
print(f"Lista actualizada: {lenguajes_1}")

# 3. Ordenamiento
letras = ["d", "a", "c", "b", "e"]
letras.sort() # Ordena de A a Z [cite: 309]
print(f"Letras ordenadas: {letras}")

numeros = [5, 4, 7, 1, 9]
numeros.reverse() # Invierte el orden actual [cite: 313]
print(f"Números invertidos: {numeros}")

# imprimir indice de cada lugar en la lista
for indice, lenguaje in enumerate(total_lenguajes):
    print(f"{indice}: {lenguaje}")
    