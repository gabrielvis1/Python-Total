"""Modulo encargado de la interfaz grafica, HUD y pantallas del juego"""
import math
import random
import pygame
from recursos import (
    fuente_hud, fuente_menu_chica, fuente_game_over, fuente_estadisticas,
    corazon_img, zombi_hud_img, titulo_img
)

def dibujar_menu(pantalla, mx, my, puntos_magicos, posicion_brillo_x):
    """Dibuja el menú principal, maneja partículas y resplandor amarillo"""
    pantalla.fill((10, 10, 25))
    for punto in puntos_magicos:
        dist_mouse = math.hypot(mx - punto["x"], my - punto["y"])
        if 0 < dist_mouse < 200:
            punto["x"] += (mx - punto["x"]) / dist_mouse * 1.5
            punto["y"] += (my - punto["y"]) / dist_mouse * 1.5
        else:
            punto["x"] += punto["vx"]
            punto["y"] += punto["vy"]
            if punto["x"] < 0 or punto["x"] > 1280:
                punto["vx"] *= -1
            if punto["y"] < 0 or punto["y"] > 720:
                punto["vy"] *= -1
        pygame.draw.circle(pantalla, (255, 255, 255), (int(punto["x"]), int(punto["y"])), 2)

    x_logo = (1280 - 800) // 2
    pantalla.blit(titulo_img, (x_logo, 100))
    
    if posicion_brillo_x > 800 + 200:
        if random.randint(1, 150) == 1:
            posicion_brillo_x = -200
    else:
        posicion_brillo_x += 12
        superficie_brillo = pygame.Surface((800, 436), pygame.SRCALPHA)
        puntos_brillo = [
            (posicion_brillo_x, 0), (posicion_brillo_x + 60, 0),
            (posicion_brillo_x - 40, 436), (posicion_brillo_x - 100, 436)
        ]
        pygame.draw.polygon(superficie_brillo, (255, 255, 150, 90), puntos_brillo)
        pantalla.blit(superficie_brillo, (x_logo, 100))

    texto_jugar = fuente_menu_chica.render("- jugar -", True, (200, 200, 200))
    pantalla.blit(texto_jugar, (1280 // 2 - texto_jugar.get_width() // 2, 580))
    return posicion_brillo_x

def dibujar_hud(pantalla, jugador, cantidad_enemigos, tiempo_actual, tiempo_inicio, modo):
    """Dibuja el HUD con estadísticas, vida, tiempo y modo de control"""
    ancho_hud = 220 
    alto_hud = 150  
    x_hud = 1280 - ancho_hud - 20
    y_hud = 20
    fondo_hud = pygame.Surface((ancho_hud, alto_hud), pygame.SRCALPHA)
    pygame.draw.rect(fondo_hud, (0, 0, 0, 150), fondo_hud.get_rect(), border_radius=15)
    pantalla.blit(fondo_hud, (x_hud, y_hud))
    
    texto_vidas = fuente_hud.render("Vidas:", True, (255, 255, 255))
    pantalla.blit(texto_vidas, (x_hud + 15, y_hud + 10))
    for i in range(jugador.vidas):
        pantalla.blit(corazon_img, (x_hud + 70 + (i * 25), y_hud + 8))
        
    texto_disp = fuente_hud.render(f"Disparos: {jugador.disparos_realizados}", True, (255, 255, 255))
    pantalla.blit(texto_disp, (x_hud + 15, y_hud + 35))
    pantalla.blit(zombi_hud_img, (x_hud + 15, y_hud + 55))
    
    texto_derr = fuente_hud.render(f"x {jugador.enemigos_derrotados} (Bajas)", True, (255, 255, 255))
    pantalla.blit(texto_derr, (x_hud + 40, y_hud + 56))
    pantalla.blit(zombi_hud_img, (x_hud + 15, y_hud + 80))
    
    texto_viv = fuente_hud.render(f"x {cantidad_enemigos} (Vivos)", True, (255, 255, 255))
    pantalla.blit(texto_viv, (x_hud + 40, y_hud + 81))

    seg_totales = (tiempo_actual - tiempo_inicio) // 1000
    minutos = seg_totales // 60
    segundos = seg_totales % 60
    fmt_tiempo = f"Tiempo: {minutos:02d}:{segundos:02d}"
    texto_tiempo = fuente_hud.render(fmt_tiempo, True, (255, 255, 255))
    pantalla.blit(texto_tiempo, (x_hud + 15, y_hud + 105))

    texto_modo = fuente_hud.render(f"Control (M): {modo}", True, (255, 255, 0))
    pantalla.blit(texto_modo, (x_hud + 15, y_hud + 125))

def dibujar_game_over(pantalla, tiempo_final_segundos, enemigos_derrotados):
    """Dibuja la pantalla de Game Over y muestra estadísticas finales"""
    filtro_oscuro = pygame.Surface((1280, 720), pygame.SRCALPHA)
    filtro_oscuro.fill((0, 0, 0, 10))
    pantalla.blit(filtro_oscuro, (0, 0))

    ancho_panel = 500
    alto_panel = 300
    x_panel = (1280 - ancho_panel) // 2
    y_panel = 200 

    fondo_panel = pygame.Surface((ancho_panel, alto_panel), pygame.SRCALPHA)
    pygame.draw.rect(fondo_panel, (20, 20, 20, 230), fondo_panel.get_rect(), border_radius=20)
    pygame.draw.rect(fondo_panel, (200, 50, 50), fondo_panel.get_rect(), width=3, border_radius=20)
    pantalla.blit(fondo_panel, (x_panel, y_panel))

    texto_gameover = fuente_game_over.render("GAME OVER", True, (255, 50, 50))
    pantalla.blit(texto_gameover, (1280 // 2 - texto_gameover.get_width() // 2, y_panel + 20))

    min_fin = tiempo_final_segundos // 60
    seg_fin = tiempo_final_segundos % 60

    texto_t_final = fuente_estadisticas.render(
        f"Tiempo jugado: {min_fin:02d}:{seg_fin:02d}", True, (200, 200, 200))
    texto_e_final = fuente_estadisticas.render(
        f"Enemigos derrotados: {enemigos_derrotados}", True, (200, 200, 200))
    texto_clic = fuente_menu_chica.render(
        "Haz clic para volver al inicio", True, (100, 100, 100))

    pantalla.blit(texto_t_final, (1280 // 2 - texto_t_final.get_width() // 2, y_panel + 120))
    pantalla.blit(texto_e_final, (1280 // 2 - texto_e_final.get_width() // 2, y_panel + 170))
    pantalla.blit(texto_clic, (1280 // 2 - texto_clic.get_width() // 2, y_panel + 250))