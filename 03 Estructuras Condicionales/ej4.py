#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))  # Solicito la edad al usuario y la convierto a entero
if edad < 12:                           # Verifico si la edad es menor de 12 años
    print("Niño/a")                     # Si es así, imprimo "Niño/a"
elif edad < 18:                         # Verifico si la edad es mayor o igual a 12 y menor de 18
    print("Adolescente")                # Si es así, imprimo "Adolescente"
elif edad < 30:                         # Verifico si la edad es mayor o igual a 18 y menor de 30
    print("Adulto/a joven")             # Si es así, imprimo "Adulto/a joven"
else:                                   
    print("Adulto/a")                   # Si no, imprimo "Adulto/a"