#6) escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]    # Genero una lista de 50 números aleatorios entre 1 y 100
print(numeros_aleatorios)
media = mean(numeros_aleatorios)                                    # Calculo la media de la lista
moda = mode(numeros_aleatorios)                                     # Calculo la moda de la lista
mediana = median(numeros_aleatorios)                                # Calculo la mediana de la lista
print(f'Media: {media}')
print(f'Moda: {moda}')
print(f'Mediana: {mediana}')
if media > mediana and mediana > moda:                              # Comparo la media, mediana y moda para determinar el sesgo
    print('Sesgo positivo')                                         # Si la media es mayor que la mediana y la mediana es mayor que la moda, hay sesgo positivo
elif media < mediana and mediana < moda:
    print('Sesgo negativo')                                         # Si la media es menor que la mediana y la mediana es menor que la moda, hay sesgo negativo
elif media == mediana and mediana == moda:
    print('No hay sesgo')                                           # Si la media, mediana y moda son iguales, no hay sesgo
else:
    print('Distribución irregular o caso no contemplado')           # Si no se cumple ninguna de las condiciones anteriores, imprimo que hay una distribución irregular o un caso no contemplado