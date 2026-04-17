"""
Ejemplo de control de flujo con if, elif y else.
"""

# Definimos una variable numérica para comparar 
puntaje = 50

if puntaje >= 90:
    # Se ejecuta si puntaje es mayor o igual a 90 
    print("Calificación: Excelente")
elif puntaje >= 70:
    # Se ejecuta si lo anterior fue falso PERO es mayor o igual a 70
    print("Calificación: Aprobado")
else:
    # Se ejecuta si ninguna de las condiciones anteriores fue True 
    print("Calificación: Reprobado")

# Ejemplo usando operadores lógicos [cite: 494]
asistencia = True

if puntaje >= 70 and asistencia:
    # Ambas condiciones deben ser True para entrar aquí 
    print("Resultado final: Promocionado")