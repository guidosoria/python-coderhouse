### Mi Primer Programa -----------------

### CONSIGNA
# Trabajas en Coderhouse y te piden crear un programa que calcule la nota final de estudiantes
# del curso de Python. La nota se calcula basándonos en 3 notas previas de las cuales, cada una corresponde
# a un porcentaje distinto de la nota final. Los porcentajes son los siguientes:
# Nota 1 --> 20% del final
# Nota 2 --> 30% del final
# Nota 3 --> 50% del final

nota_1 = int(input("Ingrese la nota 1: "))
nota_2 = int(input("Ingrese la nota 2: "))
nota_3 = int(input("Ingrese la nota 3: "))

nota_final = ((nota_1*20 + nota_2*30 + nota_3*50) / 100)
print("Tu nota final es: " + str(nota_final))