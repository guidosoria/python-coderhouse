### Desafío Tuplas -----------------------------

# Descripción de Actividad
# A partir de una variable llamada tupla, imprimir en pantalla de forma ordenada lo siguiente:
# - El último item de tupla
# - El número de ítems de tupla
# - La posición donde se encuentra el ítem "87" de tupla
# - Una lista con los tres ítems de tupla
# - Un ítem que haya en la posición 8 de tupla
# - El número de veces que el item "7" aparece en la tupla 

tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

# 1
print(tupla[-1])

# 2
print(len(tupla))

# 3
print(tupla.index(87))

# 4
print(tupla[-3:])

# 5
print(tupla.count(7))