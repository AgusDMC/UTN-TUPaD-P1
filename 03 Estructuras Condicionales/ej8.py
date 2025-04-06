#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")                                       # Solicito el nombre al usuario
print("Seleccione una opción:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra mayúscula")
opcion = int(input("Ingrese el número de la opción deseada (1, 2 o 3): "))  # Solicito la opción deseada al usuario y la convierto a entero
if opcion == 1:
    nombre_transformado = nombre.upper()                                    # Si la opción es 1, convierto el nombre a mayúsculas
elif opcion == 2:
    nombre_transformado = nombre.lower()                                    # Si la opción es 2, convierto el nombre a minúsculas
elif opcion == 3:
    nombre_transformado = nombre.title()                                    # Si la opción es 3, convierto el nombre a minúsculas con la primera letra mayúscula
else:
    nombre_transformado = "Opción no válida"                                # Si la opción no es válida, asigno un mensaje de error a la variable nombre_transformado
print(nombre_transformado)                                                  # Imprimo el nombre transformado según la opción seleccionada por el usuario