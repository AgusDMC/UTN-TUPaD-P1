# Solicitar la frase al usuario
frase = input("Ingresá una frase: ")

# Separar en palabras
palabras = frase.split()

# Obtener palabras únicas usando un set
palabras_unicas = set(palabras)

# Crear diccionario de recuento
recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Mostrar resultados
print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)
