#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Introduce un número entero: "))
numero_invertido = 0  

for i in range(len(numero)-1, -1, -1):                  # Recorremos el número de atrás hacia adelante 
    digito = numero[i]                                  # Obtenemos el dígito actual
    numero_invertido = numero_invertido * 10 + digito   # Multiplicamos el número invertido por 10 y sumamos el dígito actual

print("El número invertido es:", numero_invertido)      # Imprimimos el número invertido

