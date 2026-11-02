import random

def adivina_el_numero_computadora(x):
    print("=========================")
    print(" ¡Bienvenido(a) al juego!")
    print("=========================")
    print(f"Selecciona un numero entre 1 y {x} para que la computadora intente adivinar")


    limite_inferior = 1
    limite_superior = x

    respuesta = ""

    while respuesta != "c":
        #Generar una prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior #tambien podria ser el limite superior.


        #obetener respuesta del usuario
        respuesta = input(f"MI prediccion es{prediccion}. Si es mu alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C)").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"!Sii¡ la computadora advino tu numero correctamente: {prediccion}")

adivina_el_numero_computadora(10)
