"""
Archivo: turnos_logic.py
Maneja la lógica de generación de turnos y decoración de los tickets.
"""

def generador_turnos(letra_area):
    """Generador infinito que crea secuencias como P-01, P-02, etc."""
    turno = 1
    while True:
        # Formateamos el número para que siempre tenga dos dígitos (ej: 01, 02)
        yield f"{letra_area}-{turno:02d}"
        turno += 1

def decorador_ticket(funcion):
    """
    Decorador que envuelve la impresión del turno con un 
    mensaje personalizado de bienvenida y despedida.
    """
    def wrapper(area_nombre, turno_asignado):
        # Diccionario de mensajes específicos por área
        mensajes_inicio = {
            "Perfumería": "¡Que el rico aroma te acompañe cada día!",
            "Farmacia": "Tu salud y bienestar son nuestra prioridad.",
            "Cosmética": "Resalta tu belleza natural con nosotros.",
            "Turno con enfermería": "Cuidamos de ti con profesionalismo y dedicación.",
            "Atención al cliente": "Estamos aquí para escucharte y ayudarte.",
            "Quejas y reclamos": "Tu opinión es vital para ayudarnos a mejorar."
        }
        mensaje_fin = "¡QUE TENGAS BUENA COMPRA, ESTAMOS PARA SERVIR!"
        print("\n" + "=" * 50)
        # Obtenemos el mensaje del área, o uno genérico si no existe
        print(mensajes_inicio.get(area_nombre, "¡Bienvenido a nuestra sucursal!"))
        print("Su turno es:")
        # Ejecutamos la función original (que imprime el número)
        funcion(area_nombre, turno_asignado)
        print(mensaje_fin)
        print("=" * 50)

    return wrapper

@decorador_ticket
def imprimir_ticket(_area_nombre, turno_asignado):
    """Función base para imprimir el ticket, que será decorada."""
    # Los espacios son para centrar visualmente el número en la consola
    print(f"                 {turno_asignado}                 ")
