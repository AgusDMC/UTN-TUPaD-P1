#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

numero = random.randint(0, 9)                                                      # Genera un número aleatorio entre 0 y 9  
intentos = 0                                                                       # Inicializa el contador de intentos en 0

print("Adivina el número entre 0 y 9")
while True:
    while True:                                                                    # Bucle para asegurar que el número ingresado esté entre 0 y 9
        intento = int(input("Introduce un número: "))
        if 0 <= intento <= 9:
            break
        else:
            print("El número debe estar entre 0 y 9")
    intentos = intentos + 1                                                        # Incrementa el contador de intentos
    if intento < numero:    
        print("El número es mayor")
    elif intento > numero:
        print("El número es menor")
    else:
        print(f"¡Correcto! El número era {numero}. Te tomó {intentos} intentos.")  # Muestra el número correcto y la cantidad de intentos 
        break