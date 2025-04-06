#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero = int(input("Introduce un número entero: "))     # Se solicita al usuario un número entero
cantidad_digitos = 0 
                                   # Inicializamos la cantidad de dígitos en 0
while numero > 0:                                       
    numero = numero // 10                               # Se divide el número entre 10 para eliminar un dígito
    cantidad_digitos += 1                               # Se incrementa la cantidad de dígitos
print("La cantidad de dígitos es:", cantidad_digitos)