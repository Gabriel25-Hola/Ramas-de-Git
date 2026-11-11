import random


puntaje = 0
oportunidades = 3
numero = random.randint(1,10)

while True:
    guess = int(input("Cual crees que es el numero entre 1 y 10 (Tienes 3 oportunidades)"))

    if guess == numero:
        print("Has adivinado el numero")
        puntaje += 1
    elif guess > numero:
        print("El numero que debes adivinar es menor")
        oportunidades -= 1
    elif guess < numero:
        print("El numero que debes adivinar es mayor")
        oportunidades -= 1
    else:
        print("No lo adivinaste, ten mas suerte la proxima")
        print("El numero era:", numero)

        pregunta = input("Quieres dejar de jugar:")
        if pregunta == "si":
            print("Gracias por jugar, tu puntaje es:", puntaje, "puntos")
            break