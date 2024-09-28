### DESAFÍO DE LISTAS ---------------------------------------
# Crea dos listas "lista_1" y "lista_2" con cualquier elemento que quiera
# Realiza los siguientes puntos usando las funciones integradas ya vistas y el método slice[:]
# Imprime la lista correspondiente luego de cada punto

# 1 Añade a la lista_1 el <int> 456789 y luego el <str> "Hola Mundo"
# 2 Añade a la lista_2 el <str> "Hola y Adiós", y luego el <int> 5555
# 3 Genera una "lista_3" con todos los elementos de la "lista_1" sin considerar el último elemento [:]
# 4 Genera una lista "lista_4" con todos los elementos de la "lista_2" menos el primero y el último elemento [:]
# 5 Finalmente, genera una lista_5 con los elementos de la lista_4 y de la lista_3

lista_1 = ["Momocho", 2024, 1994, "Mayo"]
lista_2= ["Mercadolibre", "Networking", 2023, 29]
print(lista_1)
print(lista_2)

#1

lista_1.append(456789)
lista_1.append("Hola Mundo")
print(lista_1)

#2
lista_2.append("Hola y Adiós")
lista_2.append(5555)
print(lista_2)

#3
lista_3 = lista_1[:-1]
print(lista_3)

#4
lista_4 = lista_2[1:-1]
print(lista_4)

#5
lista_5 = lista_4 + lista_3
print(lista_5)