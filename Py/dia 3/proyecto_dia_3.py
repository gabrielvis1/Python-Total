""" Este es un programa que analiza textos """

Texto = input("Ingresa tu texto para analizar: ").lower()

Letra1 = input("A continuaccion te pedire que me digas 3 letras para analizar."
               " por favor ingresa solo la primera letra: ").lower()

Letra2 = input("Ingresa la segunda letra: ").lower()

Letra3 = input("Ingresa la tercera letra: ").lower()

Texto_deletreado = list(Texto)

Texto_por_palabra = Texto.split()

print("Este es el analicis de tu texto\n"
      f"Tu primera letra \"{Letra1}\" aparece {Texto_deletreado.count(Letra1)} veces")

print(f"Tu segunda letra \"{Letra2}\" aparece {Texto_deletreado.count(Letra2)} veces")

print(f"Tu segunda letra \"{Letra3}\" aparece {Texto_deletreado.count(Letra3)} veces")

print(f"Tu texto tiene {len(Texto_por_palabra)} palabras")

print(f"Tu pimera letra del texto es {Texto_deletreado[0]}, y tu ultima es {Texto_deletreado[-1]}")

print(f"Este es el texto de las palabras invertidas\n"
      f"{' '.join(Texto_por_palabra[::-1])}")

Existe_python = "python" in Texto_por_palabra

Verdadero_falso = {True:"Si",
                   False:"No"}

print(f"Tu Texto tiene la palabra \"Python?\" = {Verdadero_falso[Existe_python]}")
