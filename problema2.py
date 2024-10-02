import matplotlib.pyplot as plt

def calcular_maximo_peticiones(nodos=20, capacidad_total=400):
    # Capacidad máxima por nodo
    max_peticiones_por_nodo = capacidad_total / nodos
    # Total de peticiones procesadas
    total_peticiones = nodos * max_peticiones_por_nodo
    return max_peticiones_por_nodo, total_peticiones

def graficar_peticiones(nodos=20, capacidad_total=400):
    max_peticiones_por_nodo, total_peticiones = calcular_maximo_peticiones(nodos, capacidad_total)
    
    # Valores para graficar
    nodos_list = list(range(1, nodos + 1))
    peticiones_por_nodo_list = [capacidad_total / n for n in nodos_list]
    total_peticiones_list = [n * (capacidad_total / nodos) for n in nodos_list]
    
    plt.figure(figsize=(10, 6))
    plt.plot(nodos_list, total_peticiones_list, marker='o', linestyle='-', color='b', label='Total de Peticiones Procesadas')
    plt.axhline(y=capacidad_total, color='r', linestyle='--', label='Capacidad de Red (400 peticiones/s)')
    plt.title('Peticiones Procesadas en Función del Número de Nodos')
    plt.xlabel('Número de Nodos')
    plt.ylabel('Total de Peticiones Procesadas (por segundo)')
    plt.xticks(nodos_list)
    plt.grid(True)
    plt.legend()
    plt.show()

# Calcular el máximo de peticiones
max_peticiones_por_nodo, total_peticiones = calcular_maximo_peticiones()
print(f"Peticiones por nodo: {max_peticiones_por_nodo:.2f} peticiones/s")
print(f"Total de peticiones procesadas: {total_peticiones:.2f} peticiones/s")

# Graficar el resultado
graficar_peticiones()
