import random

def jugar():
    nombre = input("¿Cuál es tu nombre? ")
    numero_secreto = random.randint(1, 100)
    max_intentos = 8

    print(f"\nHola {nombre}, ¡bienvenido a la versión 2.0!")
    print(f"Adivina el número (1-100). Tenés {max_intentos} intentos y un termómetro de ayuda.\n")

    # Usamos range para manejar los intentos automáticamente
    for intento in range(1, max_intentos + 1):
        try:
            # Capturamos el input y lo validamos en una sola línea
            usuario = int(input(f"Intento {intento}/{max_intentos} - Introduce tu número: "))
            
            if not (1 <= usuario <= 100):
                print("¡Te dije entre 1 y 100! Este intento te va a costar caro...")
        except ValueError:
            print("¡Eso no es un número! Perdiste un intento por distraído.")
            continue

        # Lógica de victoria
        if usuario == numero_secreto:
            print(f"\n¡BOOM! Grande {nombre}. Lo sacaste en el intento {intento}.")
            break
        
        # --- NOVEDAD: El Termómetro ---
        distancia = abs(numero_secreto - usuario)
        
        if distancia > 30:
            pista = "❄️ Estás CONGELADO"
        elif 10 <= distancia <= 30:
            pista = "⛅ Estás TIBIO"
        else:
            pista = "🔥 ¡TE ESTÁS QUEMANDO!"

        # Pista de dirección (mayor/menor)
        direccion = "mayor" if numero_secreto > usuario else "menor"
        
        print(f"{pista}. El número secreto es {direccion} que {usuario}.\n")

    else:
        # Este else pertenece al for: se ejecuta si el bucle termina sin un 'break'
        print(f"\nSe acabaron los intentos, {nombre}. El número era el {numero_secreto}.")

if __name__ == "__main__":
    jugar()