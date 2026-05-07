import time
import datetime

print("--- 1. OBTENIENDO LA HORA ACTUAL ---")
# Obtener el momento exacto actual
momento_actual = datetime.datetime.now()

# Guardar partes específicas en variables
hora_actual = momento_actual.hour
minuto_actual = momento_actual.minute
segundo_actual = momento_actual.second

print(f"El reloj marca las: {hora_actual}:{minuto_actual}:{segundo_actual}")
# También puedes sacar la fecha
anio = momento_actual.year
mes = momento_actual.month
dia = momento_actual.day
print(f"Fecha de hoy: {dia}/{mes}/{anio}\n")

print("--- 2. PAUSANDO EL TIEMPO ---")
print("Iniciando una cuenta regresiva de 3 segundos...")

# time.sleep() pausa la ejecución del código
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)

print(f"¡Despegue! El cohete salió a las {datetime.datetime.now().strftime('%H:%M:%S')}\n")

print("--- 3. VIAJES EN EL TIEMPO (TIMEDELTA) ---")
hoy = datetime.datetime.now()

# ¿Qué fecha será exactamente en 10 días?
en_diez_dias = hoy + datetime.timedelta(days=10)
print(f"En 10 días será: {en_diez_dias.date()}")

# ¿Qué fecha fue hace 3 semanas y 12 horas?
en_el_pasado = hoy - datetime.timedelta(weeks=3, hours=12)
print(f"Hace 3 semanas y 12 horas fue: {en_el_pasado}")

# Calcular cuánto falta para una fecha específica
fin_de_anio = datetime.datetime(hoy.year, 12, 31, 23, 59, 59)
tiempo_restante = fin_de_anio - hoy

print(f"Faltan {tiempo_restante.days} días para que termine el año.\n")

print("--- 4. TRADUCIENDO FECHAS (STRPTIME Y STRFTIME) ---")

# De Objeto a Texto bonito (strftime = String Format Time)
# %A = Día de la semana, %d = Día, %B = Mes, %Y = Año
ahora = datetime.datetime.now()
fecha_formateada = ahora.strftime("%A, %d de %B de %Y")
print(f"Formato elegante: {fecha_formateada}")

# De Texto a Objeto (strptime = String Parse Time)
# Imagina que recibes este dato de un formulario web
fecha_texto = "15-08-2023 14:30"
formato_esperado = "%d-%m-%Y %H:%M"

fecha_traducida = datetime.datetime.strptime(fecha_texto, formato_esperado)
print(f"Python ahora entiende esta fecha: {fecha_traducida} (Año: {fecha_traducida.year})")
