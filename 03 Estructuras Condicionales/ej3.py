#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un número: "))      # Solicito un número al usuario y lo convierto a entero
if numero % 2 == 0:                             # Verifico si el número es par usando el operador módulo (%)
                                                # El operador % devuelve el resto de la división entre dos números. Si el resto es 0, el número es par.
    print("Ha ingresado un número par")         # Si el número es par, imprimo el mensaje correspondiente
else:
    print("Por favor, ingrese un número par")   # Si el número no es par, imprimo un mensaje pidiendo un número par