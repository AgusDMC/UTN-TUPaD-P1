#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
#diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")           # Agrego "jugo" a la lista del tercer cliente
compras[1][1] = "tallarines"        # Reemplazo "fideos" por "tallarines" en la lista del segundo cliente
compras[0].remove("pan")            # Elimino "pan" de la lista del primer cliente
print(compras)                      # Imprimo la lista resultante por pantalla