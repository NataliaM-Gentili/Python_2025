import csv
from programasJuegos import tictactoe, hangman, reverse
import datetime

def registrar_juego(name):
    datetime_actual = datetime.datetime.now()
    # Formatear la fecha y hora para guardarlo de manera legible
    fecha_hora_str = datetime_actual.strftime("%Y-%m-%d %H:%M:%S")
    
    # 'a' es modo agregar (append)
    # considero que el mejor formato es .csv contemplando que se podría usar
    # para la base de datos del juego, registrando (por ejemplo) 
    # la cantidad de juegos por dia
    with open("registros_juegos.csv", mode="a", newline="") as archivo:
        # Guardar el nombre del juego y la fecha y hora
        # Si el archivo está vacío, escribir la cabecera
        writer = csv.writer(archivo)
        # encabezado
        if archivo.tell() == 0:
            writer.writerow(["Nombre del Juego", "Fecha y Hora"])
        writer.writerow([name, fecha_hora_str])
        
    print(f"El juego '{name}' fue registrado en {fecha_hora_str}")
def fun():
    sigo_jugando = True
    while sigo_jugando:

        print("""
          Elegí con qué juego querés jugar:
              1.- Ahorcado
              2.- Ta-TE-TI
              3.- Otello1
              4.- Salir""")

        opcion = int(input(" - "))
        match opcion:
            case 1: 
                registrar_juego("hangman")
                hangman.main()
            case 2: 
                registrar_juego("tictactoe")
                tictactoe.main()
            case 3:
                registrar_juego("reverse")
                reverse.main()
            case 4: sigo_jugando = False


if __name__ == '__main__':
    fun()
