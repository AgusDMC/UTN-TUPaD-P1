#EJERCICIO 1: Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))  # Solicito la edad al usuario y la convierto a entero
if edad >= 18:                          # Verifico si la edad es mayor o igual a 18
    print("Es mayor de edad")           # Muestro un mensaje si es mayor de edad