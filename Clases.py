# ==========================================
# Actividad Formativa 2: App Simple en Línea
# Sistema orientado a objetos en Python
# ==========================================

class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo_inicial, pin):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial
        self.pin = pin

    def consultar_saldo(self):
        print("\n---> El saldo actual de ", self.titular, " es: $", self.saldo)
        return self.saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print("\n[OK] Se han depositado con exito: $", monto)
            print("---> Nuevo saldo de: $", self.saldo)
        else:
            print("\n[Error] El monto que desea depositar debe ser mayor a cero.")

    def retirar(self, monto):
        if monto <= 0:
            print("\n[Error] El monto a retirar debe ser mayor a 0.")

        elif monto <= self.saldo:
            self.saldo -= monto
            print("\n[OK] Se ha retirado con exito $", monto)
            print("---> Nuevo saldo de: $", self.saldo)
            return True
        else:
            print("[Error] Saldo insuficiente. Tu saldo es de: $", self.saldo)
            return False

    def verificar_pin(self, pin_ingresado):
        return self.pin == pin_ingresado


# =======================
#   (Menu interactivo)
# =======================
if __name__ == "__main__":
    print("========================================")
    print("      BIENVENIDO AL CAJERO AUTOMATICO   ")
    print("========================================")

    mi_cuenta = CuentaBancaria(
        titular= "Caleb Escobedo",
        numero_cuenta= "1234-5678-9102",
        saldo_inicial= 5000.00,
        pin= "4321"
    )

    pin_ingresado = input("Por favor, ingrese su PIN de seguridad: ")

    if mi_cuenta.verificar_pin(pin_ingresado):
        print("\n!Bienvenido/a ", mi_cuenta.titular,"!")

        activo = True
        while activo:
            print("\n--- MENU DE OPCIONES ---")
            print("1. Consultar saldo")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Salir")

            opcion = input("\nSeleccione una opcion (1, 4): ")
            if opcion == "1":
                mi_cuenta.consultar_saldo()

            elif opcion == "2":
                try:
                    monto = float(input("Ingrese el monto a depositar: $"))
                    mi_cuenta.depositar(monto)
                except ValueError:
                    print("\n[Error] Ingrese una cantidad numerica valida.")

            elif opcion == "3":
                try:
                    monto = float(input("Ingrese el monto a retirar: $"))
                    mi_cuenta.retirar(monto)
                except ValueError:
                    print("\n[Error] Ingrese una cantidad numerica valida.")

            elif opcion == "4":
                print("\nGracias por usar nuestro cajero automatico,", mi_cuenta.titular, "¡Hasta luego!")
                activo = False

            else:
                print("`[Opcion no valida] Seleccione una opcion del 1 al 4.")

    else:
        print("[Error] PIN invalido. Acceso denegado.")