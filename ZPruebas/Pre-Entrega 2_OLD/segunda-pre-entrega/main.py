from cliente import *
from producto import *

cliente1 = Cliente(
    input("Ingrese su nombre: "),
    input("Ingrese su apellido: "),
    input("Ingrese su documento: "),
    input("Ingrese su dirección: "),
)

listado_productos = [
    Producto("Remera", "Uniform", 1500),
    Producto("Shampoo", "Clear Men", 400),
    Producto("Pantalon", "Nike", 3000)
]
print("\n --- Bienvenido a COMPRAS.com! --- \nEstos son nuestros productos disponibles: ")
for indice, producto in enumerate(listado_productos):
    print(f"\t{indice} -   Producto: {producto.nombre}  Marca: {producto.marca}  Precio:  {producto.precio}")
print("\n")

opcion = int(input("Ingrese el número de producto que quiere comprar: "))
cantidad = int(input("Ingrese la cantidad que desea comprar: "))

try:
    item = listado_productos[opcion]
    cliente1.comprar(item, cantidad)
    cliente1.pagar(item, cantidad)
    print(f"El producto será enviado a la dirección {cliente1.direccion} a nombre de {cliente1.nombre} {cliente1.apellido} documento {cliente1.documento}")
except:
    print("\nAlgo salió mal! Revise la opción ingresada por favor")
