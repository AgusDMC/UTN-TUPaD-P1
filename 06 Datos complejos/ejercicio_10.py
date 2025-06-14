# Diccionario original
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

# Invertir el diccionario (capitales como claves)
invertido = {capital: pais for pais, capital in original.items()}

# Mostrar resultados
print("Original:", original)
print("Invertido:", invertido)
