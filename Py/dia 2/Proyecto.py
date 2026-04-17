""" este es un programa para calcular comision de venta del 13%"""
# 1. Pedimos los datos al usuario
nombre = input("Por favor, ingresa tu nombre: ")
ventas_mensuales = float(input("¿Cuánto has vendido este mes? "))

# 2. Calculamos la comisión (13% = 0.13)
# Usamos el operador * para la multiplicación
comision = ventas_mensuales * 0.13

# 3. Redondeamos el resultado a 2 decimales para que parezca dinero real [cite: 49, 51]
comision_final = round(comision, 2)

# 4. Mostramos el mensaje final usando f-strings para que sea fácil de leer [cite: 25]
print(f"ok {nombre}. este mes vendiste {ventas_mensuales} por eso ganaste en comisiones {comision_final}")