#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el
#radio como parámetro y devuelva el área del círculo.
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva
#el perímetro del círculo. Solicitar el radio al usuario y llamar
#ambas funciones para mostrar los resultados.

from math import pi

#Definicion de funciones

def calcular_area_circulo(radio):                       #Defino la funcion con el parametro radio
    area = pi * (radio ** 2)                            #Calculo el area usando la formula del area de un circulo (pi * radio^2)
    return area

def calcular_perimetro_circulo(radio):                 #Defino la funcion con el parametro radio
    perimetro = 2 * pi * radio                         #Calculo el perimetro usando la formula del perimetro de un circulo (2 * pi * radio)
    return perimetro

#Programa principal

radio = float(input("Ingrese el radio del círculo: "))  #Solicito al usuario el radio
area = calcular_area_circulo(radio)                     #Llamo a la funcion para calcular el area con el radio ingresado por el usuario
perimetro = calcular_perimetro_circulo(radio)           #Llamo a la funcion para calcular el perimetro con el radio ingresado por el usuario
print(f"El área del círculo es: {area:.2f}")            #Imprimo el resultado del area con 2 decimales
print(f"El perímetro del círculo es: {perimetro:.2f}")  #Imprimo el resultado del perimetro con 2 decimales