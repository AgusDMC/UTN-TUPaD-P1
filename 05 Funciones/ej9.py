#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

#Definicion de funciones

def celsius_a_fahrenheit(celsius):  #Defino la funcion con el parametro celsius
    fahrenheit = (celsius * 9/5) + 32  #Calculo la temperatura en Fahrenheit usando la formula
    return fahrenheit                   #Devuelvo la temperatura en Fahrenheit

#Programa principal

temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))  #Solicito al usuario la temperatura en Celsius
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)  #Llamo a la funcion con la temperatura ingresada por el usuario
print(f"{temperatura_celsius} grados Celsius son {temperatura_fahrenheit:.2f} grados Fahrenheit.")  #Imprimo el resultado con 2 decimales