# CONSIGNA: tarea para el hogar
# Reimplementar el desafío de las películas usando funciones 
# pensando que estas funciones se invocan desde el módulo 
# donde están definidas o pueden invocarse desde desde otros módulos.

def input_movies():
    """ This function returns a list with the duration in minutes of the movies """

    minutes = int(input("Ingresá la duración de una película  (0 para finalizar): "))
    movies_duration  = []
    while minutes != 0:
        movies_duration .append(minutes)
        minutes = int(input("Ingresá la duración de una película  (0 para finalizar): "))

    return movies_duration

def average_calculation(movies_duration):
    """ This function calculates the average of the lengths of the movies received by parameter.
    movies_duration: is a list with the duration in minutes of the movies
    """
    
    len_movies = len(movies_duration)
    average = 0 if len_movies == 0 else sum(movies_duration) / len_movies
    return average


def higher_than_average(movies_duration, average):
    total = 0
    for movie in movies_duration:
        if movie > average:
            total += 1 
    return total
           
