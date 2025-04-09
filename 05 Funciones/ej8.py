#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
#ción para mostrar el resultado con dos decimales

#Definicion de funciones

def calcular_imc(peso, altura):  #Defino la funcion con los 2 parametros
    imc = peso / (altura ** 2)   #Calculo el IMC dividiendo el peso entre la altura al cuadrado
    return imc                    #Devuelvo el IMC calculado

#Programa principal

peso = float(input("Ingrese su peso en kilogramos: "))  #Solicito al usuario el peso
altura = float(input("Ingrese su altura en metros: "))  #Solicito al usuario la altura
imc = calcular_imc(peso, altura)  #Llamo a la funcion con los datos ingresados por el usuario
print(f"Su IMC es: {imc:.2f}")  #Imprimo el resultado con 2 decimales