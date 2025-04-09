#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
#Pedir los datos al usuario y llamar a esta función con los valores
#ingresados.

#Definicion de funciones

def informacion_personal(nombre, apellido, edad, residencia):                       #Defino la funcion con los 4 parametros
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")    #Imprimo el mensaje con los datos ingresados por el usuario

#Programa principal

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)                            #Llamo a la funcion con los datos ingresados por el usuario