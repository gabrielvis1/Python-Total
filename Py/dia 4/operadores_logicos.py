# Definimos dos comparaciones
a = 6 > 5           # Esto es True [cite: 495]
b = 30 == 15 * 3    # Esto es False (porque 15*3 es 45) [cite: 496]

# Evaluación con 'and'
print(a and b)      # >> False (True y False resulta en False) 

# Evaluación con 'or'
print(a or b)       # >> True (Al menos una es verdadera) [cite: 504, 506]

# Evaluación con 'not'
print(not a)        # >> False (Invierte el True de 'a') [cite: 510, 511]