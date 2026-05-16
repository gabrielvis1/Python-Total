"""Juego para mi novia - Besos para Aime"""
import pygame
import random # AÑADIDO: Para los movimientos aleatorios (NO MODIFICAR)
import math   # AÑADIDO: Para calcular las colisiones y seguimientos (NO MODIFICAR)

# 1. Inicializamos pygame y el mezclador de audio (NO MODIFICAR)
pygame.mixer.init() # Inicializa el sistema de sonido
pygame.init()

# 2. Configuramos la pantalla de 800 de ancho por 600 de alto (PUEDES MODIFICAR LOS NÚMEROS)
pantalla = pygame.display.set_mode((800, 600))
# 3. Título de la ventana (PUEDES MODIFICARLO)
pygame.display.set_caption("Elvis te ama")

# 4. Control de FPS para mantener la velocidad estable (NO MODIFICAR)
reloj = pygame.time.Clock()

# --- CARGA DE AUDIO ---
try:
    pygame.mixer.music.load("sonidos/m_fondo.mp3")
    pygame.mixer.music.set_volume(0.8) 
    pygame.mixer.music.play(-1) 
except:
    pass 

# Sonidos Nave 1
try:
    sonido_beso = pygame.mixer.Sound("sonidos/kiss.mp3")
    sonido_beso.set_volume(1.0) 
except:
    sonido_beso = None 

try:
    sonido_k = pygame.mixer.Sound("sonidos/k.mp3")
    sonido_k.set_volume(1.0)
except:
    sonido_k = None

# Sonidos Nave 2
try:
    sonido_puno = pygame.mixer.Sound("sonidos/puno.mp3") 
    sonido_puno.set_volume(1.0) 
except:
    sonido_puno = None 

try:
    sonido_corazon = pygame.mixer.Sound("sonidos/dame_amor.mp3")
    sonido_corazon.set_volume(1.0)
except:
    sonido_corazon = None

# Sonidos de los Enemigos (Nave 1)
try:
    sonido_wii = pygame.mixer.Sound("sonidos/wii.mp3")
    sonido_wii.set_volume(1.0)
except:
    sonido_wii = None

try:
    sonido_muak = pygame.mixer.Sound("sonidos/muak.mp3")
    sonido_muak.set_volume(1.0)
except:
    sonido_muak = None

# AÑADIDO: Sonidos de los Enemigos (Nave 2)
try:
    sonido_auk = pygame.mixer.Sound("sonidos/auk.mp3")
    sonido_auk.set_volume(1.0)
except:
    sonido_auk = None

try:
    sonido_k_enamorado = pygame.mixer.Sound("sonidos/k.mp3")
    sonido_k_enamorado.set_volume(1.0)
except:
    sonido_k_enamorado = None

# --- CARGA DE IMÁGENES TEMPORALES Y DEFINITIVAS ---
try:
    icono = pygame.image.load("imagenes/carta.png")
    pygame.display.set_icon(icono)
except:
    pass

def cargar_imagen_o_falsa(ruta_archivo, color_respaldo, tamaño_respaldo=(50, 50)):
    try:
        return pygame.image.load(ruta_archivo)
    except:
        superficie = pygame.Surface(tamaño_respaldo)
        superficie.fill(color_respaldo)
        return superficie

# 5. DEFINICIÓN DE IMÁGENES (Rutas actualizadas a la carpeta imagenes)
# Fondos y Efectos
img_fondo = cargar_imagen_o_falsa("imagenes/fondo.png", (20, 20, 40), (800, 600))     
img_it = cargar_imagen_o_falsa("imagenes/it.png", (255, 255, 0), (40, 40))            
img_vida = cargar_imagen_o_falsa("imagenes/vida.png", (255, 255, 255), (30, 30)) 

# Proyectiles Nave 1
img_beso = cargar_imagen_o_falsa("imagenes/beso.png", (255, 20, 147), (20, 20))       
img_carta_amor = cargar_imagen_o_falsa("imagenes/carta-de-amor.png", (255, 182, 193), (30, 30)) 

# Proyectiles Nave 2
img_puno = cargar_imagen_o_falsa("imagenes/puno.png", (255, 165, 0), (20, 20)) 
img_corazon_k = cargar_imagen_o_falsa("imagenes/corazon.png", (255, 0, 0), (30, 30)) 

# Personajes Principales
img_nave1 = cargar_imagen_o_falsa("imagenes/besucon.png", (0, 0, 255), (64, 64))     
img_nave2 = cargar_imagen_o_falsa("imagenes/nave2.png", (0, 255, 255), (64, 64))     

# Enemigos para la Nave 1
img_n1_ene3 = cargar_imagen_o_falsa("imagenes/enemigo3.png", (150, 0, 0))   
img_n1_ene2 = cargar_imagen_o_falsa("imagenes/enemigo2.png", (200, 50, 50)) 
img_n1_ene1 = cargar_imagen_o_falsa("imagenes/enemigo1.png", (255, 150, 150)) 
img_n1_ene0 = cargar_imagen_o_falsa("imagenes/enemigo0.png", (0, 255, 0))   

# Enemigos para la Nave 2 (Variables 1.1, 2.1, 3.1)
img_n2_ene3 = cargar_imagen_o_falsa("imagenes/enemigo3_1.png", (150, 150, 0))   
img_n2_ene2 = cargar_imagen_o_falsa("imagenes/enemigo2_1.png", (200, 200, 50))  
img_n2_ene1 = cargar_imagen_o_falsa("imagenes/enemigo1_1.png", (255, 255, 150)) 
img_n2_ene0 = cargar_imagen_o_falsa("imagenes/enemigo0_1.png", (0, 255, 0))     

# Fuentes para los textos del menú y puntuación 
fuente_titulo = pygame.font.SysFont(None, 72)
fuente_menu = pygame.font.SysFont(None, 48)
fuente_chica = pygame.font.SysFont(None, 36)
fuente_mini = pygame.font.SysFont(None, 24)

# --- VARIABLES GLOBALES DEL JUEGO ---
estado_juego = "MENU" # Puede ser: "MENU", "SELECCION", "JUGANDO", "GAMEOVER" (NO MODIFICAR)
nave_elegida = 1      # Guardará qué nave se escogió (1 o 2) (NO MODIFICAR)
puntuacion_enamorados = 0 # Contador de novias enamoradas (NO MODIFICAR)

# Variables del jugador (NO MODIFICAR AQUÍ, SE REINICIAN AL JUGAR)
jugador_x = 368
jugador_y = 530
jugador_x_cambio = 0
jugador_y_cambio = 0
vidas = 3
nivel_ataque = 1

# Listas de objetos en pantalla (NO MODIFICAR)
besos = []
burbujas_k = []      
enemigos = []
rayos_enemigos = []
poderes = []
estrellas = []        
lista_it = []        
temporizador_spawn = 0

# Controles de tiempo especiales (NO MODIFICAR)
ultimo_uso_k = -50000
ultimo_it_mostrado = 0

# --- FUNCIONES MATEMÁTICAS Y DE DIBUJO ---
def hay_colision(x1, y1, x2, y2, distancia_minima):
    distancia = math.hypot(x1 - x2, y1 - y2)
    return distancia < distancia_minima

def reiniciar_juego():
    global jugador_x, jugador_y, vidas, puntuacion_enamorados, nivel_ataque
    global besos, burbujas_k, enemigos, rayos_enemigos, poderes, estrellas, lista_it
    global ultimo_uso_k, ultimo_it_mostrado
    jugador_x = 368
    jugador_y = 530
    vidas = 3
    puntuacion_enamorados = 0
    nivel_ataque = 1
    ultimo_uso_k = -50000
    ultimo_it_mostrado = 0
    besos.clear(); burbujas_k.clear(); enemigos.clear()
    rayos_enemigos.clear(); poderes.clear(); estrellas.clear(); lista_it.clear()

def disparar_beso(x, y, nivel):
    if nave_elegida == 1 and sonido_beso:
        sonido_beso.play()
    elif nave_elegida == 2 and sonido_puno:
        sonido_puno.play()
        
    if nivel == 1: besos.append([x + 24, y, 0, -8])
    elif nivel == 2:
        besos.append([x + 8, y, 0, -8]); besos.append([x + 40, y, 0, -8])
    elif nivel == 3:
        besos.append([x + 24, y, 0, -8]); besos.append([x + 8, y, -3, -7]); besos.append([x + 40, y, 3, -7])
    elif nivel >= 4:
        besos.append([x + 16, y, 0, -8]); besos.append([x + 32, y, 0, -8])
        besos.append([x, y, -4, -6]); besos.append([x + 48, y, 4, -6])

def dibujar_texto(texto, fuente, color, x, y):
    imagen_texto = fuente.render(texto, True, color)
    pantalla.blit(imagen_texto, (x, y))

# --- BUCLE PRINCIPAL DEL JUEGO ---
ejecutando = True
while ejecutando:
    tiempo_actual = pygame.time.get_ticks()

    # Dibuja el fondo de pantalla (NO MODIFICAR)
    pantalla.blit(img_fondo, (0, 0))

    # --- SISTEMA DE ESTRELLAS DE FONDO ---
    if random.randint(1, 100) <= 15:
        estrellas.append([random.randint(0, 800), 0, random.uniform(0.5, 2), random.randint(1, 3)])
        
    for est in estrellas[:]:
        est[1] += est[2]
        pygame.draw.circle(pantalla, (255, 255, 255), (int(est[0]), int(est[1])), est[3])
        if est[1] > 600:
            estrellas.remove(est)

    # 1. CAPTURA DE EVENTOS GENERALES
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            
        if estado_juego == "JUGANDO":
            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_LEFT, pygame.K_a): jugador_x_cambio = -5
                if evento.key in (pygame.K_RIGHT, pygame.K_d): jugador_x_cambio = 5
                if evento.key in (pygame.K_UP, pygame.K_w): jugador_y_cambio = -5
                if evento.key in (pygame.K_DOWN, pygame.K_s): jugador_y_cambio = 5
                
                if evento.key == pygame.K_SPACE: disparar_beso(jugador_x, jugador_y, nivel_ataque)
                
                if evento.key == pygame.K_k:
                    if tiempo_actual - ultimo_uso_k >= 50000:
                        if nave_elegida == 1 and sonido_k: 
                            sonido_k.play()
                        elif nave_elegida == 2 and sonido_corazon:
                            sonido_corazon.play()
                            
                        burbujas_k.append({
                            "x": jugador_x + 16,
                            "y": jugador_y - 20,
                            "fase": "volando",
                            "radio": 30
                        })
                        ultimo_uso_k = tiempo_actual

            if evento.type == pygame.KEYUP:
                if evento.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_d): jugador_x_cambio = 0
                if evento.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_w, pygame.K_s): jugador_y_cambio = 0

        if evento.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            
            if estado_juego == "MENU":
                if 250 < y_mouse < 300: estado_juego = "SELECCION"
                if 450 < y_mouse < 500: ejecutando = False
                
            elif estado_juego == "SELECCION":
                if x_mouse < 400:
                    nave_elegida = 1
                    reiniciar_juego()
                    estado_juego = "JUGANDO"
                else:
                    nave_elegida = 2
                    reiniciar_juego()
                    estado_juego = "JUGANDO"
                    
            elif estado_juego == "GAMEOVER":
                if 400 < y_mouse < 450:
                    estado_juego = "MENU"

    # --- LÓGICA Y DIBUJO DEPENDIENDO DEL ESTADO ---

    if estado_juego == "MENU":
        dibujar_texto("Besos para Aime", fuente_titulo, (255, 100, 150), 200, 100)
        dibujar_texto("> Iniciar Juego <", fuente_menu, (255, 255, 255), 250, 250)
        dibujar_texto("> Configuración <", fuente_menu, (150, 150, 150), 250, 350)
        dibujar_texto("> Salir <", fuente_menu, (255, 255, 255), 330, 450)

    elif estado_juego == "SELECCION":
        dibujar_texto("Elige tu Nave", fuente_titulo, (255, 255, 255), 230, 50)
        pygame.draw.line(pantalla, (255,255,255), (400, 150), (400, 550), 2)
        
        pantalla.blit(img_nave1, (160, 250))
        dibujar_texto("Nave 1", fuente_menu, (255,255,255), 150, 350)
        pantalla.blit(img_n1_ene3, (50, 450)); pantalla.blit(img_n1_ene2, (150, 450)); pantalla.blit(img_n1_ene1, (250, 450))
        
        pantalla.blit(img_nave2, (560, 250))
        dibujar_texto("Nave 2", fuente_menu, (255,255,255), 550, 350)
        pantalla.blit(img_n2_ene3, (450, 450)); pantalla.blit(img_n2_ene2, (550, 450)); pantalla.blit(img_n2_ene1, (650, 450))

    elif estado_juego == "JUGANDO":
        
        # --- APARICIÓN DE IMAGEN SORPRESA "IT" (+50 ENEMIGOS) ---
        if puntuacion_enamorados > 0 and puntuacion_enamorados % 50 == 0 and puntuacion_enamorados > ultimo_it_mostrado:
            lista_it.append({
                "x": random.randint(50, 700), "y": random.randint(50, 200),
                "vx": random.choice([-3, 3]), "vy": random.choice([-3, 3]),
                "size": 40, "spawn_time": tiempo_actual
            })
            ultimo_it_mostrado = puntuacion_enamorados
            
        for personaje_it in lista_it[:]:
            personaje_it["x"] += personaje_it["vx"]
            personaje_it["y"] += personaje_it["vy"]
            
            if personaje_it["x"] <= 0 or personaje_it["x"] >= 800 - personaje_it["size"]:
                personaje_it["vx"] *= -1
            if personaje_it["y"] <= 0 or personaje_it["y"] >= 600 - personaje_it["size"]:
                personaje_it["vy"] *= -1
                
            if personaje_it["size"] < 100:
                personaje_it["size"] += 0.05
                
            img_it_escalada = pygame.transform.scale(img_it, (int(personaje_it["size"]), int(personaje_it["size"])))
            pantalla.blit(img_it_escalada, (int(personaje_it["x"]), int(personaje_it["y"])))
            
            if tiempo_actual - personaje_it["spawn_time"] >= 50000:
                lista_it.remove(personaje_it)

        # 1. Movimiento y Límites del jugador
        jugador_x += jugador_x_cambio
        jugador_y += jugador_y_cambio
        if jugador_x <= 0: jugador_x = 0
        elif jugador_x >= 736: jugador_x = 736
        if jugador_y <= 0: jugador_y = 0
        elif jugador_y >= 536: jugador_y = 536

        # 2. Generación de Enemigos
        temporizador_spawn += 1
        if temporizador_spawn >= 80:
            tipo_azar = random.choice([1, 2, 3])
            enemigos.append({
                "x": random.randint(50, 700), "y": -50,
                "nivel": tipo_azar,
                "vel_x": random.choice([-2, 2]), "vel_y": random.uniform(1, 2.5),
                "cooldown": 0
            })
            temporizador_spawn = 0

        # 3. Lógica de Enemigos
        for ene in enemigos[:]:
            if ene["nivel"] <= 0:
                ene["y"] -= 2
                if ene["y"] < -60: enemigos.remove(ene)
                continue

            ene["x"] += ene["vel_x"]
            ene["y"] += ene["vel_y"]

            if ene["y"] > 360:
                ene["y"] = 360
                ene["vel_y"] *= -1
            if ene["y"] < 0 and ene["vel_y"] < 0: ene["vel_y"] *= -1
            if ene["x"] <= 0 or ene["x"] >= 750: ene["vel_x"] *= -1

            ene["cooldown"] += 1

            if ene["nivel"] == 2 and ene["cooldown"] > 120:
                rayos_enemigos.append({"x": ene["x"]+25, "y": ene["y"]+50, "vx": 0, "vy": 5, "rastreador": False})
                ene["cooldown"] = 0

            if ene["nivel"] == 3:
                if random.randint(1, 100) < 5:
                    if ene["x"] < jugador_x: ene["vel_x"] = 2
                    else: ene["vel_x"] = -2
                    
                if ene["cooldown"] > 90:
                    rayos_enemigos.append({"x": ene["x"]+25, "y": ene["y"]+50, "vx": 0, "vy": 4, "rastreador": True})
                    ene["cooldown"] = 0
                    
                for beso in besos:
                    if hay_colision(ene["x"], ene["y"], beso[0], beso[1], 100) and ene["cooldown"] > 30:
                        rayos_enemigos.append({"x": ene["x"]+25, "y": ene["y"]+50, "vx": 0, "vy": 6, "rastreador": False})
                        ene["cooldown"] = -50

            if hay_colision(jugador_x+32, jugador_y+32, ene["x"]+25, ene["y"]+25, 40):
                vidas -= 1
                enemigos.remove(ene)
                jugador_x = 368
                jugador_y = 530

        # 4. Lógica de Disparos del Enemigo (Rayos)
        for rayo in rayos_enemigos[:]:
            if rayo["rastreador"] and rayo["y"] < jugador_y - 100:
                if rayo["x"] < jugador_x + 32: rayo["vx"] = 2
                else: rayo["vx"] = -2
            else:
                if rayo["rastreador"]: rayo["vx"] = 0
                
            rayo["x"] += rayo["vx"]
            rayo["y"] += rayo["vy"]
            
            pygame.draw.rect(pantalla, (255, 255, 0), (int(rayo["x"]), int(rayo["y"]), 5, 15))
            
            if hay_colision(jugador_x+32, jugador_y+32, rayo["x"], rayo["y"], 30):
                vidas -= 1
                rayos_enemigos.remove(rayo)
            elif rayo["y"] > 600:
                rayos_enemigos.remove(rayo)

        # 5. Lógica de Disparos del Jugador
        for beso in besos[:]:
            beso[0] += beso[2]; beso[1] += beso[3]
            
            if nave_elegida == 1:
                pantalla.blit(img_beso, (int(beso[0]), int(beso[1])))
            else:
                pantalla.blit(img_puno, (int(beso[0]), int(beso[1])))
            
            eliminar_beso = False
            for ene in enemigos[:]:
                if ene["nivel"] > 0 and hay_colision(beso[0]+10, beso[1]+10, ene["x"]+25, ene["y"]+25, 30):
                    ene["nivel"] -= 1
                    eliminar_beso = True
                    
                    # AÑADIDO: Lógica separada de sonidos al golpear enemigos con disparos normales
                    if ene["nivel"] == 0:
                        puntuacion_enamorados += 1
                        if random.randint(1, 100) <= 15: poderes.append([ene["x"], ene["y"]])
                        # Sonido final de enamoramiento
                        if nave_elegida == 1 and sonido_muak: 
                            sonido_muak.play()
                        elif nave_elegida == 2 and sonido_k_enamorado:
                            sonido_k_enamorado.play()
                    else:
                        # Sonido de daño (baja nivel)
                        if nave_elegida == 1 and sonido_wii:
                            sonido_wii.play()
                        elif nave_elegida == 2 and sonido_auk:
                            sonido_auk.play()
                    break
                    
            if beso[1] < 0 or beso[0] < 0 or beso[0] > 800: eliminar_beso = True
            if eliminar_beso and beso in besos: besos.remove(beso)

        # 6. LÓGICA DEL ATAQUE ESPECIAL "K" (MISIL TELEDIRIGIDO Y EXPLOSIÓN DE ÁREA)
        for bomba in burbujas_k[:]:
            if bomba["fase"] == "volando":
                enemigo_cercano = None
                distancia_minima = 9999
                for ene in enemigos:
                    if ene["nivel"] > 0:
                        dist = math.hypot(bomba["x"] - (ene["x"]+25), bomba["y"] - (ene["y"]+25))
                        if dist < distancia_minima:
                            distancia_minima = dist
                            enemigo_cercano = ene
                
                if enemigo_cercano:
                    dx = (enemigo_cercano["x"] + 25) - bomba["x"]
                    dy = (enemigo_cercano["y"] + 25) - bomba["y"]
                    dist = math.hypot(dx, dy)
                    if dist != 0:
                        bomba["x"] += (dx / dist) * 7
                        bomba["y"] += (dy / dist) * 7
                else:
                    bomba["y"] -= 7

                if nave_elegida == 1:
                    carta_escalada = pygame.transform.scale(img_carta_amor, (30, 30))
                else:
                    carta_escalada = pygame.transform.scale(img_corazon_k, (30, 30))
                    
                pantalla.blit(carta_escalada, (int(bomba["x"] - 15), int(bomba["y"] - 15)))

                hit = False
                for ene in enemigos:
                    if ene["nivel"] > 0 and hay_colision(bomba["x"], bomba["y"], ene["x"]+25, ene["y"]+25, 30):
                        bomba["fase"] = "explotando"
                        hit = True
                        break
                if not hit and bomba["y"] < -50:
                    burbujas_k.remove(bomba)
            
            elif bomba["fase"] == "explotando":
                bomba["radio"] += 4
                
                if nave_elegida == 1:
                    carta_escalada = pygame.transform.scale(img_carta_amor, (int(bomba["radio"]), int(bomba["radio"])))
                else:
                    carta_escalada = pygame.transform.scale(img_corazon_k, (int(bomba["radio"]), int(bomba["radio"])))
                    
                pos_x = int(bomba["x"] - bomba["radio"]/2)
                pos_y = int(bomba["y"] - bomba["radio"]/2)
                pantalla.blit(carta_escalada, (pos_x, pos_y))
                
                if bomba["radio"] >= 100:
                    for ene in enemigos:
                        if ene["nivel"] > 0 and hay_colision(bomba["x"], bomba["y"], ene["x"]+25, ene["y"]+25, 100):
                            nivel_anterior = ene["nivel"] 
                            ene["nivel"] -= 2
                            
                            # AÑADIDO: Lógica de sonidos separada para la explosión K
                            if ene["nivel"] <= 0:
                                ene["nivel"] = 0
                                puntuacion_enamorados += 1
                                if random.randint(1, 100) <= 15: poderes.append([ene["x"], ene["y"]])
                                
                                if nivel_anterior > 0: 
                                    if nave_elegida == 1 and sonido_muak:
                                        sonido_muak.play()
                                    elif nave_elegida == 2 and sonido_k_enamorado:
                                        sonido_k_enamorado.play()
                            else:
                                if nave_elegida == 1 and sonido_wii: 
                                    sonido_wii.play() 
                                elif nave_elegida == 2 and sonido_auk:
                                    sonido_auk.play()
                    burbujas_k.remove(bomba)

        # 7. DIBUJAR TODO EN PANTALLA
        if nave_elegida == 1: pantalla.blit(img_nave1, (jugador_x, jugador_y))
        else: pantalla.blit(img_nave2, (jugador_x, jugador_y))

        for ene in enemigos:
            x, y = int(ene["x"]), int(ene["y"])
            if nave_elegida == 1:
                if ene["nivel"] == 3: pantalla.blit(img_n1_ene3, (x, y))
                elif ene["nivel"] == 2: pantalla.blit(img_n1_ene2, (x, y))
                elif ene["nivel"] == 1: pantalla.blit(img_n1_ene1, (x, y))
                elif ene["nivel"] == 0: pantalla.blit(img_n1_ene0, (x, y))
            else:
                if nave_elegida == 2:
                    if ene["nivel"] == 3: pantalla.blit(img_n2_ene3, (x, y))
                    elif ene["nivel"] == 2: pantalla.blit(img_n2_ene2, (x, y))
                    elif ene["nivel"] == 1: pantalla.blit(img_n2_ene1, (x, y))
                    elif ene["nivel"] == 0: pantalla.blit(img_n2_ene0, (x, y))

        # UI: Textos de Vida y Enamorados en pantalla
        dibujar_texto(f"Vidas: {vidas}", fuente_chica, (255, 255, 255), 10, 10)
        dibujar_texto(f"Enamorados: {puntuacion_enamorados}", fuente_chica, (255, 100, 150), 10, 40)
        
        # INDICADOR VISUAL DEL SUPER PODER (K)
        segundos_restantes = 50 - ((tiempo_actual - ultimo_uso_k) // 1000)
        if segundos_restantes <= 0:
            dibujar_texto("Super K: ¡LISTO!", fuente_mini, (0, 255, 0), 10, 70)
        else:
            dibujar_texto(f"Super K: {segundos_restantes}s", fuente_mini, (200, 200, 200), 10, 70)

        if vidas <= 0:
            estado_juego = "GAMEOVER"

    # ESTADO 4: PANTALLA DE FIN DE JUEGO (GAMEOVER)
    elif estado_juego == "GAMEOVER":
        dibujar_texto("¡Fuiste Derrotado!", fuente_titulo, (255, 0, 0), 180, 150)
        dibujar_texto(f"Lograste enamorar a: {puntuacion_enamorados} caritas", fuente_menu, (255, 150, 150), 150, 250)
        dibujar_texto("> Volver a Jugar <", fuente_menu, (255, 255, 255), 250, 400)

    # Actualiza la pantalla y limita a 60 FPS (NO MODIFICAR)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()