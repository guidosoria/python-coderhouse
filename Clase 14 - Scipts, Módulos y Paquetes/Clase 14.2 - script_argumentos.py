import sys # sys es una librería (vermos mas adelante), que nos permite entre otras cosas acceder a los argumentos
print(sys.argv) # Imprime todos los argumentos

print(sys.argv[1]) # También podemos acceder a los argumentos por su índice. El índice 0 es el nombre del script

print(f"El script tiene {len(sys.argv)} argumentos, contando el nombre del script [0]")

for r in sys.argv:
    print(r)