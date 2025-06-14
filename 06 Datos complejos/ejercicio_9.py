# Agenda con eventos definidos
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "18:00"): "Gimnasio"
}

# Consultar actividad
dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato hh:mm): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay actividad programada en ese horario.")
