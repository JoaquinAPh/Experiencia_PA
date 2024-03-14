import random

def juego_del_dado():
    j1 = 0
    bot = 0
    while j1 < 30 and bot < 30:
        a = input("Presione enter para tirar el dado.")
        x = random.randint(1, 6)
        xx = random.randint(1, 6)
        j1 += x
        bot += xx
    if j1 >= 30:
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
        print("Puntos jugador:", j1)
        print("Puntos bot:", bot)





