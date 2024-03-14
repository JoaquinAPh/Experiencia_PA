import random

def cachipun():
    seleccion = input("¿Piedra, Papel o Tijera? ")
    bot = random.randint(1, 3)
    j1 = 0

    if seleccion == "Piedra":
        j1 = 1
    elif seleccion == "Papel":
        j1 = 2
    elif seleccion == "Tijera":
        j1 = 3 
    else:
        return print("Escriba el su seleción en el siguente formato: Piedra, Papel o Tijera")

    if bot == j1:
        print("Empate")
        
    elif  (bot == 1 and j1 == 2) or (bot == 2 and j1 == 3) or (bot == 3 and j1 == 1):
        print("¡Ganaste!")
        
    else:
        print("¡Perdiste!")
    
    if bot == 1:
        print("Bot eligio Piedra")
    elif bot == 2:
        print("Bot eligio Papel")
    else:
        print("Bot eligio Tijera")



    

