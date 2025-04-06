#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

password = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")     # Solicito la contraseña al usuario
if len(password) >= 8 and len(password) <= 14:                              # Verifico si la longitud de la contraseña está entre 8 y 14 caracteres
    print("Ha ingresado una contraseña con longitud correcta")              # Si la longitud es correcta, imprimo el mensaje correspondiente
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")   # Si la longitud no es correcta, imprimo un mensaje pidiendo una contraseña de longitud adecuada