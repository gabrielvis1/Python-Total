""" Analizador de Texto - Versión Optimizada Final """
texto = input("Ingresa un texto para analizar: ").lower()
letras = input("Ingresa 3 letras (separadas por espacio): ").lower().split()
palabras = texto.split()

print(f"\n1. Conteo: '{letras[0]}': {texto.count(letras[0])} | '{letras[1]}': {texto.count(letras[1])} | '{letras[2]}': {texto.count(letras[2])}")
print(f"2. Palabras totales: {len(palabras)}")
print(f"3. Extremos: Primera '{texto[0]}' | Última '{texto[-1]}'")
print(f"4. Texto invertido: {' '.join(palabras[::-1])}")
# Nota el espacio entre las llaves: { { ... } }
print(f"5. ¿Está la palabra Python?: { {True: 'Sí', False: 'No'}['python' in texto] }")
