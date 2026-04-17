tabla = 5

for n in range(5):
    print(n)

print(f"--- Tabla del {tabla} ---")

# Empezamos en 1 y terminamos en 11 (para que incluya el 10)
for numero in range(1, 11):
    resultado = tabla * numero
    print(f"{tabla} x {numero} = {resultado}")

print("Números pares del 2 al 20:")

# Empieza en 2, termina antes de 21, salta de 2 en 2
for par in range(2, 21, 2):
    print(par)

ventas = [100, 150, 200, 50, 300, 400]

for i in range(0, len(ventas), 2):
    # Sumamos el día actual y el siguiente
    print(len(ventas))
    parcial = ventas[i] + ventas[i+1]
    print(f"Suma del bloque de dos días (desde índice {i}): {parcial}")

# El límite superior debe ser 10000 para que incluya el 9999
mi_lista = list(range(1, 10000))

# Verificación
print(mi_lista)
print(f"Primer elemento: {mi_lista[0]}")
print(f"Último elemento: {mi_lista[-1]}")
print(f"Longitud total: {len(mi_lista)}")

mi_lista = [n for n in range(2500,2586)]