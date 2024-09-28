### Desafío Números

# Descripción de la actividad:
# En nuestro trabajo nos solicitan desarrollar un programa que permita calcular el promedio final
# de los equipos de fútbol de un torneo. Para ello debemos considerar tres aspectos:

# Jugaron 20 partidos durante el torneo
# Los partidos poseen diferente puntaje según el resultado; los partidos ganados 3, partido
# empatado 1 punto, partido perdido 0 puntos

# El promedio final resulta de la cantidad de puntos totales divididos la cantidad de partidos

# --------------------------------------

partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))
partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))

total_partidos = partidos_ganados + partidos_empatados + partidos_perdidos
total_puntos = partidos_ganados*3 + partidos_empatados*1 + partidos_perdidos*0
promedio = total_puntos / total_partidos
print(promedio)

print("El promedio de puntos por partido de su equipo es de: " + str(promedio))