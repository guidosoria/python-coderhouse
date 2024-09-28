#Módulo de clase Producto

class Producto():
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca

    def __str__(self):
        return f"Producto: {self.nombre}"