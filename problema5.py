import numpy as np
import matplotlib.pyplot as plt

# Función de tiempo de entrenamiento en función del tamaño del lote
def tiempo_entrenamiento(x):
    return (1000 / x) + 0.1 * x

# Entrada interactiva del tamaño del lote
batch_size = int(input("Ingresa el tamaño del lote (batch size) entre 16 y 128: "))

# Valores de tamaño del lote (batch size) desde 16 hasta 128
x_val = np.arange(16, 129, 1)
tiempos = tiempo_entrenamiento(x_val)

# Encontrar el índice del valor mínimo de tiempo de entrenamiento
min_index = np.argmin(tiempos)
batch_size_min = x_val[min_index]
tiempo_min = tiempos[min_index]
tiempo_actual = tiempo_entrenamiento(batch_size)

# Crear el gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_val, tiempos, label='Tiempo de entrenamiento', color='b')
ax.axvline(x=batch_size_min, color='r', linestyle='--', label=f'Mínimo global en x={batch_size_min} (Tiempo: {tiempo_min:.2f})')
ax.axvline(x=batch_size, color='g', linestyle='--', label=f'Tamaño de lote seleccionado: {batch_size} (Tiempo: {tiempo_actual:.2f})')

# Títulos y etiquetas
ax.set_title('Tiempo de entrenamiento vs Tamaño del lote (Batch size)')
ax.set_xlabel('Tamaño del lote (Batch size)')
ax.set_ylabel('Tiempo de entrenamiento')
ax.grid(True)
ax.legend()

# Mostrar el gráfico
plt.show()

# Resultados
print(f'El tamaño de lote que minimiza el tiempo de entrenamiento es: {batch_size_min} con un tiempo de {tiempo_min:.2f} segundos.')
print(f'El tiempo de entrenamiento para el tamaño de lote seleccionado ({batch_size}) es: {tiempo_actual:.2f} segundos.')
