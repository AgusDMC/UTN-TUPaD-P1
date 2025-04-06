#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

numero = int(input("Ingrese un número entero (0 para salir): "))    # Se solicita al usuario un número entero
suma = 0                                                            # Inicializamos la suma en 0

while numero != 0:                                                  # Mientras el número no sea 0, se suma el número en la variable suma
    suma = suma + numero
    numero = int(input("Ingrese un número entero (0 para salir): "))
print("La suma total es:", suma)                                    # Se imprime la suma total acumulada