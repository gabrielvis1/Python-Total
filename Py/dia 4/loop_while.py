"""
Ejemplo de Loop While: Restando hasta salir.
"""

# 1. Creamos la variable con un valor inicial (x)
x = 10

# 2. El loop se ejecutará MIENTRAS x sea mayor que 0
# Usamos el operador de comparación '>' que devuelve un booleano [cite: 176, 178]
while x > 0:
    print(f"El valor actual es: {x}")
    
    # 3. Restamos 1 a la cantidad en cada vuelta
    # Esto es fundamental para que la condición eventualmente sea False [cite: 130-131]
    x = x - 1

# 4. Mensaje al salir del bucle
print("El valor llegó a 0. ¡Bucle terminado!")

# 1. Inicializamos la variable con 'si' para que la primera condición sea True
respuesta = "s"

# 2. El bucle se ejecuta MIENTRAS la respuesta no sea 'no'
while respuesta != "n":
    # El código que quieres repetir va aquí
    print("El programa sigue ejecutándose...")
    # 3. Preguntamos al usuario y usamos .lower() para evitar errores de mayúsculas
    respuesta = input("¿Deseas continuar? (s/n): ").lower()

# 4. Mensaje final al salir del bucle
print("Has salido del programa con éxito.")
# 1. Pedimos el texto al usuario
texto = input("Ingresa un texto para analizar: ")
letra_objetivo = "p"

print(f"\nAnalizando el texto buscando la letra '{letra_objetivo}':")

for letra in texto:
    if letra == letra_objetivo:
        # 1. BREAK: Detiene el bucle por completo
        print(f"\n[BREAK] ¡Encontré la '{letra_objetivo}'! Deteniendo el programa.")
        break 
    
    if letra == " ":
        # 2. CONTINUE: Salta esta vuelta y sigue con la siguiente
        # (En este caso, no imprimirá los espacios)
        continue 
        
    if letra == "x":
        # 3. PASS: No hace nada, es solo un marcador de posición
        # Útil cuando planeás agregar código después pero no querés errores ahora
        pass 

    print(f"Letra procesada: {letra}")

print("\n--- Fin del análisis ---")
