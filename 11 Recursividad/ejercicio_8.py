def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

# Ejemplo de uso:
print(contar_digito(12233421, 2))  # 3
print(contar_digito(5555, 5))      # 4
print(contar_digito(123456, 7))    # 0