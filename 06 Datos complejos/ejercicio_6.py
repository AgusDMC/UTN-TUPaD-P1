# Crear diccionario vacío
alumnos = {}

# Cargar 3 alumnos y sus notas
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ")
    nota1 = int(input(f"Ingresá la nota 1 de {nombre}: "))
    nota2 = int(input(f"Ingresá la nota 2 de {nombre}: "))
    nota3 = int(input(f"Ingresá la nota 3 de {nombre}: "))
    alumnos[nombre] = (nota1, nota2, nota3)

# Mostrar promedio de cada alumno
print("\nPromedios:")
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {promedio:.2f}")
