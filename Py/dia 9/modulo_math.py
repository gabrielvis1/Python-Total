"""
Archivo: ejemplos_math.py
20 ejemplos prácticos utilizando el módulo 'math' de Python.
"""

import math

print("--- 🌟 CONSTANTES MATEMÁTICAS ---")
# 1. math.pi (Número Pi)
print("1. Pi:", math.pi)

# 2. math.e (Número de Euler)
print("2. Euler:", math.e)


print("\n--- 📏 REDONDEO Y VALOR ABSOLUTO ---")
# 3. math.ceil() - Redondea siempre hacia arriba
print("3. Redondear hacia arriba (4.1):", math.ceil(4.1))

# 4. math.floor() - Redondea siempre hacia abajo
print("4. Redondear hacia abajo (4.9):", math.floor(4.9))

# 5. math.trunc() - Corta los decimales (deja solo el entero)
print("5. Truncar/Cortar decimales (8.999):", math.trunc(8.999))

# 6. math.fabs() - Convierte negativos a positivos (valor absoluto en decimal)
print("6. Valor absoluto (-25.5):", math.fabs(-25.5))


print("\n--- 🧮 ARITMÉTICA Y CÁLCULOS ---")
# 7. math.pow() - Eleva un número a una potencia
print("7. Potencia (2 al cubo):", math.pow(2, 3))

# 8. math.sqrt() - Raíz cuadrada
print("8. Raíz cuadrada de 64:", math.sqrt(64))

# 9. math.factorial() - Multiplica todos los números hasta llegar al indicado
print("9. Factorial de 4 (4x3x2x1):", math.factorial(4))

# 10. math.gcd() - Máximo Común Divisor
print("10. Máximo Común Divisor de 24 y 36:", math.gcd(24, 36))

# 11. math.lcm() - Mínimo Común Múltiplo
print("11. Mínimo Común Múltiplo de 4 y 5:", math.lcm(4, 5))

# 12. math.comb() - Combinaciones posibles (sin importar orden)
print("12. Combinaciones (5 elementos en grupos de 2):", math.comb(5, 2))


print("\n--- 📐 TRIGONOMETRÍA (Usa Radianes) ---")
# 13. math.radians() - Convierte grados a radianes
print("13. Convertir 90 grados a radianes:", math.radians(90))

# 14. math.sin() - Seno
print("14. Seno de 90 grados:", math.sin(math.radians(90)))

# 15. math.cos() - Coseno
print("15. Coseno de 180 grados:", math.cos(math.radians(180)))

# 16. math.tan() - Tangente
print("16. Tangente de 45 grados:", math.tan(math.radians(45)))

# 17. math.degrees() - Convierte radianes a grados
print("17. Convertir Pi radianes a grados:", math.degrees(math.pi))


print("\n--- 📈 LOGARITMOS Y EXPONENCIALES ---")
# 18. math.log() - Logaritmo natural (base e)
print("18. Logaritmo natural de 10:", math.log(10))

# 19. math.log10() - Logaritmo en base 10
print("19. Logaritmo base 10 de 1000:", math.log10(1000))

# 20. math.exp() - Eleva la constante 'e' a la potencia indicada
print("20. Exponencial (e a la potencia de 2):", math.exp(2))