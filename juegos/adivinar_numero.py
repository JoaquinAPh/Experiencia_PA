def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    import random
    numero = random.randint(1,10)
    adivinado = input("Adivina en qué número estoy pensando entre 1 y 10: ")
    if numero == adivinado:
        print("FELICITACIONES, ADIVINASTE!")
    else:
        print(f"NOOO ESE NO ES! Era {numero} jiji")

