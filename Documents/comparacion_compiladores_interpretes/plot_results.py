import matplotlib.pyplot as plt
import numpy as np

# Datos de rendimiento (obtenidos de performance_results.txt)
results = {
    'C++ Iterativo': 3e-07,
    'C++ Recursivo': 0.896143,
    'Python Iterativo': 6.9141387939453125e-06,
    'Python Recursivo': 17.07407259941101
}

labels = list(results.keys())
times = list(results.values())

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects = ax.bar(x, times, width)

ax.set_ylabel('Tiempo de Ejecución (segundos)')
ax.set_title('Comparación de Rendimiento: C++ vs Python (Fibonacci)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_yscale('log') # Usar escala logarítmica para mejor visualización de diferencias grandes

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2e}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects)

fig.tight_layout()
plt.savefig('/home/ubuntu/comparacion_compiladores_interpretes/performance_chart.png')
print('Gráfico de rendimiento guardado en performance_chart.png')


