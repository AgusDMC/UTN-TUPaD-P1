#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos-
#trar el resultado usando esta función.

#Definicion de funciones

def segundos_a_horas(segundos):  #Defino la funcion con el parametro segundos
    horas = segundos / 3600      #Calculo las horas dividiendo los segundos entre 3600 (segundos en una hora)
    return horas                 #Devuelvo la cantidad de horas

#Programa principal

segundos = int(input("Ingrese la cantidad de segundos: "))  #Solicito al usuario la cantidad de segundos
horas = segundos_a_horas(segundos)  #Llamo a la funcion con los segundos ingresados por el usuario
print(f"{segundos} segundos son {horas:.2f} horas.")  #Imprimo el resultado