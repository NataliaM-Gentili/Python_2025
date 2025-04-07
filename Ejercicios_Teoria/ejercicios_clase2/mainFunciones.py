# CONSIGNA: tarea para el hogar
# Reimplementar el desafío de las películas usando funciones 
# pensando que estas funciones se invocan desde el módulo 
# donde están definidas o pueden invocarse desde desde otros módulos.

import funciones

movies = funciones.input_movies()
average = funciones.average_calculation(movies)
print(f"Las duraciones cargadas son: {movies}")
print(f"El promedio de minutos es de {average:.2f}") #:.2f recorta el float a dos decimales
total = funciones.higher_than_average(movies, average)
print(f"Hay {total} peliculas que superan el promedio de minutos")

