"""Mago Survivor - Archivo Principal"""
import pygame
from recursos import icono
from juego import Juego

# desactivamos a pylint
# pylint: disable=no-member

def main():
    """Punto de arranque del programa"""
    
    # 1. Creamos la ventana
    pantalla = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Mago survivor")
    pygame.display.set_icon(icono)
    
    # 2. Instanciamos nuestro Administrador de Juego
    motor_juego = Juego(pantalla)
    
    # 3. Encendemos el motor (Esto arranca el bucle while)
    motor_juego.ejecutar()
    
    # 4. Cuando el bucle termine (al cerrar la ventana), salimos de forma segura
    pygame.quit()

# Si este archivo se ejecuta directamente, llama a la función main()
if __name__ == "__main__":
    main()