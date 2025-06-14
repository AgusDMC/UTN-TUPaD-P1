# Crear diccionario vacío
contactos = {}

# Cargar 5 contactos desde el usuario
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i + 1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero

# Consultar un contacto
consulta = input("\nIngresá el nombre del contacto que querés consultar: ")

if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print(f"No se encontró ningún contacto llamado {consulta}.")
