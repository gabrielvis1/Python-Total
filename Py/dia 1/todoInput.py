# ==========================================
# GUÍA MAESTRA DE INPUT() - REFERENCIA RÁPIDA
# ==========================================

# 1. EL "HOLA MUNDO" INTERACTIVO
print("--- 1. BÁSICO ---")
# El espacio al final del texto es para que el cursor no quede pegado
nombre = input("¿Cómo te llamas? ") 
print("¡Hola,", nombre + "!")


# 2. EL TRUCO DEL TEXTO (La trampa del string)
print("\n--- 2. TODO ES TEXTO ---")
# Aunque escribas un número, Python lo ve como "texto"
edad_texto = input("Ingresa tu edad: ")
print("El tipo de dato es:", type(edad_texto)) # Verás que dice <class 'str'>


# 3. CONVERSIÓN A NÚMEROS (Cálculos)
print("\n--- 3. CONVERSIÓN ---")
# Usamos int() para números enteros y float() para decimales
num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa otro número entero: "))
print("La suma real es:", num1 + num2)

precio = float(input("Ingresa el precio del producto: "))
print("Precio con 21% de IVA:", precio * 1.21)


# 4. EJEMPLO PRÁCTICO: CALCULADORA DE EDAD
print("\n--- 4. CALCULADORA DE EDAD ---")
# Como estamos en el año 2026, restamos el nacimiento a este año
nacimiento = int(input("¿En qué año naciste? "))
print("Tu edad actual es:", 2026 - nacimiento)


# 5. EJEMPLO PRÁCTICO: ÁREA DE UN RECTÁNGULO
print("\n--- 5. CÁLCULO DE ÁREA ---")
base = float(input("Base del rectángulo: "))
altura = float(input("Altura del rectángulo: "))
print("El área total es:", base * altura)

print("\n--- FIN DE LA GUÍA INTERACTIVA ---")