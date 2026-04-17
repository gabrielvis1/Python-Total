"""
GUÍA DE SETS (CONJUNTOS) - CÓDIGO LIMPIO
Este script demuestra operaciones lógicas entre conjuntos sin errores.
"""

# 1. Definición de conjuntos (sin duplicados automáticamente)
set_a = {1, 2, "tres"}
set_b = {3, "tres"}

# 2. Operaciones que generan un NUEVO conjunto
# Unión: combina ambos eliminando repetidos
union_set = set_a.union(set_b)

# Intersección: solo los elementos que están en ambos
inter_set = set_a.intersection(set_b)

# Diferencia: elementos que están en A pero NO en B
diff_set = set_a.difference(set_b)

# Diferencia Simétrica: elementos que no se repiten en ambos
sym_diff = set_a.symmetric_difference(set_b)

# 3. Métodos de actualización (modifican el original)
# Agrega los elementos de B al conjunto A
set_a.update(set_b)

# 4. Comprobaciones lógicas (True/False)
# ¿No tienen nada en común?
print(f"¿Son conjuntos disjuntos?: {set_a.isdisjoint(set_b)}")

# Resultados para verificar en consola
print(f"Unión: {union_set}")
print(f"Intersección: {inter_set}")
print(f"Diferencia: {diff_set}")

# 5 eliminar un aleatorio
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
ganador = sorteo.pop()
print("el ganador es " + ganador)
# 6 agragar a set
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Martin")

#7 medir
print(len(sorteo))

print("Dámian" in sorteo)

print(sorteo)

sorteo.remove("Camila")
print(sorteo)

sorteo.discard("Damián")
print(sorteo)
