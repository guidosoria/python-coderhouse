### LISTAS ------------------------------------

# Las listas son un tipo de datos el cual se describe como una lista de ítems separados por coma y
# contenido entre dos corchetes

mi_lista = [-11, 20, 3 ,41]
otra_lista = ["Hola", "como", "estás", "?"]

# En otros lenguajes, las listas tienen como restricción que pueden contener solamente un tipo de datos.
# En Python, no existe esta restricción por lo que podemos tener una lista heterogenea que contenga;
# números, variables, strings, etc o incluso otras listas o tipos de datos dentro de ella

mi_otra_lista = ["cadena", 1000, 12.34, 0, "otra cadena"]
print(mi_otra_lista)

### Indice de las listas -----------
# Las listas son muy parecidas a los strings ya que funcionan igual respecto a índice y slicing
# Ejemplo:
datos = [1, -5, 123, 34, "Una cadena", "Otra cadena", "Pepito"]
print(datos[0]) # 1
print(datos[-1]) # 'Pepito'
print(datos[-2:]) # ['Otra cadena', 'Pepito']

### Concatenación de listas ----------
# Otro punto en el que se parecen a los strings es que ambos se pueden concatenar. Ejemplo:
datos = [1, -5, 123, 34, "Una cadena", "Otra cadena", "Pepito"]
datos += [0, "cadena nueva", -53231]
print (datos)
numeros = [1, 2, 3, 4]
numeros += [5, 6, 7, 8]
print(numeros)

### Propiedad Mutable -----------
# Algo en lo que son diferentes de los strings es que los strings son INMUTABLES pero las listas son MUTABLES

pares = [2, 4, 5, 8, 10]
pares[2] = 6
print(pares) #[2, 4, 6, 8, 10]

### Funciones de las listas ------------
# Las listas en Python tienen muchas funciones para utilizar, entre todas ellas vamos a nombrar las más relevantes

# Append - Permite agregar un nuevo ítem al final de una lista
pares.append(12) # [2, 4, 5, 8, 10, 12]
print(pares)

# Len - Nos permite saber la longitud de una lista, es decir, la cantidad de ítems dentro de la misma
longitud = len(pares)
print(longitud)

# Pop - Elimina un ítem de una lista sin modificar el resto
# Si no indicamos un índice, se elimina el último elemento de la lista
pares.pop()
print(pares)
#Podemos indicar un índice "lista.pop(índice)" para especificar el elemento que queremos eliminar
pares.pop(1)
print(pares)

# Count - Cuenta el número de veces que se repite un elemento en una lista
numeros = [1, 2, 1, 3, 1, 4, 1]
print(numeros.count(1)) # En este caso "1" indica el valor que quiero saber que se repita, no el índice 1

# Índice - Busca un elemento y nos dice en qué índice se encuentra
print(numeros.index(4)) # Me dirá en qué indice tengo el valor 4
# Si se intenta buscar un valor fuera de la lista, nos datá un error de que el valor no se encontró. Y
# si el valor está mas de una vez en la lista nos arrojará el primer índice donde lo encontró

# Insert - Nos permite agregar un nuevo item a la lista indicándole en que índice queremos que se inserte y su valor; esto desplaza los que ya están
my_list = [1, 2, 3, 4]
my_list.insert(2, "Nuevo Item")
print(my_list)