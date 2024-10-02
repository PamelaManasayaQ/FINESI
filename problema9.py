import numpy as np
import matplotlib.pyplot as plt


def costo_total(x):
    return 50 * x + 5 * x**2

presupuesto = 500
x_values = np.linspace(0, 10, 400)

costo_values = costo_total(x_values)

plt.figure(figsize=(8, 6))
plt.plot(x_values, costo_values, label='Costo total ($)', color='blue')
plt.axhline(y=presupuesto, color='red', linestyle='--', label=f'Presupuesto ($500)')
plt.axvline(x=6.18, color='green', linestyle='--', label=f'Máximo almacenamiento (6.18 TB)')

plt.title('Maximización de Almacenamiento sin Exceder el Presupuesto', fontsize=14)
plt.xlabel('Almacenamiento (TB)', fontsize=12)
plt.ylabel('Costo Total ($)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()