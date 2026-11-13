# ==========================================
# Actividad Formativa 3: Herencia
# Sistema orientado a objetos en Python
# ==========================================

"""
CLASE BASE (Superrclase):
Define los atributos y metodos comunes (nombre, precio, stock)
que serán heredados y reutilizados por las subclases.
"""
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_detalles(self):
        """ Metodo de la clase base que será heredado y reutilizado por las subclases."""
        print("Producto: ", self.nombre, " | Precio: ", self.precio, " | Stock: ", self.stock)

# ==========================================
# CLASE DERIVADA 1 (Subclase)
# Implementa la herencia a partor de la clase base 'Producto'.
# ==========================================

class Electrodomestico(Producto):
    def __init__(self, nombre, precio, stock, consumo_watts):
        """super().__init__() reutiliza el constructor de la clase base."""
        super().__init__(nombre, precio, stock)

        """Atributo único y exclusivo de esta subclase."""
        self.consumo_watts = consumo_watts

    def verificar_energia(self):
        """Método exclusivo de la subclase Electrodomestico."""
        print("El aparato ", self.nombre, "consume ", self.consumo_watts, "W.")

# ==========================================
# CLASE DERIVADA 2 (Subclase)
# Otra clase derivada que reutiliza la estructura base.
# ==========================================

class Ropa(Producto):
    def __init__(self, nombre, precio, stock, talla, material):
        """Herencia de atributos generales llamando a la clase base."""
        super().__init__(nombre, precio, stock)

        """Atributos exclusivos de la subclase Ropa."""
        self.talla = talla
        self.material = material

    def mostrar_etiqueta(self):
        """Método exclusivo de la subclase Ropa."""
        print("Prenda ", self.nombre, " - Talla: ", self.talla, ", Material: ", self.material, ".")


# ==========================================
# PROGRAMA PRINCIPAL
# Instancia objetos de las clases derivadas y prueba la herencia.
# ==========================================

if __name__ == "__main__":
    print("=== PRUEBA DE HERENCIA Y REUTILIZACIÓN DE CÓDIGO ===\n")

    """Instanciación de un objeto de la clase derivada Electrodomestico."""
    tv = Electrodomestico("Pantalla Smart TV", 8500, 10, 120)
    tv.mostrar_detalles()   # Método heredado de la clase base Producto
    tv.verificar_energia()  # Método exclusivo de Electrodomestico

    print("-" * 50)

    """Instanciación de un objeto de la clase derivada Ropa."""
    camisa = Ropa("Camisa Casual", 450, 25, "L", "Algodon")
    camisa.mostrar_detalles() # Método heredado de la clase base Producto
    camisa.mostrar_etiqueta() # Método exclusivo de Ropa