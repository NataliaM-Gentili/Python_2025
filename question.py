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

for _ in range(3):
    
    question_index = random.randint(0, len(questions) - 1)
    
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")
    
    for intento in range(2):
       
        #ejecutamos la lectura input con un manejo de errores
        try:
            user_answer = int(input("Respuesta: ")) - 1
        except ValueError:
            print("Debes elegir un número")
            sys.exit(1)
        if user_answer == correct_answers_index[question_index]:
            print("¡Correcto!")
            puntaje += 1
            break
        #evaluamos que el numero este dentro del rango
        elif (user_answer < 0) or (user_answer > (len(answers[question_index])-1)):
            print("Respuesta no válida")
            sys.exit(1)
        #si esta dentro del rango, pero no es el numero se ejecuta el else
        else:
            print("Incorrecto. Intente de nuevo")
            puntaje = puntaje - 0.5
    else:
        print("Incorrecto. La respuesta correcta es:")
        print(answers[question_index]
    [correct_answers_index[question_index]])
    print()
print(f"Usted ha obtenido un total de ",puntaje," puntos") #imprimimos el puntaje total
    
