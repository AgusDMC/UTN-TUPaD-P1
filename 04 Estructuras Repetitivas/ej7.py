#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

numero = int(input("Introduce un número entero positivo: "))        # Se solicita al usuario un número entero positivo
suma = 0                                                            # Inicializamos la suma en 0

while numero < 0:                                                   # Mientras el número sea negativo, se solicita otro número
    print("El número debe ser positivo.")
    numero = int(input("Introduce un número entero positivo: "))

for i in range(1, numero + 1): 
    suma = suma + i                                                 # Se suma cada número desde 1 hasta el número ingresado

print("La suma de los números entre 0 y", numero, "es:", suma)      # Se imprime la suma total acumulada