import numpy as np
import matplotlib.pyplot as plt

# Función para calcular el ancho de banda disponible según el número de archivos transmitidos
def ancho_banda_disponible(N):
    if N <= 30:
        return 1000
    else:
        return 1000 * (1 - 0.05 * (N - 30))

# Función para determinar el número máximo de archivos antes de que el ancho de banda sea menor de 500 Mbps
def max_archivos_transmitidos():
    for N in range(31, 51):  # Verificamos desde 31 archivos en adelante
        if ancho_banda_disponible(N) < 500:
            return N - 1  # El máximo es el archivo anterior
    return 50  # Si nunca baja de 500 Mbps, el máximo es 50

# Parámetros
N_values = np.arange(1, 51)  # Valores de archivos transmitidos de 1 a 50
ancho_banda_values = [ancho_banda_disponible(N) for N in N_values]

# Determinar el número máximo de archivos que se pueden transmitir antes de bajar de 500 Mbps
max_archivos = max_archivos_transmitidos()

# Gráfico
plt.plot(N_values, ancho_banda_values, label='Ancho de banda disponible (Mbps)', color='b', marker='o')
plt.axhline(y=500, color='red', linestyle='--', label='Umbral de 500 Mbps')
plt.axvline(x=30, color='green', linestyle='--', label='Umbral de 30 archivos')
plt.axvline(x=max_archivos, color='orange', linestyle='--', label=f'Máx archivos = {max_archivos}')
plt.title('Ancho de Banda vs Número de Archivos Transmitidos')
plt.xlabel('Número de archivos transmitidos (N)')
plt.ylabel('Ancho de banda disponible (Mbps)')
plt.legend()
plt.grid(True)
plt.show()

print(f"El número máximo de archivos que se pueden transmitir antes de que el ancho de banda baje de 500 Mbps es: {max_archivos}")
