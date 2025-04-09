#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

#Definicion de funciones

def calcular_promedio(a, b, c):  #Defino la funcion con los 3 parametros
    promedio = (a + b + c) / 3  #Calculo el promedio sumando los 3 numeros y dividiendo por 3
    return promedio               #Devuelvo el promedio calculado

#Programa principal

a = float(input("Ingrese el primer número: "))  #Solicito al usuario el primer numero
b = float(input("Ingrese el segundo número: "))  #Solicito al usuario el segundo numero
c = float(input("Ingrese el tercer número: "))  #Solicito al usuario el tercer numero

promedio = calcular_promedio(a, b, c)  #Llamo a la funcion con los numeros ingresados por el usuario
print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")  #Imprimo el resultado con 2 decimales