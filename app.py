import random

# Función para determinar el resultado de una ronda
def determinar_ganador(opcion_jugador, opcion_computadora):
    if opcion_jugador == opcion_computadora:
        return "Empate"
    elif (opcion_jugador == "rock" and opcion_computadora == "scissors") or \
         (opcion_jugador == "scissors" and opcion_computadora == "paper") or \
         (opcion_jugador == "paper" and opcion_computadora == "rock"):
        return "Ganaste"
    else:
        return "Perdiste"

# Opciones del juego
opciones = ["rock", "paper", "scissors"]


# Función principal del juego
def jugar_piedra_papel_tijeras():
    puntos_jugador = 0

    while True:
        print("Elige una opción: rock, paper, scissors")
        eleccion_jugador = input().lower()

        if eleccion_jugador in opciones:
            eleccion_computadora = random.choice(opciones)
            resultado = determinar_ganador(eleccion_jugador, eleccion_computadora)

            print(f"El oponente eligió: {eleccion_computadora}")
            print(f"Tú elegiste: {eleccion_jugador}")
            print(f"Resultado: {resultado}")

            if resultado == "Ganaste":
                puntos_jugador += 1
            elif resultado == "Perdiste":
                puntos_jugador -= 1

            print(f"Puntos: {puntos_jugador}")

            print("¿Quieres jugar de nuevo? (sí/no)")
            jugar_nuevo = input().lower()
            if jugar_nuevo != "si":
                break
        else:
            print("Opción no válida. Por favor, elige rock, paper o scissors.")
    
    print("¡Gracias por jugar!")

# Iniciar el juego
jugar_piedra_papel_tijeras()