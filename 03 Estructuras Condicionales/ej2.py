#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota = float(input("Ingrese su nota: "))    # Solicito la nota al usuario
if nota >= 6:                               # Verifico si la nota es mayor o igual a 6
    print("Aprobado")                       # Si es así, imprimo "Aprobado"
else:                      
    print("Desaprobado")                    # Si no, imprimo "Desaprobado"