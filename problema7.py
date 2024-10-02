import numpy as np
import matplotlib.pyplot as plt

# Función del tiempo de respuesta T(x)
def tiempo_respuesta(x):
    return (100 / x) + 2 * x

# Derivada de T(x) para encontrar el mínimo
def derivada_tiempo_respuesta(x):
    return -100 / (x**2) + 2

# Valores de x para graficar, con la restricción de que x >= 5
x_values = np.linspace(5, 20, 500)
T_values = tiempo_respuesta(x_values)

# Cálculo del mínimo teórico de la derivada
x_min = np.sqrt(50)
T_min = tiempo_respuesta(x_min)

# Gráfico
plt.plot(x_values, T_values, label='T(x) = 100/x + 2x', color='b')
plt.axvline(x=x_min, color='orange', linestyle='--', label=f'Mínimo en x ≈ {x_min:.2f}')
plt.scatter(x_min, T_min, color='red', zorder=5, label=f'Tiempo mínimo ≈ {T_min:.2f} s')

# Límites de la gráfica
plt.xlim(5, 20)
plt.ylim(0, max(T_values) + 10)

# Etiquetas y título
plt.title('Minimización del Tiempo de Respuesta del Sistema')
plt.xlabel('Número de trabajos por segundo (x)')
plt.ylabel('Tiempo de respuesta (T(x))')
plt.legend()
plt.grid(True)

# Mostrar gráfico
plt.show()

print(f"El número óptimo de trabajos por segundo es: {x_min:.2f}")
print(f"El tiempo de respuesta mínimo es: {T_min:.2f} segundos")
