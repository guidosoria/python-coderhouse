### TUPLAS ----------------------------------------

# Son coleeciones de datos, al igual que las listas, con la diferencia de que éstas son INMUTABLES
# Se utilizan para asegurarnos de que una coleccion determinada de datos no pueda cambiarse
# Python utiliza tuplas en algunas funciones para devolver resultados inmutables. A su vez, dependiendo de lo que
# queramos hacer, las tuplas pueden ser mas rápidas que las listas

### Declarar una tupla ------------
# Las tuplas se declaran de manera muy similar a la lista, solamente que con paréntesis, en lugar de corchetes

mi_tupla = (1, 2, 3, 4)
otra_tupla = ("Hola", "?", "como", "estás", "?" )

#Para declarar una tupla de un único valor hay que declararla de la siguiente forma:
tupla_valor_unico = (2,) # Si no ponemos la "," al final Python interpretará que es un numero entero y no una tupla

# Al igual que las listas, las tuplas no tienen restricción de tipos de datos de los ítems
mi_variable = "una variable"
datos = (1, "cadena", -0.4, mi_variable)
print(datos)

### Índice y Slicing
# Al igual que las listas, las tuplas funcionan igual con el índice y el slicing
datos = (1, "2", [3, "4"], (5, "6"))
print(datos[1])
print(datos[-1])
print(datos[2:])

### Concatenación
# Las tuplas también se pueden concatenar
# Importante: Las tuplas no tienen la función append(), pero podemos agregar elementos con la concatenación
numeros = (1, 2, 3, 4)
numeros += (5, 6, 7, 8)
print(numeros)

### Mutabilidad
# Las tuplas no son mutables, por esto en caso de que queramos reasignar otro valor a un items nos dará error

# mi_tupla = (1, 2, 3, 4)
# mi_tupla[2] = 5 # Esto nos arrojará un error

### FUNCIONES DE TUPLAS -----------------------------------------

# Len - Al igual que en las listas nos dice la cantidad de items que tiene la tupla
numeros = (1, 2, 3, 4)
print(len(numeros))

# Count - Al igual que en las listas, esta función cuenta el número de veces que un item se repite en la tupla
numeros = (1, 3, 5, 1, 3, 1, 2)
print(numeros.count(1))

# Índice - Igual que con las listas, busca un ítem dado y nos dice en que índice se encuentra
numeros = (1, 2, 3, 4)
print(numeros.index(2))

# Anidación - En Python una tupla y una lista pueden ser anidadas, lo que significa que pueden contener una lista o una tupla dentro de sí respectivamente
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
resultado = [a, b, c]
print(resultado) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(resultado[0]) # [1, 2 ,3]
print(resultado[0][1]) # 2




### TRANSFORMACIÓN DE COLECCIONES -------------------------------------
# En Python, podemos convertir una lista a una tupla haciendo uso de la funcion "tuple()", y a su vez, 
# podemos hacer lo mismo pero a la inversa, es decir, convertir una tupla a lista usando "list()"
numeros = (1, 2, 3, 4)
numeros = list(numeros)
print(numeros) # [1, 2, 3, 4]

datos = [1, -5, 123.34, "Una Cadena", "Otra Cadena"]
datos = tuple(datos)
print(datos) # (1, -5, 123.34, 'Una Cadena', 'Otra Cadena')
