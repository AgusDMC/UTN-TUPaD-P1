# Sets con alumnos que aprobaron cada parcial
parcial1 = {"Ana", "Luis", "Marta", "Julián"}
parcial2 = {"Marta", "Luis", "Carlos", "Sofía"}

# Aprobados en ambos parciales (intersección)
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

# Aprobaron solo uno (diferencia simétrica)
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

# Aprobó al menos uno (unión)
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)
