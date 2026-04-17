def procesar_comando(comando):
    match comando:
        case "iniciar":
            return "El sistema se está encendiendo..."
        
        case "detener":
            return "Apagando todos los procesos."
        
        case "reiniciar" | "reload":
            # El símbolo | actúa como un "o" lógico dentro del case
            return "Reiniciando el sistema."
        
        case _:
            # El guion bajo captura cualquier cosa que no coincidió arriba
            return "Comando no reconocido."

# Pruebas
print(procesar_comando("iniciar"))    # El sistema se está encendiendo...
print(procesar_comando("reload"))     # Reiniciando el sistema.
print(procesar_comando("vuelo"))      # Comando no reconocido.

# 2 Diccionarios de Clientes
cliente_1 = {"nombre": "Carlos", "id_cliente": 101, "plan": "Premium"}
cliente_2 = {"nombre": "Ana", "id_cliente": 102, "plan": "Básico"}

# 2 Diccionarios de Películas
pelicula_1 = {"titulo": "Inception", "director": "Christopher Nolan", "año": 2010}
pelicula_2 = {"titulo": "Pulp Fiction", "director": "Quentin Tarantino", "año": 1994}

# 1 Diccionario de Libro
libro_1 = {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "isbn": "978-0307474728"}

# Almacenamos todo en una sola variable (lista)
coleccion_datos = [cliente_1, cliente_2, pelicula_1, pelicula_2, libro_1]

""" 
Recorremos la colección y usamos match para identificar 
el tipo de dato basándonos en sus llaves (keys).
"""

for elemento in coleccion_datos:
    match elemento:
        # Si tiene la llave 'id_cliente', es un Cliente
        case {"nombre": n, "id_cliente": i, "plan": p}:
            print(f"REGISTRO: Se ha detectado un CLIENTE. Nombre: {n} | ID: {i}")

        # Si tiene la llave 'director', es una Película
        case {"titulo": t, "director": d, "año": a}:
            print(f"CINE: Se ha detectado una PELÍCULA. Título: '{t}' dirigida por {d}")

        # Si tiene la llave 'isbn', es un Libro
        case {"titulo": t, "autor": a, "isbn": i}:
            print(f"LITERATURA: Se ha detectado un LIBRO. Título: '{t}' escrito por {a}")

        # Caso por defecto si no coincide con ninguna estructura conocida
        case _:
            print("Error: Tipo de dato no reconocido.")