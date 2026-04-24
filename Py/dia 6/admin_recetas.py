import os
import shutil
from pathlib import Path

# Definimos la ruta base según tu captura
RUTA_BASE = Path(r"C:\Users\gabri\OneDrive\Escritorio\Drive\Python total\Py\dia 6\Recetas\Recetas")

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def volver_inicio():
    input("\nPresioná Enter para volver al menú principal...")

def listar_categorias():
    # Retorna una lista con los nombres de las carpetas (categorías)
    return [c.name for c in RUTA_BASE.iterdir() if c.is_dir()]

def listar_recetas(categoria):
    # Retorna una lista con los archivos .txt dentro de una categoría
    ruta_cat = RUTA_BASE / categoria
    return [r.name for r in ruta_cat.glob("*.txt")]

def contar_total_recetas():
    total = 0
    print("\n--- Estado del Recetario ---")
    for cat in listar_categorias():
        recetas = listar_recetas(cat)
        print(f"* {cat}: {len(recetas)} recetas")
        total += len(recetas)
    print(f"\nTOTAL GLOBAL: {total} recetas")

def seleccionar_opcion(lista, mensaje):
    # Función genérica para que el usuario elija algo de una lista
    for i, elemento in enumerate(lista, 1):
        print(f"{i} - {elemento}")
    
    while True:
        eleccion = input(f"\n{mensaje} (o 'v' para volver): ")
        if eleccion.lower() == 'v': return None
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(lista):
            return lista[int(eleccion) - 1]
        print("Opción inválida.")

# --- Funciones de Acción ---

def leer_receta():
    cat = seleccionar_opcion(listar_categorias(), "Elegí una categoría")
    if not cat: return
    
    receta = seleccionar_opcion(listar_recetas(cat), f"¿Qué receta de {cat} querés leer?")
    if not receta: return
    
    ruta_final = RUTA_BASE / cat / receta
    print(f"\n--- {receta} ---\n")
    print(ruta_final.read_text(encoding="utf-8"))

def crear_receta():
    cat = seleccionar_opcion(listar_categorias(), "Elegí la categoría para tu nueva receta")
    if not cat: return
    
    nombre = input("Nombre de la nueva receta: ") + ".txt"
    contenido = input("Escribí el contenido de la receta:\n")
    
    ruta_nueva = RUTA_BASE / cat / nombre
    ruta_nueva.write_text(contenido, encoding="utf-8")
    print(f"\n¡Receta '{nombre}' creada con éxito!")

def crear_categoria():
    nombre = input("Nombre de la nueva categoría: ")
    nueva_ruta = RUTA_BASE / nombre
    if not nueva_ruta.exists():
        nueva_ruta.mkdir()
        print(f"Categoría '{nombre}' creada.")
    else:
        print("Esa categoría ya existe.")

def eliminar_receta():
    cat = seleccionar_opcion(listar_categorias(), "Elegí categoría")
    if not cat: return
    receta = seleccionar_opcion(listar_recetas(cat), "Elegí la receta a eliminar")
    if not receta: return
    
    (RUTA_BASE / cat / receta).unlink() # unlink borra el archivo
    print(f"Receta '{receta}' eliminada.")

def eliminar_categoria():
    cat = seleccionar_opcion(listar_categorias(), "Elegí la categoría a borrar POR COMPLETO")
    if not cat: return
    shutil.rmtree(RUTA_BASE / cat) # Borrado nuclear
    print(f"Categoría '{cat}' y todas sus recetas eliminadas.")

# --- Programa Principal ---

def inicio():
    limpiar_consola()
    print("¡Bienvenido al Administrador de Recetas!")
    nombre = input("¿Cómo es tu nombre? ")
    
    while True:
        limpiar_consola()
        print(f"Hola {nombre}. ¿Qué deseás hacer hoy?\n")
        print(f"Ruta actual: {RUTA_BASE}\n")
        print("1 - Leer receta")
        print("2 - Crear receta")
        print("3 - Crear categoría")
        print("4 - Eliminar receta")
        print("5 - Eliminar categoría")
        print("6 - Ver estadísticas (Conteo)")
        print("7 - Salir")
        
        op = input("\nSeleccioná una opción: ")
        
        limpiar_consola()
        if op == '1': leer_receta()
        elif op == '2': crear_receta()
        elif op == '3': crear_categoria()
        elif op == '4': eliminar_receta()
        elif op == '5': eliminar_categoria()
        elif op == '6': contar_total_recetas()
        elif op == '7': break
        else: print("Opción no válida.")
        
        volver_inicio()

if __name__ == "__main__":
    inicio()