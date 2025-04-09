#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

#Definicion de funciones

def tabla_multiplicar(numero):  #Defino la funcion con el parametro numero
    for i in range(1, 11):  #Itero desde 1 hasta 10 (inclusive)
        print(f"{numero} x {i} = {numero * i}")  #Imprimo la tabla de multiplicar del numero ingresado por el usuario

#Programa principal

numero = int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))  #Solicito al usuario el numero
tabla_multiplicar(numero)  #Llamo a la funcion con el numero ingresado por el usuario