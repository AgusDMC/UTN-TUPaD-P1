# Diccionario de productos y stock inicial
stock = {
    "pan": 10,
    "leche": 5,
    "huevos": 12
}

# Consultar o modificar el stock
producto = input("Ingresá el nombre del producto: ").lower()

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar? "))
    stock[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    nuevo_stock = int(input(f"{producto} no está en el stock. ¿Cuántas unidades querés agregar? "))
    stock[producto] = nuevo_stock
    print(f"{producto} agregado con {nuevo_stock} unidades.")

# Mostrar estado final del stock
print("\nStock final:")
for prod, cant in stock.items():
    print(f"{prod}: {cant}")
