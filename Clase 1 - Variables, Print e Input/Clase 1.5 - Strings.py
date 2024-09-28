### Cadenas de texto <str> ------------------------------
# Las cadenas de texto o strings son un tipo de datos compuestos por secuencias de caracteres que representan texto
# El tipo de dato de los strings es "str" y se delimintan mediante comillas dobles " " o comillas simples ' '

cadena1 = "Esto es una cadena de texto"
cadena2 = 'Esto tambien es una cadena de texto'

# En el caso de que querámos usar comillas dentro de una cadena de texto tenemos distintas opciones para hacerlo:

# Lo más simple es encerrar el texto entre las comillas que no necesitamos usar en el texto, y luego dentro usar las otras
cadena_con_comillas = 'Este texto tiene "comillas"'
# Otra opción es utilizar las mismas comillas en todo momento pero utilizar una barra invertida antes de las comillas
# que son parte del texto para escapear su significado
ccadena2_con_comillas = "Este texto \"también tiene\" comillas"

### Sáltos de línea
# Si querémos imprimir un string con saltos de líneas podemos utilizar "\n" para realizar el salto de línea
print("Esto es un texto\ncon un salto de línea")
# Otra forma de crear strings de mas de una línea es utilizar comillas triples
print("""Esto también
es un texto
con salto de línea""")
# Que pasa si nuestro texto tiene "/n" en su texto; por ejemplo una ruta de directorio como "C:\nombre\directorio" ??
# r --> raw string

print(r"C:\nombre\directorio")

### Longitud de Strings --> función len()
# La función len() nos permite saber cuál es la longitud de un string
palabra = "Python"
len(palabra)

frase = "Hola ¿Cómo están?"
len(frase)

### Indexación de Strings --------------
# Cada uno de los caracteres (incluídos los espacios) tiene asignado un índice
# Este índice nos permite seleccionar su caracter asociado haciendo referencia a él entre corchetes [] 
# en el nombre de la variable que almacena la cadena
# Si consideramos el órden de izquierda a derecha, el primer índice es 0 para el primer caracter
# También podemos considerar el órden de derecha a izquierda, donde el último caracter comienza con -1, penúltimo -2 y así..

cadena = "Esta es una cadena de texto"
primer_caracter = cadena[0] # --> "E"
ultimo_caracter = cadena[-1] # --> "o"
print("El primer caracter de la cadena es " + primer_caracter + " y el último es " + ultimo_caracter)

### Slicing - Rebanar strings
# Otra función de los strings que podemos utilizar es seleccionar solamente una parte de las cadenas
# para ello se usa la notación [inicio:fin:paso]
# inicio: Es el primer caracter de la porción que queremos seleccionar
# fin: Es el índice del último caracter (no incluído) de la porción que queremos seleccionar; es decir el último caracter+1
# paso: Indica cada cuantos caracteres seleccionamos entre las posiciones de inicio y fin

print(cadena[0:8:2])