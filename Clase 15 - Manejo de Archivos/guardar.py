### Guardar información en un archivo

### Dos formas 

### Forma 1 --- Menos utilizada

file = open("canciones.txt", "w") # El Open pide que le pasemos el "Path (absoluto o relativo)" del archivo y la forma "w"=Write, "r"=Read, etc.

file.write("Pimpollo - Chiquititas\n") # Si no hacemos el salto de línea "\n", se escribirá a continuación de lo que hay
file.write("Mi bestido azul - Cenicienta\n")
file.write("Welcome to the Paradise - Green Day\n")

# Con el "w", si el archivo no existe lo crea; si existe lo sobrescribe si tiene los permisos necesarios

file.close ### Si usamos este método es FUNDAMENTAL cerrar el archivo


### Forma 2 --- MAS UTILIZADO

with open("libros.txt", "w") as file_libros:
    file_libros.write("Harry Potter\n")
    file_libros.write("El Señor de los Anillos\n")

### Con esta forma no es necesario hacer el "CLOSE", ya que cuando termina el "With, automaticamente Python hace el "CLOSE"
