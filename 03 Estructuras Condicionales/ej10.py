#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

#Periodo del año
#Desde el 21 de diciembre hasta el 20 de marzo (incluidos)
#Estación en el hemisferio norte: Invierno
#Estación en el hemisferio sur: Verano

#Desde el 21 de marzo hasta el 20 de junio (incluidos)
#Estación en el hemisferio norte: Primavera
#Estación en el hemisferio sur: Otoño

#Desde el 21 de junio hasta el 20 de septiembre (incluidos)
#Estación en el hemisferio norte: Verano
#Estación en el hemisferio sur: Invierno

#Desde el 21 de septiembre hasta el 20 dediciembre (incluidos)
#Estación en el hemisferio norte: Otoño
#Estación en el hemisferio sur: Primavera
  
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper() # Solicito el hemisferio al usuario y lo convierto a mayúsculas
if hemisferio not in ["N", "S"]:
    print("Hemisferio inválido.")                                               # Verifico si el hemisferio es válido (N o S)
    exit()
mes = int(input("¿Qué mes es? (1-12): "))                                       # Solicito el mes al usuario y lo convierto a entero
if mes < 1 or mes > 12:
    print("Mes inválido.")                                                      # Verifico si el mes es válido (1-12)
    exit()
dias_de_los_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]            # Lista con la cantidad de días de cada mes
dia = int(input("¿Qué día es? (1-31): "))                                       # Solicito el día al usuario y lo convierto a entero
if dia < 1 or dia > dias_de_los_meses[mes - 1]:
    print("Día inválido.")                                                      # Verifico si el día es válido (1-31 según el mes)
    exit()
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes <= 2) or (mes == 3 and dia <= 20):     # Verifico si el mes y día corresponden a invierno
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes <= 6) or (mes == 6 and dia <= 20):    # Verifico si el mes y día corresponden a primavera
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes <= 9) or (mes == 9 and dia <= 20):    # Verifico si el mes y día corresponden a verano
        estacion = "Verano"
    else:   
        estacion = "Otoño"                                                      #Si no corresponde a ninguna estación, asigno "Otoño"
else:
    if (mes == 12 and dia >= 21) or (mes <= 2) or (mes == 3 and dia <= 20):     # Verifico si el mes y día corresponden a verano
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes <= 6) or (mes == 6 and dia <= 20):    # Verifico si el mes y día corresponden a otoño
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes <= 9) or (mes == 9 and dia <= 20):    # Verifico si el mes y día corresponden a invierno
        estacion = "Invierno"
    else:
        estacion = "Primavera"                                                  #Si no corresponde a ninguna estación, asigno "Primavera"