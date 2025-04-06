#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in ["a","e","i","o","u"]:  # Verifico si la última letra de la frase es una vocal
                                                # La función lower() convierte la letra a minúscula para que no haya problemas con mayúsculas y minúsculas
    frase += "!"                                # Si es una vocal, le agrego un signo de exclamación al final
    print(frase)                                # Imprimo la frase con el signo de exclamación
else:
    print(frase)                                # Si no es una vocal, imprimo la frase tal cual la ingresó el usuario