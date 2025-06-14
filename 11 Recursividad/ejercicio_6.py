def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Ejemplo de uso:
print(suma_digitos(1234))   # 10
print(suma_digitos(9))      # 9
print(suma_digitos(305))    # 8