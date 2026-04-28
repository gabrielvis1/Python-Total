""" Este es una cuenta bancaria """

class Persona:
    """Clase base para representar a cualquier persona."""
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Cliente(Persona):
    """Clase que representa a un cliente bancario, heredando de Persona."""
    def __init__(self, nombre, apellido, edad, numero_cuenta, balance=0, credito=0):
        # Usamos super() para no repetir el código de Persona
        super().__init__(nombre, apellido, edad)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
        self.credito = credito

    def __str__(self):
        """Método especial para imprimir los datos del cliente de forma prolija."""
        return (f"\n{'='*30}\n"
                f"DATOS DEL CLIENTE\n"
                f"{'='*30}\n"
                f"Nombre: {self.nombre} {self.apellido}\n"
                f"Edad: {self.edad}\n"
                f"Nro. Cuenta: {self.numero_cuenta}\n"
                f"Balance: ${self.balance:.2f}\n"
                f"Límite de Crédito: ${self.credito}\n"
                f"{'='*30}")

    def depositar(self):
        """Permite sumar dinero al balance actual."""
        monto = validar_monto("Ingrese el monto a depositar: $")
        self.balance += monto
        print(f"\n✅ Depósito exitoso. Nuevo balance: ${self.balance:.2f}")

    def retirar(self):
        """Permite restar dinero, validando que no exceda el balance."""
        monto = validar_monto("Ingrese el monto a retirar: $")
        if monto > self.balance:
            print("\n❌ OPERACIÓN DENEGADA: Fondos insuficientes.")
            print(f"Su balance actual es de: ${self.balance:.2f}")
        else:
            self.balance -= monto
            print(f"\n✅ Retiro exitoso. Nuevo balance: ${self.balance:.2f}")

def validar_monto(mensaje):
    """Asegura que el usuario ingrese un número válido y positivo."""
    while True:
        try:
            monto = float(input(mensaje))
            if monto < 0:
                print("Por favor, ingrese un número positivo.")
                continue
            return monto
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número (ej: 500.50).")

def crear_cliente():
    """Pide los datos iniciales y devuelve una instancia de Cliente."""
    print("\n--- REGISTRO DE NUEVO CLIENTE ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    while True:
        try:
            edad = int(input("Edad: "))
            break
        except ValueError:
            print("Error: La edad debe ser un número entero.")

    # Generamos un número de cuenta ficticio para el ejercicio
    nro_cuenta = "CTA-789456"
    return Cliente(nombre, apellido, edad, nro_cuenta)

def inicio():
    """Función principal que controla el flujo del programa."""
    print("*" * 40)
    print("BIENVENIDO AL SISTEMA BANCARIO DIGITAL")
    print("*" * 40)

    # Creamos el objeto cliente
    usuario = crear_cliente()
    opcion = ""
    while opcion != "S":
        print(usuario) # Esto llama automáticamente al método __str__
        print("\nOPCIONES DISPONIBLES:")
        print("[D] Depositar")
        print("[R] Retirar")
        print("[S] Salir")
        opcion = input("\nSeleccione una opción: ").upper()
        if opcion == "D":
            usuario.depositar()
        elif opcion == "R":
            usuario.retirar()
        elif opcion == "S":
            print(f"\nGracias por operar con nosotros, {usuario.nombre}. ¡Hasta pronto!")
        else:
            print("Opción no válida. Intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    inicio()
