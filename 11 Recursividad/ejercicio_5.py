def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

# Ejemplo de uso:
print(es_palindromo("reconocer"))  # True
print(es_palindromo("python"))     # False