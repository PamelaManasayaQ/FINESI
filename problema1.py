import matplotlib.pyplot as plt
def calcular_datos_procesados(lotes, memoria_total=1024):
    if lotes <= 0 or lotes > 8:
        return "El número de lotes debe estar entre 1 y 8."
    if lotes <= 5:
        x = memoria_total / lotes
        datos_procesados = lotes * x
        return x, datos_procesados, lotes
    else:
        x = memoria_total / lotes
        datos_procesados = 5 * x
        for i in range(6, lotes + 1):
            eficiencia = 1 - (i - 5) * 0.2
            datos_procesados += eficiencia * x       
        return x, datos_procesados, lotes
    
def graficar_datos(lotes_max=8, memoria_total=1024):
    lotes = list(range(1, lotes_max + 1))
    datos_procesados_list = []
    for n in lotes:
        _, datos_procesados, _ = calcular_datos_procesados(n, memoria_total)
        datos_procesados_list.append(datos_procesados)

    plt.figure(figsize=(10, 6))
    plt.plot(lotes, datos_procesados_list, marker='o', linestyle='-', color='b')
    plt.title('Datos Procesados en función del Número de Lotes')
    plt.xlabel('Número de Lotes')
    plt.ylabel('Total de Datos Procesados (MB)')
    plt.xticks(lotes)
    plt.grid(True)
    plt.axhline(y=memoria_total, color='r', linestyle='--', label='Memoria Total (1024 MB)')
    plt.legend()
    plt.show()
lotes = int(input("Ingrese el número de lotes a procesar (máximo 8): "))
resultado = calcular_datos_procesados(lotes)
print(f"Memoria por lote: {resultado[0]:.2f} MB")
print(f"Total de datos procesados: {resultado[1]:.2f} MB")
graficar_datos()
