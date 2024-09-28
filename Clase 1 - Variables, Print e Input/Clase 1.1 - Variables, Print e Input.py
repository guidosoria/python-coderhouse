### Números y cadenas de caracteres ### ------------------------

## Función "print()" ----------------------
# Se utiliza para mostrar información en la pantalla de la computadora

print("Hola Mundo")

### Variable --------------------
# En algunos lenguajes de programación, las variables se pueden entender como "cajas" en las que se guardan los datos
# Pero en Python las variables son "etiquetas" que hacen referencia a los datos (que se guardan en "cajas llamadas objetos")

# Por cada dato que se crea en un programa; Python crea un "objeto" que lo contiene
# Cada objeto tiene:
# 1 - Identificador Único --> Un número entero, distinto para cada objeto; lo que permite referirse a él sin ambiguedades
# 2 - Tipo de Datos --> Entero, Decimal, String, etc
# 3 - Un Valor --> El propio dato

# Las variables en Python no guardan los datos, sino que son simples nombres para poder hacer referencia a esos objetos
# En Python, si escribimos la instrucción "a = 2"; se creará el objeto "2"
# Ese objeto tendrá un identificador único que se asigna en el momento de la creación y se conserva a lo largo del programa
# Se asocia el nombre "a" al objeto número entero "2"

# Declaración de variables
nombre = "Guido"
print(nombre)

## Función input() ---------------------------
# Se utiliza para solicitar información al usuario
# Cuando se llama a input el programa se detiene y espera que el usuario escriba algo; esto puede ser almacenado en una variable

apellido = input("Cuál es tu apellido: ")
print(apellido)


