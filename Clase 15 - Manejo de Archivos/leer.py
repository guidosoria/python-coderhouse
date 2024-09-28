with open("canciones.txt", "r") as file: # Si no le pongo el "r", por defecto en open ese valor es "r"
    contenido = file.read()
    print(contenido)

# Abrir un archivo línea a línea
with open("canciones.txt", "r") as file:
    for linea in file.readlines():
        print(linea)

# Puedo buscar una línea que contenga algo que yo quiera buscar: READLINES
with open("canciones.txt", "r") as file:
    for linea in file.readlines():
        if "Green" in linea:
            print(linea)

# Puedo traer la primer línea de un archivo
with open("canciones.txt", "r") as file:
    linea = file.readlines()
    print(linea)