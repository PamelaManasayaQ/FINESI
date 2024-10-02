import matplotlib.pyplot as plt
import numpy as np

# Definir la función de tiempo de ejecución
def tiempo_ejecucion(x):
    return 5 * x + 2

# Límite de tiempo
limite_tiempo = 50

# Crear un rango de valores de x (número de datos)
x_values = np.arange(0, 20, 1)  # Probar valores de 0 a 19
y_values = tiempo_ejecucion(x_values)

# Encontrar el número máximo de datos
max_datos = 0
for x in x_values:
    if tiempo_ejecucion(x) <= limite_tiempo:
        max_datos = x
    else:
        break

# Imprimir el resultado
print("El número máximo de datos que puede procesar el script es:", max_datos)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Tiempo de Ejecución (5x + 2)', color='blue')
plt.axhline(y=limite_tiempo, color='red', linestyle='--', label='Límite de Tiempo (50s)')
plt.scatter(max_datos, tiempo_ejecucion(max_datos), color='green', label='Máximo de Datos', zorder=5)
plt.title('Tiempo de Ejecución en Función de los Datos Procesados')
plt.xlabel('Número de Datos')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.xlim(0, 20)
plt.ylim(0, 60)
plt.legend()
plt.grid()
plt.show()
