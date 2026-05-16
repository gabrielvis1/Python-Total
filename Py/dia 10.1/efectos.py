import pygame

class Explosion:
    """Controla la animación de humo al morir un enemigo"""
    img1 = pygame.transform.scale(pygame.image.load("imagenes/explosion.png"), (50, 50))
    img2 = pygame.transform.scale(pygame.image.load("imagenes/explosion2.png"), (50, 50))
    
    def __init__(self, x, y, tiempo_inicio):
        self.x = x
        self.y = y
        self.tiempo_inicio = tiempo_inicio
        
    def procesar_y_dibujar(self, superficie, tiempo_actual):
        """Dibuja el frame correcto según el tiempo. Retorna False si ya terminó."""
        tiempo_vivo = tiempo_actual - self.tiempo_inicio
        if tiempo_vivo < 150:
            superficie.blit(self.img1, (self.x, self.y))
            return True
        elif tiempo_vivo < 300:
            superficie.blit(self.img2, (self.x, self.y))
            return True
        return False