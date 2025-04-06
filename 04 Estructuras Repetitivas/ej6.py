#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):    # El rango va de 100 a 0, con un paso de -2 para obtener solo los números pares
    if i % 2 == 0:              # Verificamos si el número es par
        print(i)                # Se imprime el número actual de la iteración
    print(i, end="\n")
