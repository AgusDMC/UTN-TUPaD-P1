#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

par = 0
impar = 0
neg = 0
pos = 0

for i in range(100):
    numero = int(input("Ingrese un número entero: "))  # Se solicita al usuario un número entero
    if numero % 2 == 0:                                # Si el modulo de num entre 2 es 0, el número es par
        par += 1    
    else:
        impar += 1                                  # Si no, el número es impar
    if numero < 0:                                     # Si el número es menor que 0, es negativo
        neg += 1
    elif numero > 0:
        pos += 1                                    # Si el número es mayor que 0, es positivo                  

                                                    # Se imprime la cantidad de números pares, impares, negativos y positivos
print("Cantidad de números pares:", par)
print("Cantidad de números impares:", impar)
print("Cantidad de números negativos:", neg)
print("Cantidad de números positivos:", pos)