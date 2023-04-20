import random

# Función para generar el patrón de colores
def generar_patron():
    colores = ['rojo', 'azul', 'verde', 'amarillo', 'naranja', 'morado']
    return random.sample(colores, 4)

# Función para validar la jugada del jugador
def validar_jugada(jugada, patron):
    if jugada == patron:
        return True
    else:
        # Comprobar los colores que están en el patrón pero en la posición equivocada
        colores_en_posicion_equivocada = 0
        for i in range(len(jugada)):
            if jugada[i] in patron and jugada[i] != patron[i]:
                colores_en_posicion_equivocada += 1
        # Comprobar los colores que están en el patrón y en la posición correcta
        colores_en_posicion_correcta = sum(1 for i in range(len(jugada)) if jugada[i] == patron[i])
        print('Intento {0}: {1} colores en posición correcta, {2} colores en posición equivocada'.format(intentos, colores_en_posicion_correcta, colores_en_posicion_equivocada))
        return False

# Generar el patrón de colores
patron = generar_patron()

# Imprimir las instrucciones del juego
print('Bienvenido a Mastermind!\nIntroduce 4 colores de la siguiente lista: rojo, azul, verde, amarillo, naranja, morado')
print('Tienes 10 intentos para adivinar el patrón de colores.\n')

# Inicializar el número de intentos
intentos = 0

# Comenzar el juego
while intentos < 10:
    # Pedir la jugada del jugador
    jugada = input('Jugada #{0}: '.format(intentos + 1)).split()
    # Validar la jugada del jugador
    if validar_jugada(jugada, patron):
        print('¡Felicidades! ¡Has adivinado el patrón de colores en {0} intentos!'.format(intentos + 1))
        break
    # Incrementar el número de intentos
    intentos += 1
else:
    print('Lo siento, has agotado los 10 intentos. El patrón de colores era {0}.'.format(patron))
