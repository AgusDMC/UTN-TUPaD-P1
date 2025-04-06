#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Introduce el primer número: "))                        # Se solicita al usuario el primer número 
numero2 = int(input("Introduce el segundo número: "))                       # Se solicita al usuario el segundo número
suma = 0                                                                    # Inicializamos la suma en 0

for i in range(numero1 + 1, numero2):
    suma = i + suma                                                         # Se suma cada número entre los dos valores ingresados

print("La suma de los números entre", numero1, "y", numero2, "es:", suma)   # Se imprime la suma total acumulada