"""
Archivo: main.py
Punto de entrada del sistema. Maneja la consola y la interacción.
"""

import os
import time
import sys
from turnos_logic import generador_turnos, imprimir_ticket

def limpiar_consola():
    """Limpia la pantalla de la consola para mantener un entorno agradable."""
    os.system('cls' if os.name == 'nt' else 'clear')

def inicializar_areas():
    """Crea y devuelve el diccionario con las áreas y sus generadores limpios."""
    return {
        "1": {"nombre": "Perfumería", "letra": "P", "gen": generador_turnos("P")},
        "2": {"nombre": "Farmacia", "letra": "F", "gen": generador_turnos("F")},
        "3": {"nombre": "Cosmética", "letra": "C", "gen": generador_turnos("C")},
        "4": {"nombre": "Turno con enfermería", "letra": "E", "gen": generador_turnos("E")},
        "5": {"nombre": "Atención al cliente", "letra": "A", "gen": generador_turnos("A")},
        "6": {"nombre": "Quejas y reclamos", "letra": "Q", "gen": generador_turnos("Q")}
    }

def mostrar_menu_areas(areas_disponibles):
    """Muestra dinámicamente las áreas que el cliente aún puede seleccionar."""
    print("\n--- SELECCIONE EL ÁREA A LA QUE DESEA DIRIGIRSE ---")
    for clave, datos in areas_disponibles.items():
        print(f"[{clave}] - {datos['nombre']}")
    print("-" * 51)

def inicio():
    """Funcion que inicia el programa"""
    areas = inicializar_areas()
    clientes_atendidos_hoy = 0

    while True:
        try:
            limpiar_consola()
            print("*" * 50)
            print("       BIENVENIDO AL TURNERO DE LA FARMACIA       ")
            print("*" * 50)
            print("\nOpciones de ingreso:")
            print("[1] Retirar Turno (Cliente)")
            print("[2] Configuración (Personal)")

            opcion_principal = input("\nIngrese una opción: ").strip()

            if opcion_principal == "1":
                # Lógica del cliente
                areas_para_elegir = areas.copy()
                turnos_seleccionados = [] # Guardaremos las tuplas (NombreArea, NumeroTurno)

                while areas_para_elegir:
                    limpiar_consola()
                    mostrar_menu_areas(areas_para_elegir)
                    seleccion = input("Ingrese el número del área: ").strip()
                    if seleccion in areas_para_elegir:
                        # Extraemos el área para que no pueda volver a elegirla
                        area_elegida = areas_para_elegir.pop(seleccion)
                        # Generamos el turno
                        nuevo_turno = next(area_elegida["gen"])
                        turnos_seleccionados.append((area_elegida["nombre"], nuevo_turno))
                        if not areas_para_elegir:
                            print("\nHas seleccionado todas las áreas disponibles.")
                            break
                        # Preguntamos si desea otra área
                        while True:
                            otra = input("\n¿Desea dirigirse a otra área? (S/N): ").strip().upper()
                            if otra in ['S', 'N']:
                                break
                            print("Por favor, ingrese 'S' para Sí o 'N' para No.")
                        if otra == 'N':
                            break
                    else:
                        print("❌ Error: Opción inválida. Intente nuevamente.")
                        time.sleep(1.5)

                # Imprimir todos los tickets acumulados
                limpiar_consola()
                print("IMPRIMIENDO SUS TURNOS...\n")
                for nombre, turno in turnos_seleccionados:
                    imprimir_ticket(nombre, turno)

                clientes_atendidos_hoy += 1

                print("\nGracias por su visita. Esta pantalla se recargará en 10 segundos...")
                time.sleep(10) # Pausa de 10 segundos como fue solicitado

            elif opcion_principal == "2":
                # Lógica de configuración
                while True:
                    limpiar_consola()
                    print("--- MENÚ DE CONFIGURACIÓN ---")
                    print("[1] Reiniciar día")
                    print("[2] Salir del programa")
                    print("[3] Volver al menú principal")

                    conf = input("\nSeleccione una opción: ").strip()

                    if conf == "1":
                        limpiar_consola()
                        print(f"📊 RESUMEN DEL DÍA: Se atendido {clientes_atendidos_hoy} personas.")
                        print("\nReiniciando contadores y turnos...")
                        areas = inicializar_areas()
                        clientes_atendidos_hoy = 0
                        time.sleep(4)
                        break
                    elif conf == "2":
                        print("\nCerrando el sistema. ¡Hasta pronto!")
                        sys.exit()
                    elif conf == "3":
                        break
                    else:
                        print("❌ Opción inválida.")
                        time.sleep(1)
            else:
                print("❌ Opción inválida. Ingrese 1 o 2.")
                time.sleep(1.5)

        except KeyboardInterrupt:
            # Manejo de error si el usuario presiona Ctrl+C accidentalmente
            print("\n\n⚠️ Interrupción detectada. Cerrando el turnero de forma segura...")
            sys.exit()
        except Exception as e:  # pylint: disable=broad-exception-caught
            # Manejo de errores imprevistos
            print(f"\n❌ Ha ocurrido un error inesperado: {e}")
            print("Reiniciando la interfaz...")
            time.sleep(3)

if __name__ == "__main__":
    inicio()
