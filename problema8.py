import numpy as np
import matplotlib.pyplot as plt

# Título del programa
print('Consumo Total de Energía vs Tamaño de Lote')
print('')

# Solicitar al usuario el tamaño del lote
tamaño_lote = int(input('Selecciona el tamaño del lote (x) (entre 1 y 20): '))

# Definición de la función de energía consumida
def energia_consumida(x):
    if x <= 10:
        return x
    else:
        return x * (1 + 0.1 * (x - 10))

# Definición de la función de consumo total
def consumo_total(x):
    return x * energia_consumida(x)

# Generar los valores de x y calcular el consumo
x_values = np.linspace(1, 20, 100)
consumo = np.array([consumo_total(x) for x in x_values])
x_max = np.max(x_values[consumo <= 200])

# Crear la gráfica
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_values, consumo, label='Consumo total de energía', color='b')
ax.axhline(y=200, color='r', linestyle='--', label='Restricción de 200 unidades de energía')
ax.axvline(x=x_max, color='g', linestyle='--', label=f'Máximo en x={x_max:.2f}')
ax.plot(x_max, consumo_total(x_max), 'go')
ax.axvline(x=tamaño_lote, color='purple', linestyle='--', label=f'Tamaño de lote seleccionado: {tamaño_lote}')
ax.plot(tamaño_lote, consumo_total(tamaño_lote), 'mo') 
ax.set_title('Consumo total de energía vs Tamaño de lote')
ax.set_xlabel('Tamaño de lote (x)')
ax.set_ylabel('Consumo total de energía (unidades)')
ax.grid(True)
ax.legend()

# Mostrar la gráfica
plt.show()

# Mostrar los resultados en consola
print(f"El tamaño de lote máximo que satisface la restricción de 200 unidades de energía es aproximadamente: {x_max:.2f}.")
print(f"Consumo total de energía para el tamaño de lote seleccionado ({tamaño_lote}): {consumo_total(tamaño_lote):.2f} unidades.")
