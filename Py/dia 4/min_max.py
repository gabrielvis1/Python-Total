"""Demostración de las funciones min y max para encontrar el valor mínimo y máximo de una serie de números."""

menor = min(58,10,5,862,158,25,3,1,0)
mayor = max(58,10,5,862,158,25,3,1,0)
print(f"El número menor es: {menor}")
print(f"El número mayor es: {mayor}")

lista = [58,10,5,862,158,25,3,1,0]
menor_lista = min(lista)
mayor_lista = max(lista)
print(f"El número menor en la lista es: {menor_lista}")
print(f"El número mayor en la lista es: {mayor_lista}")

nombres = ["Juan", "María", "Carlos", "Lucía", "Pedro", "Sofía", "Diego", "Elena", "Marcos", "Valeria"]
menor_nombre = min(nombres) # La función min() devuelve el nombre que va primero alfabéticamente
mayor_nombre = max(nombres) # La función max() devuelve el nombre que va último alfabéticamente
print(f"El nombre que va primero alfabéticamente es: {menor_nombre}")
print(f"El nombre que va último alfabéticamente es: {mayor_nombre}")

nombre = "Sofía"
menor_letra = min(nombre.lower()) # La función min() devuelve la letra que va primero alfabéticamente
mayor_letra = max(nombre) # La función max() devuelve la letra que va último alfabéticamente
print(f"La letra que va primero alfabéticamente en '{nombre}' es: {menor_letra}")
print(f"La letra que va último alfabéticamente en '{nombre}' es: {mayor_letra}")

dic = {"Coca-Cola": "KO", "PepsiCo": "PEP", "McDonald's": "MCD", "Apple": "AAPL"}
menor_clave = min(dic.values()) # La función min() devuelve la clave que va primero alfabéticamente
mayor_clave = max(dic) # La función max() devuelve la clave que va último alfabéticamente
print(f"La clave que va primero alfabéticamente en el diccionario es: {menor_clave}")
print(f"La clave que va último alfabéticamente en el diccionario es: {mayor_clave}")
