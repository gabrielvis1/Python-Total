import pygame
import math

class Proyectil:
    """Clase base para cualquier ataque a distancia"""
    def __init__(self, x, y, dir_x, dir_y, velocidad, imagen):
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.velocidad = velocidad
        self.imagen = imagen

    def mover(self):
        """Avanza el proyectil en su dirección matemática"""
        self.x += self.dir_x * self.velocidad
        self.y += self.dir_y * self.velocidad

    def dibujar(self, superficie):
        """Dibuja el ataque en pantalla"""
        superficie.blit(self.imagen, (self.x, self.y))

    def fuera_de_pantalla(self):
        """Comprueba si el ataque ya salió de los límites para borrarlo"""
        return self.x < -50 or self.x > 1300 or self.y < -50 or self.y > 800

class RayoMagico(Proyectil):
    """Ataque básico del Mago. Hereda de Proyectil."""
    imagen_base = pygame.transform.scale(pygame.image.load("imagenes/destello.png"), (32, 32))
    
    def __init__(self, x, y, dir_x, dir_y, angulo_grados):
        imagen_rotada = pygame.transform.rotate(self.imagen_base, angulo_grados + 135)
        super().__init__(x, y, dir_x, dir_y, velocidad=5, imagen=imagen_rotada)