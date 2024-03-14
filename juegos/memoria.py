def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    import random
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    num3 = random.randint(0,9)
    print(f"{num1} {num2} {num3}")
    input("Si te los aprendiste, apreta enter")
    res1 = int(input("Número 1: "))
    res2 = int(input("Número 2: "))
    res3 = int(input("Número 3: "))
    if res1 == num1 and res2 == num2 and res3 == num3:
        print("GUAU! Que buena memoria!")
    else:
        print("CUEK, falta chocolate para la memoria")
