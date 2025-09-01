import random
import csv

# Abrir el archivo dentro del bloque with
with open("edades.csv", mode="w", newline="") as archivo:
    escritor = csv.writer(archivo)

    # Generar y escribir 100 edades aleatorias
    for i in range(100):
        num = random.randint(15, 18)
        escritor.writerow([num])
        print(num)
