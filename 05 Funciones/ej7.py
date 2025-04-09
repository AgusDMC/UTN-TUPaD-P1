#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resulta-
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
#sultados de forma clara.

#Definicion de funciones

def operaciones_basicas(a, b):  #Defino la funcion con los parametros a y b
    suma = a + b  #Realizo la suma
    resta = a - b  #Realizo la resta
    multiplicacion = a * b  #Realizo la multiplicacion
    if b != 0:  #Verifico que b no sea cero para evitar division por cero
        division = a / b  #Realizo la division
    else:
        division = "Error: Division por cero"  #Mensaje de error si b es cero
    return (suma, resta, multiplicacion, division)  #Devuelvo una tupla con los resultados

#Programa principal

num1 = float(input("Ingrese el primer numero: "))  #Solicito al usuario el primer numero
num2 = float(input("Ingrese el segundo numero: "))  #Solicito al usuario el segundo numero
resultados = operaciones_basicas(num1, num2)  #Llamo a la funcion con los numeros ingresados por el usuario

print("Resultados:")
print(f"Suma: {num1} + {num2} = {resultados[0]}")  #Imprimo el resultado de la suma
print(f"Resta: {num1} - {num2} = {resultados[1]}")  #Imprimo el resultado de la resta
print(f"Multiplicacion: {num1} * {num2} = {resultados[2]}")  #Imprimo el resultado de la multiplicacion
print(f"Division: {num1} / {num2} = {resultados[3]:.2f}")  #Imprimo el resultado de la division con dos decimales