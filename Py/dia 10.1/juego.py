"""Módulo principal que controla la lógica y el estado del juego"""
import math
import random
import pygame

from personajes import Mago
from enemigos import Zombi, Lobo
from armas import RayoMagico
from efectos import Explosion
from recursos import fondo, sonido_dano, sonido_muerte, sonido_rayo
from interfaz import dibujar_menu, dibujar_hud, dibujar_game_over

class Juego:
    """Clase administradora que controla todo el flujo del juego"""
    
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.se_ejecuta = True
        
        # Estados
        self.estado = "MENU"
        self.modo_movimiento = "TECLADO"
        self.tiempo_inicio_juego = 0
        self.tiempo_final_segundos = 0
        
        # Entidades (listas y jugador)
        self.jugador = None
        self.enemigos = []
        self.proyectiles = []
        self.explosiones = []
        
        # Tiempos y configuraciones
        self.tiempo_spawn_enemigos = 3000
        self.ultimo_spawn_enemigos = 0
        self.tiempo_entre_disparos = 1000
        self.ultimo_disparo = 0
        self.rango_ataque = 300
        
        # Efectos visuales de Menú
        self.posicion_brillo_x = 1000
        self.puntos_magicos = []
        for _ in range(100):
            self.puntos_magicos.append({
                "x": random.randint(0, 1280),
                "y": random.randint(0, 720),
                "vx": random.uniform(-0.5, 0.5), 
                "vy": random.uniform(-0.5, 0.5)  
            })
            
        # Variables de tiempo y ratón por fotograma
        self.mx = 0
        self.my = 0
        self.tiempo_actual = 0

    def generar_enemigo(self):
        """Genera una instancia de Enemigo en un borde aleatorio"""
        borde = random.randint(0, 3) 
        if borde == 0: 
            x = random.randint(0, 1280)
            y = -50
        elif borde == 1: 
            x = random.randint(0, 1280)
            y = 720 + 50
        elif borde == 2: 
            x = -50
            y = random.randint(0, 720)
        else: 
            x = 1280 + 50
            y = random.randint(0, 720)
        
        # NUEVO: Lógica de aparición aleatoria
        probabilidad = random.randint(1, 100)
        if probabilidad <= 30: # 30% de las veces
            return Lobo(x, y)
        else:                  # 70% de las veces
            return Zombi(x, y)

    def iniciar_partida(self):
        """Reinicia todas las variables del juego para una nueva partida"""
        self.jugador = Mago(640 - 32, 360 - 32)
        self.enemigos.clear()
        self.proyectiles.clear()
        self.explosiones.clear()
        
        self.tiempo_inicio_juego = pygame.time.get_ticks()
        self.ultimo_spawn_enemigos = self.tiempo_inicio_juego - self.tiempo_spawn_enemigos
        pygame.mixer.music.play(-1)

    def procesar_eventos(self):
        """Captura todas las entradas del usuario (teclado y ratón)"""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.se_ejecuta = False

            if self.estado == "JUGANDO":
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_m:
                        if self.modo_movimiento == "TECLADO":
                            self.modo_movimiento = "MOUSE"
                            self.jugador.cambio_x = 0
                            self.jugador.cambio_y = 0
                        else:
                            self.modo_movimiento = "TECLADO"
                            
                    if self.modo_movimiento == "TECLADO":
                        if evento.key in (pygame.K_LEFT, pygame.K_a):
                            self.jugador.cambio_x = -self.jugador.velocidad
                        if evento.key in (pygame.K_RIGHT, pygame.K_d):
                            self.jugador.cambio_x = self.jugador.velocidad
                        if evento.key in (pygame.K_UP, pygame.K_w):
                            self.jugador.cambio_y = -self.jugador.velocidad
                        if evento.key in (pygame.K_DOWN, pygame.K_s):
                            self.jugador.cambio_y = self.jugador.velocidad
                
                if evento.type == pygame.KEYUP:
                    if self.modo_movimiento == "TECLADO":
                        tecl_x = (pygame.K_LEFT, pygame.K_a, pygame.K_RIGHT, pygame.K_d)
                        tecl_y = (pygame.K_UP, pygame.K_w, pygame.K_DOWN, pygame.K_s)
                        if evento.key in tecl_x:
                            self.jugador.cambio_x = 0
                        if evento.key in tecl_y:
                            self.jugador.cambio_y = 0

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if self.estado == "MENU":
                    self.estado = "JUGANDO"
                    self.iniciar_partida()
                elif self.estado == "GAME_OVER":
                    self.estado = "MENU"

    def actualizar(self):
        """Actualiza la matemática y colisiones si el juego está en curso"""
        if self.estado != "JUGANDO":
            return

        # Movimiento del Jugador
        if self.modo_movimiento == "TECLADO":
            self.jugador.mover_teclado()
        elif self.modo_movimiento == "MOUSE":
            self.jugador.mover_mouse(self.mx, self.my)

        self.jugador.aplicar_limites()
        self.jugador.actualizar_inmunidad(self.tiempo_actual)

        # Spawn de Enemigos
        if self.tiempo_actual - self.ultimo_spawn_enemigos >= self.tiempo_spawn_enemigos:
            for _ in range(3):
                self.enemigos.append(self.generar_enemigo())
            self.ultimo_spawn_enemigos = self.tiempo_actual

        enemigo_mas_cercano = None
        distancia_minima = float('inf')

        # Acercar enemigos y buscar al más cercano
        for enemigo in self.enemigos:
            enemigo.mover_hacia_objetivo(self.jugador.x, self.jugador.y)
            dx = self.jugador.x - enemigo.x
            dy = self.jugador.y - enemigo.y
            distancia = (dx ** 2 + dy ** 2) ** 0.5
            if distancia < distancia_minima:
                distancia_minima = distancia
                enemigo_mas_cercano = enemigo

        # Colisiones Enemigo - Jugador
        for enemigo in self.enemigos:
            dx_mago = (enemigo.x + 25) - (self.jugador.x + 32)
            dy_mago = (enemigo.y + 25) - (self.jugador.y + 32)
            distancia_mago = (dx_mago ** 2 + dy_mago ** 2) ** 0.5
            
            if distancia_mago < 35:
                if self.jugador.recibir_dano(self.tiempo_actual):
                    sonido_dano.play()
                    if self.jugador.vidas <= 0:
                        self.estado = "GAME_OVER"
                        pygame.mixer.music.stop()
                        self.tiempo_final_segundos = (
                            self.tiempo_actual - self.tiempo_inicio_juego
                        ) // 1000
                break

        # Disparar Proyectiles
        if self.tiempo_actual - self.ultimo_disparo >= self.tiempo_entre_disparos:
            if enemigo_mas_cercano is not None and distancia_minima <= self.rango_ataque:
                dx_proy = enemigo_mas_cercano.x - self.jugador.x
                dy_proy = enemigo_mas_cercano.y - self.jugador.y
                angulo_rad = math.atan2(-dy_proy, dx_proy)
                angulo_grados = math.degrees(angulo_rad)
                
                if distancia_minima > 0:
                    dir_x = dx_proy / distancia_minima
                    dir_y = dy_proy / distancia_minima
                    
                    nuevo_rayo = RayoMagico(
                        self.jugador.x + 16, self.jugador.y + 16, 
                        dir_x, dir_y, angulo_grados
                    )
                    self.proyectiles.append(nuevo_rayo)
                    self.jugador.disparos_realizados += 1
                    sonido_rayo.play()
                self.ultimo_disparo = self.tiempo_actual

        # Movimiento de Proyectiles y limpieza
        proyectiles_a_eliminar = []
        for i, proyectil in enumerate(self.proyectiles):
            proyectil.mover()
            if proyectil.fuera_de_pantalla():
                if i not in proyectiles_a_eliminar:
                    proyectiles_a_eliminar.append(i)

        # Colisiones Enemigo - Proyectil
        enemigos_a_eliminar = []
        for i, enemigo in enumerate(self.enemigos):
            for j, proyectil in enumerate(self.proyectiles):
                dx_col = (enemigo.x + 25) - (proyectil.x + 16)
                dy_col = (enemigo.y + 25) - (proyectil.y + 16)
                distancia_col = (dx_col ** 2 + dy_col ** 2) ** 0.5
                
                if distancia_col < 30:
                    if i not in enemigos_a_eliminar:
                        enemigos_a_eliminar.append(i)
                        sonido_muerte.play()
                    if j not in proyectiles_a_eliminar:
                        proyectiles_a_eliminar.append(j)
                    
                    self.explosiones.append(
                        Explosion(enemigo.x, enemigo.y, self.tiempo_actual)
                    )

        # Limpiar muertos e impactos
        for i in sorted(enemigos_a_eliminar, reverse=True):
            self.enemigos.pop(i)
            self.jugador.enemigos_derrotados += 1 

        for i in sorted(proyectiles_a_eliminar, reverse=True):
            if i < len(self.proyectiles):
                self.proyectiles.pop(i)

    def dibujar(self):
        """Dibuja todos los elementos en pantalla dependiendo del estado"""
        if self.estado == "MENU":
            self.posicion_brillo_x = dibujar_menu(
                self.pantalla, self.mx, self.my, 
                self.puntos_magicos, self.posicion_brillo_x
            )

        elif self.estado == "JUGANDO":
            self.pantalla.blit(fondo, (-100, -60))
            self.jugador.dibujar(self.pantalla)

            for enemigo in self.enemigos:
                enemigo.dibujar(self.pantalla)

            for proyectil in self.proyectiles:
                proyectil.dibujar(self.pantalla)

            explosiones_a_eliminar = []
            for i, explosion in enumerate(self.explosiones):
                animacion_activa = explosion.procesar_y_dibujar(
                    self.pantalla, self.tiempo_actual
                )
                if not animacion_activa:
                    explosiones_a_eliminar.append(i)
                    
            for i in sorted(explosiones_a_eliminar, reverse=True):
                self.explosiones.pop(i)

            dibujar_hud(
                self.pantalla, self.jugador, len(self.enemigos), 
                self.tiempo_actual, self.tiempo_inicio_juego, self.modo_movimiento
            )

        elif self.estado == "GAME_OVER":
            dibujar_game_over(
                self.pantalla, self.tiempo_final_segundos, 
                self.jugador.enemigos_derrotados
            )

        pygame.display.update()

    def ejecutar(self):
        """El bucle principal que mantiene vivo el juego"""
        while self.se_ejecuta:
            self.tiempo_actual = pygame.time.get_ticks()
            self.mx, self.my = pygame.mouse.get_pos()
            
            self.procesar_eventos()
            self.actualizar()
            self.dibujar()