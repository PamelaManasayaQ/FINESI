# Importamos las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt

# Definimos la función de latencia
def latencia(x):
    return 100 - 2 * x

# Restricción de la latencia mínima
latencia_minima = 20

# Generamos los valores de x (mensajes por segundo)
x_values = np.linspace(0, 50, 400)

# Calculamos los valores de latencia para esos valores de x
latencia_values = latencia(x_values)

# Graficamos la función latencia
plt.figure(figsize=(8, 6))
plt.plot(x_values, latencia_values, label='Latencia (ms)', color='blue')
plt.axhline(y=latencia_minima, color='red', linestyle='--', label=f'Latencia mínima (20 ms)')
plt.axvline(x=40, color='green', linestyle='--', label=f'Máximo mensajes (40 mensajes/segundo)')

# Etiquetas y título
plt.title('Maximización de Mensajes sin Exceder la Latencia Mínima', fontsize=14)
plt.xlabel('Mensajes por segundo', fontsize=12)
plt.ylabel('Latencia (ms)', fontsize=12)
plt.legend()
plt.grid(True)

# Mostramos el gráfico
plt.show()
