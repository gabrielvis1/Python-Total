"""
Archivo: ejemplos_regex.py
20 ejemplos prácticos de Expresiones Regulares (Regex) en Python.
"""

import re

print("=" * 50)
print(" 🕵️‍♂️ BÚSQUEDAS COMPLEJAS (Mails, Teléfonos, Direcciones)")
print("=" * 50)

# 1. BUSCAR CORREOS ELECTRÓNICOS
# Explicación: 
# [a-zA-Z0-9._-]+ -> Busca letras, números, puntos, guiones bajos o medios antes del @. El '+' significa "uno o más".
# @ -> Busca el símbolo arroba literal.
# [a-zA-Z0-9.-]+ -> Busca el dominio (ej: gmail, hotmail).
# \. -> Busca un punto literal (se usa la barra \ para que no se confunda con el comodín).
# [a-zA-Z]{2,} -> Busca la extensión (com, org, net) que tenga al menos 2 letras.
texto_mail = "Contactanos en info_ventas@mi-empresa.com o en soporte@ayuda.net"
patron_mail = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
mails_encontrados = re.findall(patron_mail, texto_mail)
print(f"1. Mails encontrados: {mails_encontrados}")

# 2. BUSCAR NÚMEROS DE TELÉFONO
# Explicación:
# \+? -> El símbolo + es opcional (por el cuantificador '?').
# \d{2,3} -> Busca entre 2 y 3 dígitos (código de país).
# [\s-]? -> Busca un espacio o un guion de forma opcional.
# \d{4} -> Busca exactamente 4 dígitos.
texto_tel = "Llamame al +54 11-4321-8765 o al 011 5555-4444"
patron_tel = r"\+?\d{2,3}[\s-]?\d{2,4}[\s-]?\d{4}"
telefonos_encontrados = re.findall(patron_tel, texto_tel)
print(f"2. Teléfonos encontrados: {telefonos_encontrados}")

# 3. BUSCAR DIRECCIONES (Calle y Número)
# Explicación:
# [A-Z][a-z]+ -> Una letra mayúscula seguida de letras minúsculas (ej: Calle, Avenida, San).
# \s -> Un espacio en blanco.
# \d{1,5} -> Un número de calle que tenga entre 1 y 5 dígitos.
texto_dir = "El local está en Avenida Cabildo 2500 y la sucursal en Calle Falsa 123."
patron_dir = r"[A-Z][a-z]+\s[A-Z]?[a-z]*\s?\d{1,5}" 
direcciones_encontradas = re.findall(patron_dir, texto_dir)
print(f"3. Direcciones encontradas: {direcciones_encontradas}")


print("\n" + "=" * 50)
print(" 🔢 CUANTIFICADORES (Controlan la cantidad de repeticiones)")
print("=" * 50)

# 4. CUANTIFICADOR '*' (Cero o más veces)
# Busca la letra 'o' repetida 0, 1 o infinitas veces.
texto_risa = "jajaja, jojo, joooooo, j, ja"
patron_asterisco = r"jo*" # Encuentra 'j', 'jo', 'jooo', etc.
asterisco_result = re.findall(patron_asterisco, texto_risa)
print(f"4. Uso del asterisco (*): {asterisco_result}")

# 5. CUANTIFICADOR '+' (Una o más veces)
# A diferencia del *, el + exige que el carácter esté AL MENOS una vez.
texto_grito = "¡Gooooool! ¡Gl!"
patron_mas = r"Go+l" # Encuentra "Gol", "Gooool", pero NO "Gl"
mas_result = re.findall(patron_mas, texto_grito)
print(f"5. Uso del más (+): {mas_result}")

# 6. CUANTIFICADOR '?' (Cero o una vez - OPCIONAL)
# Hace que la letra anterior sea opcional. Excelente para variaciones de ortografía.
texto_color = "The color is red, but in UK they say colour."
patron_interrogacion = r"colou?r" # La 'u' puede estar o no.
interrogacion_result = re.findall(patron_interrogacion, texto_color)
print(f"6. Uso del opcional (?): {interrogacion_result}")

# 7. CUANTIFICADOR '{}' (Cantidad exacta)
# Busca exactamente una cantidad de repeticiones. 
texto_codigos = "Mis pines son 123, 4567, 89 y 9999"
patron_llaves = r"\b\d{4}\b" # '\b' es un límite de palabra. Busca exactamente 4 dígitos seguidos.
llaves_result = re.findall(patron_llaves, texto_codigos)
print(f"7. Cantidad exacta ({{}}): {llaves_result}")


print("\n" + "=" * 50)
print(" 🔠 OTROS EJEMPLOS ÚTILES (Clases y Grupos)")
print("=" * 50)

# 8. CLASES DE CARACTERES '[]'
# Busca cualquiera de los caracteres que estén dentro de los corchetes.
texto_vocales = "Murcielago"
patron_corchetes = r"[aeiou]" # Busca solo las vocales
corchetes_result = re.findall(patron_corchetes, texto_vocales)
print(f"8. Buscar vocales ([]): {corchetes_result}")

# 9. INICIO '^' Y FIN '$' (Anclas)
# Verifican si un texto COMPLETO empieza o termina de cierta forma.
texto_archivo = "reporte_ventas_2023.pdf"
patron_fin = r"\.pdf$" # Comprueba si termina exactamente en ".pdf"
es_pdf = bool(re.search(patron_fin, texto_archivo))
print(f"9. ¿El archivo termina en .pdf? ($): {es_pdf}")

# 10. GRUPOS Y ALTERNATIVAS '()' y '|'
# El símbolo '|' funciona como un "OR" (O lógico).
texto_mascotas = "Tengo un perro, un gato y un loro."
patron_or = r"(perro|gato|conejo)" # Busca perro, gato o conejo.
or_result = re.findall(patron_or, texto_mascotas)
print(f"10. Buscar alternativas (|): {or_result}")


print("\n" + "=" * 50)
print(" 📅 VALIDACIONES Y EXTRACCIONES FRECUENTES")
print("=" * 50)

# 11. BUSCAR FECHAS (dd/mm/aaaa o dd-mm-aaaa)
# Explicación:
# \d{2} -> Busca exactamente 2 dígitos para día y mes.
# [/-] -> Acepta una barra "/" o un guion "-".
# \d{4} -> Busca exactamente 4 dígitos para el año.
texto_fechas = "Las fechas importantes son 05/05/2026, 24-12-2025 y 2026/05/05."
patron_fechas = r"\b\d{2}[/-]\d{2}[/-]\d{4}\b"
fechas_result = re.findall(patron_fechas, texto_fechas)
print(f"11. Fechas encontradas: {fechas_result}")

# 12. VALIDAR UN DNI ARGENTINO
# Explicación:
# ^ y $ -> Obligan a que el texto completo cumpla el patrón.
# \d{7,8} -> Acepta 7 u 8 dígitos.
dni = "42123456"
patron_dni = r"^\d{7,8}$"
dni_valido = bool(re.fullmatch(patron_dni, dni))
print(f"12. ¿El DNI es válido?: {dni_valido}")

# 13. BUSCAR PATENTES ARGENTINAS
# Explicación:
# [A-Z]{3}\s?\d{3} -> Formato viejo: ABC 123 o ABC123.
# [A-Z]{2}\s?\d{3}\s?[A-Z]{2} -> Formato nuevo: AB 123 CD o AB123CD.
texto_patentes = "Autos vistos: ABC 123, AA123BB, XY 987 ZT y A123BCD."
patron_patentes = r"\b(?:[A-Z]{3}\s?\d{3}|[A-Z]{2}\s?\d{3}\s?[A-Z]{2})\b"
patentes_result = re.findall(patron_patentes, texto_patentes)
print(f"13. Patentes encontradas: {patentes_result}")

# 14. BUSCAR URLS
# Explicación:
# https? -> Acepta "http" o "https".
# :// -> Busca los símbolos literales de una URL.
# [^\s]+ -> Toma todo hasta encontrar un espacio.
texto_urls = "Visitá https://python.org o http://mi-sitio.com/tutorial?id=5"
patron_urls = r"https?://[^\s]+"
urls_result = re.findall(patron_urls, texto_urls)
print(f"14. URLs encontradas: {urls_result}")

# 15. BUSCAR HASHTAGS
# Explicación:
# # -> Busca el numeral literal.
# \w+ -> Busca letras, números o guiones bajos una o más veces.
texto_hashtags = "Aprendiendo #Python #Regex_2026 y #programacion"
patron_hashtags = r"#\w+"
hashtags_result = re.findall(patron_hashtags, texto_hashtags)
print(f"15. Hashtags encontrados: {hashtags_result}")

# 16. BUSCAR USUARIOS DE REDES SOCIALES
# Explicación:
# @ -> Busca el arroba literal.
# [a-zA-Z0-9_]{3,15} -> Usuario de 3 a 15 caracteres alfanuméricos o guiones bajos.
texto_usuarios = "Escribile a @ana_dev, @PythonFan2026 o a @x."
patron_usuarios = r"@[a-zA-Z0-9_]{3,15}\b"
usuarios_result = re.findall(patron_usuarios, texto_usuarios)
print(f"16. Usuarios encontrados: {usuarios_result}")


print("\n" + "=" * 50)
print(" 🛠️ REEMPLAZOS, GRUPOS Y FLAGS")
print("=" * 50)

# 17. REEMPLAZAR ESPACIOS REPETIDOS
# Explicación:
# \s+ -> Busca uno o más espacios, saltos de línea o tabulaciones.
texto_desordenado = "Python     es   muy      claro"
patron_espacios = r"\s+"
texto_limpio = re.sub(patron_espacios, " ", texto_desordenado)
print(f"17. Texto con espacios corregidos: {texto_limpio}")

# 18. OCULTAR PARTE DE UN EMAIL
# Explicación:
# ([a-zA-Z0-9._-]{2}) -> Captura los primeros 2 caracteres del usuario.
# [a-zA-Z0-9._-]+ -> Captura el resto del usuario para ocultarlo.
# (@...) -> Captura el dominio para conservarlo.
email_privado = "cliente.importante@gmail.com"
patron_ocultar_mail = r"([a-zA-Z0-9._-]{2})[a-zA-Z0-9._-]+(@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
email_oculto = re.sub(patron_ocultar_mail, r"\1***\2", email_privado)
print(f"18. Email oculto: {email_oculto}")

# 19. USAR GRUPOS CON NOMBRE
# Explicación:
# (?P<nombre>...) -> Guarda una parte del resultado con un nombre.
texto_producto = "Código: LAP-2026, Producto: Notebook"
patron_producto = r"Código:\s(?P<codigo>[A-Z]{3}-\d{4}),\sProducto:\s(?P<producto>[A-Za-z]+)"
producto_match = re.search(patron_producto, texto_producto)
if producto_match:
    print(f"19. Código: {producto_match.group('codigo')} | Producto: {producto_match.group('producto')}")

# 20. BUSCAR SIN IMPORTAR MAYÚSCULAS O MINÚSCULAS
# Explicación:
# re.IGNORECASE permite encontrar coincidencias aunque cambie el uso de mayúsculas.
texto_lenguajes = "Me gusta python, PYTHON y Python."
patron_python = r"python"
python_result = re.findall(patron_python, texto_lenguajes, flags=re.IGNORECASE)
print(f"20. Coincidencias ignorando mayúsculas: {python_result}")

