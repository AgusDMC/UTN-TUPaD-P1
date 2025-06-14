def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario un número
limite = int(input("Ingrese un número entero positivo: "))

print("Factoriales del 1 al", limite)
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")