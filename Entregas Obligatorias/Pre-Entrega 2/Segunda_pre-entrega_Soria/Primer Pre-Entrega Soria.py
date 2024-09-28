usuarios = {}
print("Bienvenido al Sistema")

# Función para registrar usuarios; se muestra un menú de opciones para que se puedan cargar usuarios hasta que se quiera finalizar con la carga
def registro():
    usuario = input("Nombre de usuario: ")
    # Se evalúa si el usuario ya existe en la base. Se pasa a "lower" el usuario para evitar el case sensitive en los usuarios: Juan = juan
    if usuario.lower() not in usuarios:
        contrasena = input("Contraseña: ")
        usuarios[usuario.lower()] = contrasena
    else:
        print("\n\nYa existe un usuario con ese nombre\n\n")
    print("\n")

# Función para mostrar los usuarios que hay disponibles en la base de datos para hacer login
def mostrar():
    print("Lista de usuarios dispobibles:  ")
    lista_usuarios = usuarios.keys()
    for clave in lista_usuarios:
        print(clave)
    print("\n")

# Función para realizar login en el sistema
def login():
    contador = 1
    print("\n\n")
    usuario = input("Ingrese al nombre de usuario para conectarse: ")
    # Se evalúa que el usuario exista en la base. Nuevamente se pasa a "lower" para evitar el case sensitive en los usuarios
    if usuario.lower() in usuarios:
        while contador <= 3:
            password = input("Ingrese el password: ")
            if password == usuarios[usuario.lower()]:
                print("\n\n¡¡¡Bienvenido al Sistema!!!\n\n")
                break
            else:
                print("\n\nLa clave es incorrecta\n\n")
                contador +=1
        else:
            print("\n\nLogin incorrecto: Se ha superado el máximo de intentos\n\n")
    else:
        print("\n\nEl usuario no existe")

while True:
    print("Ingrese una opción para continuar:\n")
    print("1: Crear nuevo registro\n2: Mostrar Usuarios\n3: Ingresar al Sistema\n4: Finalizar\n")
    option = input("Opción: ")
    if option == "1":
        registro()
    elif option == "2":
        mostrar()
    elif option == "3":
        login()
    elif option == "4":
        print("\nSaliendo del sistema...\n")
        exit()
    else:
        print("Opción Incorrecta, intente de nuevo")