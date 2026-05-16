import pygame
import math

class Enemigo:
    """Clase base para todos los enemigos del juego"""
    def __init__(self, x, y, velocidad, imagen):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.imagen = imagen

    def mover_hacia_objetivo(self, objetivo_x, objetivo_y):
        """Calcula la distancia al jugador y se mueve hacia él"""
        dx = objetivo_x - self.x
        dy = objetivo_y - self.y
        distancia = (dx ** 2 + dy ** 2) ** 0.5
        if distancia > 0:
            self.x += (dx / distancia) * self.velocidad
            self.y += (dy / distancia) * self.velocidad

    def dibujar(self, superficie):
        """Dibuja al enemigo en pantalla"""
        superficie.blit(self.imagen, (self.x, self.y))


class Zombi(Enemigo):
    """Enemigo tipo Zombi. Hereda de Enemigo."""
    # Cargamos la imagen una sola vez a nivel de clase para no saturar la memoria
    imagen_bruta = pygame.image.load("imagenes/zombi.png")
    imagen_zombi = pygame.transform.scale(imagen_bruta, (50, 50))
    
    def __init__(self, x, y):
        # Llama al padre dándole su velocidad específica y su imagen
        super().__init__(x, y, velocidad=0.5, imagen=self.imagen_zombi)

class Lobo(Enemigo):
    """Enemigo tipo Lobo. Más rápido y se mueve en zigzag."""
    
    # Intenta cargar la imagen, usa un cuadro gris de respaldo si no existe
    try:
        imagen_bruta = pygame.image.load("imagenes/lobo.png")
        imagen_lobo = pygame.transform.scale(imagen_bruta, (50, 50))
    except FileNotFoundError:
        imagen_lobo = pygame.Surface((50, 50))
        imagen_lobo.fill((100, 100, 100)) # Cuadro gris si falta la imagen
    
    def __init__(self, x, y):
        # Velocidad 1.5 como pediste
        super().__init__(x, y, velocidad=1.5, imagen=self.imagen_lobo)
        # Guardamos cuándo nació para calcular el zigzag basándonos en su tiempo de vida
        self.tiempo_nacimiento = pygame.time.get_ticks()

    def mover_hacia_objetivo(self, objetivo_x, objetivo_y):
        """Sobrescribimos el método para darle un movimiento en Zigzag"""
        dx = objetivo_x - self.x
        dy = objetivo_y - self.y
        distancia = (dx ** 2 + dy ** 2) ** 0.5
        
        if distancia > 0:
            # 1. Dirección recta hacia el jugador (Vector Normalizado)
            dir_x = dx / distancia
            dir_y = dy / distancia
            
            # 2. Dirección perpendicular (para moverse de lado a lado)
            perp_x = -dir_y
            perp_y = dir_x
            
            # 3. Calcular la oscilación del zigzag usando seno (math.sin)
            tiempo_vivo = pygame.time.get_ticks() - self.tiempo_nacimiento
            # Ajusta el '0.005' para que cambie de dirección más rápido/lento
            # Ajusta el '2.5' para que el zigzag sea más ancho/estrecho
            onda = math.sin(tiempo_vivo * 0.005) * 2.5 
            
            # 4. Sumamos el avance frontal + el desplazamiento lateral (zigzag)
            self.x += (dir_x * self.velocidad) + (perp_x * onda)
            self.y += (dir_y * self.velocidad) + (perp_y * onda)