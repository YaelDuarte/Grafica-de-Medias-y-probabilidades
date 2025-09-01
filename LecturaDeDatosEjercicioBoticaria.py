import numpy as np
import matplotlib.pyplot as plt

# Lectura de los datos desde CSV (soporta encabezados y celdas vacías)
arg1 = np.genfromtxt('./Edades2.csv', delimiter=',', dtype=np.int16, skip_header=0)   
# El skip ignora la primera fila si hay encabezado

# Eliminamos posibles NaN si había celdas vacías
arg1 = arg1[~np.isnan(arg1)]

# Ordenamos y ajustamos a 100 datos
arg2 = np.sort(np.reshape(arg1, 100))

# Cálculo del rango, como tenemos 100 elementos se hace una operacion del Valor Max - Valor Min
rango = arg2[99] - arg2[0]
print("Rango:", rango)

# Intervalos de la clase para que se muestren es decir de 15 a 19, para abarcar los datos de 18 años
b = np.arange(15, 20, 1, dtype=np.int16)
print("Intervalos:", b)

# Histograma
fig, ax = plt.subplots()
intervalos_clase = ax.hist(arg2, bins=b,
                           linewidth=0.5, edgecolor="white")

# Probabilidades


frecuencias = intervalos_clase[0]
total = np.sum(frecuencias)
probabilidades = frecuencias / total
print("Frecuencias:", frecuencias)
print("Probabilidades:", probabilidades)

# Medias

# Media aritmética → el promedio clásico: suma de todos los valores / número de datos.
media_aritmetica = np.mean(arg2)

# Media armónica → útil en casos de tasas, razones o velocidades.
# Se calcula como el inverso del promedio de los inversos de los datos.
media_armonica = np.mean(1.0 / arg2) ** (-1)

# Media geométrica → se obtiene multiplicando todos los valores y sacando la raíz n-ésima.
# En este caso puede dar 0 si algún dato en el CSV es 0 (porque anula el producto).
media_geometrica = np.prod(arg2) ** (1.0/len(arg2))

print("Media aritmética:", media_aritmetica)
print("Media armónica:", media_armonica)
print("Media geométrica:", media_geometrica)

# Configuración gráfica
plt.xticks(fontsize=8)
ax.set(xlim=(15, 19), xticks=b,
       ylim=(0, max(intervalos_clase[0])+2), 
       yticks=np.arange(0, max(intervalos_clase[0])+2, 1, dtype=np.int16))
ax.grid(True)
plt.show()

# CONCLUSION 

#El análisis de los 100 datos muestra que las edades de los espectadores del anime de la boticaria se concentran principalmente 
#en los 15 años (30%), seguidos de 17 años (28%), 16 años (24%) y en menor medida 18 años (18%). 
#El rango de 3 confirma que los valores están acotados entre 15 y 18 años, sin registros fuera de lo esperado. 
#La media aritmética (16.34) y la media armónica (16.26) reflejan que la edad promedio de los participantes se sitúa entre 16 y 17 años, 
#lo cual coincide con la distribución observada. 

#En conclusión, 
#la población analizada está compuesta mayormente por adolescentes entre 15 y 17 años, 
#con ligera predominancia en los de 15, y la edad promedio general se mantiene cercana a los 16 años.
