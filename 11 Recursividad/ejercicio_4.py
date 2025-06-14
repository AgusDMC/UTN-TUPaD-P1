def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Solicitar al usuario un número
numero = int(input("Ingrese un número decimal positivo: "))
print(f"El número {numero} en binario es: {decimal_a_binario(numero)}")