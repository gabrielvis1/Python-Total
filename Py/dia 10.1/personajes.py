import pygame
import math

class Personaje:
    """Clase base que contiene toda la lógica común de cualquier personaje jugable"""
    def __init__(self, x, y, vidas):
        self.x = x
        self.y = y
        self.cambio_x = 0
        self.cambio_y = 0
        self.vidas = vidas
        self.disparos_realizados = 0
        self.enemigos_derrotados = 0
        self.inmune = False
        self.tiempo_inmunidad = 2000
        self.ultimo_golpe_recibido = 0
        self.visible = True
        self.imagen = None
        self.velocidad = 0

    def mover_teclado(self):
        """Aplica el movimiento al personaje usando teclado"""
        self.x += self.cambio_x
        self.y += self.cambio_y

    def mover_mouse(self, mx, my):
        """Calcula el vector y mueve al personaje hacia el ratón"""
        dx_mouse = mx - (self.x + 32)
        dy_mouse = my - (self.y + 32)
        dist_mouse = math.hypot(dx_mouse, dy_mouse)
        if dist_mouse > self.velocidad:
            self.x += (dx_mouse / dist_mouse) * self.velocidad
            self.y += (dy_mouse / dist_mouse) * self.velocidad

    def aplicar_limites(self):
        """Verifica que el personaje no salga de la pantalla"""
        if self.x < 0:
            self.x = 0
        elif self.x > 1280 - 62:
            self.x = 1280 - 62
        if self.y < 0:
            self.y = 0
        elif self.y > 720 - 62:
            self.y = 720 - 62

    def actualizar_inmunidad(self, tiempo_actual):
        """Comprueba el temporizador de daño y genera el efecto de parpadeo"""
        if self.inmune:
            tiempo_desde_golpe = tiempo_actual - self.ultimo_golpe_recibido
            if tiempo_desde_golpe > self.tiempo_inmunidad:
                self.inmune = False
                self.visible = True
            else:
                if (tiempo_desde_golpe // 150) % 2 == 0:
                    self.visible = False
                else:
                    self.visible = True
        else:
            self.visible = True

    def recibir_dano(self, tiempo_actual):
        """Procesa el impacto de un enemigo. Retorna True si recibió daño"""
        if not self.inmune:
            self.vidas -= 1
            self.inmune = True
            self.ultimo_golpe_recibido = tiempo_actual
            return True
        return False

    def dibujar(self, superficie):
        """Dibuja la imagen del personaje en pantalla si es visible"""
        if self.visible and self.imagen:
            superficie.blit(self.imagen, (self.x, self.y))


class Mago(Personaje):
    """Clase específica del personaje Mago. Hereda de Personaje."""
    def __init__(self, x, y):
        super().__init__(x, y, vidas=3)
        imagen_bruta = pygame.image.load("imagenes/mago.png")
        self.imagen = pygame.transform.scale(imagen_bruta, (64, 64))
        self.velocidad = 1