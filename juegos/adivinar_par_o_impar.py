def adivinar_par_o_impar():
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
    import random
    numero = random.randint(1,100)
    adivina = input("Adivina si estoy pensando en un número par o impar: ")

    if (numero % 2 == 0 and adivina == "par") or (numero % 2 != 0 and adivina == "impar"):
        print ("ESO ES! Crack")
    else:
        print("Pusha no, era el otro")
    print(f"El número era {numero}")