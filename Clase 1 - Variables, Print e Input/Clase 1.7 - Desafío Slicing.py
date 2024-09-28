### Desafía Slicing -----------

# Se tiene una cadena de texto, pero al revés. Al parecer contiene el nombre de un alumno, la nota
# de un examen y la materia

cadena = "sacitametaM ,5.8 ,otipeP ordeP"

# Pedro Pepito, 8.5, Matematicas

# 1 - Dar vuelta la cadena y asignarla a una variable llamada "cadena_volteada"
# 2 - Extraer nombre y apellido, almacenarlo en una variable que se llame "nombre_alumno"
# 3 - Extraer la nota y almacenarla en una variable llamada "nota"
# 4 - Extraer la materia y almacenarla en una variable llamada "materia"
# 5 - Mostrar en pantalla la siguiente estructura, usando la concatenación de cadenas:
# NOMBRE APELLIDO ha sacado un NOTA en MATERIA

cadena_volteada = cadena[::-1]
nombre_alumno = cadena_volteada[:12]
nota = cadena_volteada[14:17]
materia = cadena_volteada[19:]

print(str(nombre_alumno) + " ha sacado un " + str(nota) + " en " + str(materia))