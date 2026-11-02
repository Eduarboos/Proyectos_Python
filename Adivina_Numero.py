import random

def adivina_el_numero(x):

    print("=========================")
    print(" ¡Bienvenido(a) al juego!")
    print("=========================")
    print(" Tu meta es adivinar el numero generado por la computadora.")

    numero_aleatiorio = random.randint(1, x) #Numero aleatorio entre 1 y x

    prediccion = 0

    while prediccion != numero_aleatiorio:
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: ")) 

        if prediccion < numero_aleatiorio:
            print("Intenta otra vez. Este numero es muy bajo")
        elif prediccion > numero_aleatiorio:
            print("Intenta otra vez. Este numero es muy alto")

    print(f"!Felicidades¡ Adivinaste el numero {numero_aleatiorio} correctamente.")  


adivina_el_numero(10) 