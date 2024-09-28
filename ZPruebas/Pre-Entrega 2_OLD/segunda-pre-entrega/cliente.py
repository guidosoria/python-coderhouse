# Modulo con la clase Cliente

class Cliente():
    def __init__(self, nombre, apellido, documento, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.direccion = direccion

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"

    def comprar(self, producto, cantidad):
        print(f"{self.nombre} {self.apellido} ha seleccionado comprar {cantidad} {producto.nombre} de {producto.marca} por ${producto.precio}")
    
    def pagar(self, producto, cantidad):
        print(f"{self.nombre} {self.apellido} ha pagado ${producto.precio * cantidad} por su compra")