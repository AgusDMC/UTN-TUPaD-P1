#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

suma = 0
limite = 100

for i in range(1, limite + 1):                                     # Se solicita al usuario ingresar 100 números enteros
    while True:
        numero = int(input(f"Ingrese el número entero {i}: "))     # Se solicita al usuario un número entero
        if numero >= 0:                                            # Si el número es mayor o igual a 0, se acepta
            break
        else:                                                      # Si el número es negativo, se solicita otro número
            print("El número debe ser entero positivo. Intente nuevamente.")
    suma = suma + numero                                           # Se suma cada número ingresado a la variable suma

media = suma / limite                                              # Se calcula la media dividiendo la suma entre el límite (100) 
print(f"La media de los números ingresados es: {media:.2f}")       # Se imprime la media con 2 decimales

