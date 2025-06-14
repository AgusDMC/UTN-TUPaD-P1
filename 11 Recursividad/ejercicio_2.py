def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar al usuario la cantidad de términos
pos = int(input("Ingrese la cantidad de términos de Fibonacci: "))

print("Serie de Fibonacci:")
for i in range(pos):
    print(fibonacci(i), end=" ")
print()