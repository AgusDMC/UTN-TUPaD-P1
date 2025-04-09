#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

#Definicion de funciones

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")  #Imprimo el saludo personalizado usando el nombre ingresado por el usuario


#Programa principal
nombre = input("Por favor, introduce tu nombre: ")  #Solicito al usuario que ingrese su nombre
saludar_usuario(nombre)  #Llamo a la funcion con el nombre ingresado por el usuario

