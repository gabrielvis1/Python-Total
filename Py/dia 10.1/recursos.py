import pygame

# Inicializamos los motores base de Pygame para poder cargar recursos
pygame.init()
pygame.mixer.init()

# =========================================================================
# FUENTES DE TEXTO
# =========================================================================
fuente_hud = pygame.font.SysFont("Arial", 16, bold=True) 
fuente_menu_chica = pygame.font.SysFont("Arial", 24, bold=True)
fuente_game_over = pygame.font.SysFont("Arial", 64, bold=True)
fuente_estadisticas = pygame.font.SysFont("Arial", 32)

# =========================================================================
# IMÁGENES GLOBALES Y HUD
# =========================================================================
icono = pygame.image.load("imagenes/baston_magico.png")

fondo = pygame.image.load("imagenes/fondo.png")
fondo = pygame.transform.scale(fondo, (1504, 820))

corazon_img = pygame.image.load("imagenes/corazon.png") 
corazon_img = pygame.transform.scale(corazon_img, (20, 20)) 

zombi_hud_img = pygame.transform.scale(pygame.image.load("imagenes/zombi.png"), (20, 20))

try:
    titulo_img = pygame.image.load("imagenes/mago_survivor.png")
    titulo_img = pygame.transform.scale(titulo_img, (800, 436))
except FileNotFoundError:
    titulo_img = pygame.Surface((800, 436))
    titulo_img.fill((30, 30, 30))

# =========================================================================
# MÚSICA Y EFECTOS DE SONIDO
# =========================================================================
pygame.mixer.music.load("sonidos/fondo.mp3") 
pygame.mixer.music.set_volume(0.2) 

sonido_rayo = pygame.mixer.Sound("sonidos/rayo.mp3")
sonido_rayo.set_volume(0.5) 

sonido_muerte = pygame.mixer.Sound("sonidos/muerte.mp3")
sonido_muerte.set_volume(0.5) 

sonido_dano = pygame.mixer.Sound("sonidos/vida_perdida.mp3")
sonido_dano.set_volume(0.5)