import random

def juego_del_dado():
    j1 = random.randint(1, 6)
    bot = random.randint(1, 6)
    return [j1,bot]

j1 = 0
bot = 0
while j1 < 30 and bot < 30:
    x = juego_del_dado()
    j1 += x[0]
    bot += x[1]

if j1 >= 30:
    print("¡Ganaste!")
else:
    print("¡Perdiste!")
print("Puntos jugador:", j1)
print("Puntos bot:", bot)
