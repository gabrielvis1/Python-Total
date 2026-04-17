# ==========================================================
# GUÍA MAESTRA DE VARIABLES - REFERENCIA RÁPIDA
# ==========================================================

# 1. CREACIÓN Y ASIGNACIÓN
# En Python, "=" significa ASIGNAR (guardar), no "igual a".
nombre = "María"    # Creamos la etiqueta 'nombre' y le asignamos "María" 
edad = 25           # Guardamos un entero 
precio = 99.99      # Guardamos un flotante 


# 2. REGLAS DE ORO PARA NOMBRAR 
# ✅ BIEN: mi_variable, usuario2, _secreto (usa snake_case)
# ❌ MAL: 1nombre (no empezar con número), mi variable (sin espacios), if (palabra reservada)
puntos_totales = 100 # Nombre descriptivo y válido 


# 3. REASIGNACIÓN Y TIPADO DINÁMICO [cite: 3, 4]
# Podés cambiar el valor y el TIPO de una variable en cualquier momento.
dato = 100          # Ahora es un número (int) [cite: 4]
dato = "Cien"       # Ahora la misma variable es un texto (str) [cite: 4]

# Actualización con operadores abreviados 
puntos = 10
puntos += 5         # Es lo mismo que: puntos = puntos + 5 
print("Puntos actualizados:", puntos) # Resultado: 15


# 4. USO CON PRINT() Y CONCATENACIÓN 
usuario = "Carlos"
# Con comas: agrega espacio automático y acepta números 
print("Hola,", usuario, "tienes", 30, "años") 
# Con concatenación (+): solo para strings, sino da error 
print("Bienvenido " + usuario + "!") 


# 5. VARIABLES E INPUT() 
# Guardamos la respuesta del usuario en una variable
mascota = input("¿Cómo se llama tu mascota? ") # 
print("Qué lindo nombre tiene " + mascota)


# 6. ASIGNACIÓN MÚLTIPLE Y TRUCOS [cite: 7]
x, y, z = 1, 2, 3   # Crear tres variables a la vez [cite: 7]
a = b = c = 0       # El mismo valor para todas [cite: 7]

# Intercambio (swap) - Truco de Python [cite: 7]
color1, color2 = "Rojo", "Azul"
color1, color2 = color2, color1 # Ahora color1 es Azul y color2 es Rojo [cite: 7]


print("\n--- PROGRAMA FINALIZADO ---")