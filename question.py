import random
import sys #importé sys para poder hacer un exit status

questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    ("// Esto es un comentario","/* Esto es un comentario */","-- Esto es un comentario","# Esto es un comentario",),
    ("=", "==", "!=", "==="),
]

correct_answers_index = [1, 2, 0, 3, 1]
puntaje = 0 #inicializamos los puntos

#agregamos la ayuda dada para el inciso C
#reemplazamos random.choices por random.sample para que no se elija la misma pregunta más de una vez
questions_to_ask = random.sample(list(zip(questions,answers, correct_answers_index)), k=3)
#k = 3 indica que se tomaran tuplas, por lo que no es necesario utilizar for in range (3)
#se "igualan" (posicionalmente hablando) las listas, por lo que la pregunta 0 se corresponde con las respuestas en la posicion 0 y la opcion correcta de la posicion 0   
for pregunta, respuestas, correcta in questions_to_ask:
    #al no haber indices, se imprime directamente la variable de la estructura for
    print(pregunta) # print(questions[question_index])

    for i, answer in enumerate(respuestas): #imprimimos las posibles respuestas
        print(f"{i + 1}. {answer}")
   
    for intento in range(2):
       
        #ejecutamos la lectura input con un manejo de errores
        try:
            user_answer = int(input("Respuesta: ")) - 1
        except ValueError:
            print("Debes elegir un número")
            sys.exit(1)

        if user_answer == correcta: #correct_answers_index[question_index]
            print("¡Correcto!")
            puntaje += 1
            break
        #evaluamos que el numero este dentro del rango
        elif (user_answer < 0) or (user_answer > (len(respuestas)-1)): #(len(answers[question_index])-1))
            print("Respuesta no válida")
            sys.exit(1)
        #si esta dentro del rango, pero no es el numero se ejecuta el else
        else:
            print("Incorrecto. Intente de nuevo")
            puntaje = puntaje - 0.5

    else:
        print("Incorrecto. La respuesta correcta es:")
        print(f"{correcta+1}. {respuestas[correcta]}")
    print()
print(f"Usted ha obtenido un total de ",puntaje," puntos") #imprimimos el puntaje total
    
