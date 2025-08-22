# Comparación de Rendimiento entre Lenguajes Compilados e Interpretados

Este proyecto tiene como objetivo comparar el rendimiento de un lenguaje compilado (C++) y un lenguaje interpretado (Python) utilizando algoritmos iterativos y recursivos para el cálculo de la secuencia de Fibonacci. Además, se incluye un análisis de los resultados y una visualización gráfica de los tiempos de ejecución.

## Algoritmos Implementados

Se implementaron las siguientes versiones del algoritmo de Fibonacci:

*   **Iterativa:** Una implementación que calcula la secuencia de Fibonacci utilizando un bucle, lo que la hace eficiente en términos de tiempo y espacio.
*   **Recursiva:** Una implementación que calcula la secuencia de Fibonacci utilizando llamadas recursivas. Esta versión es conceptualmente más simple pero computacionalmente más costosa debido a las llamadas repetidas a la función para los mismos valores.

## Metodología

Para realizar la comparación de rendimiento, se siguió la siguiente metodología:

1.  **Implementación:** Los algoritmos iterativo y recursivo de Fibonacci se implementaron tanto en C++ como en Python.
2.  **Medición de Tiempo:** Se midió el tiempo de ejecución de cada implementación para un valor `n` fijo (en este caso, `n=40`). Se utilizó la librería `chrono` en C++ y el módulo `time` en Python para obtener mediciones precisas.
3.  **Ejecución en la Misma Arquitectura:** Todas las pruebas se realizaron en la misma máquina virtual para asegurar una comparación justa y evitar variaciones de rendimiento debido a diferencias de hardware.
4.  **Análisis de Resultados:** Los tiempos de ejecución obtenidos se recopilaron y se analizaron para identificar patrones y diferencias significativas entre los lenguajes y los tipos de algoritmos.
5.  **Visualización:** Se generó un gráfico de barras para visualizar claramente los tiempos de ejecución y facilitar la comprensión de las diferencias de rendimiento.

## Estructura del Proyecto

```
comparacion_compiladores_interpretes/
├── cpp/
│   ├── fibonacci_iterative.cpp
│   ├── fibonacci_recursive.cpp
│   ├── iterative_cpp_results.txt
│   └── recursive_cpp_results.txt
├── python/
│   ├── fibonacci_iterative.py
│   ├── fibonacci_recursive.py
│   ├── iterative_python_results.txt
│   └── recursive_python_results.txt
├── analyze_results.py
├── plot_results.py
├── performance_results.txt
├── performance_chart.png
└── README.md
```

## Resultados

Los tiempos de ejecución obtenidos para `n=40` son los siguientes:

*   **C++ Iterativo:** 3.00e-07 segundos
*   **C++ Recursivo:** 0.896143 segundos
*   **Python Iterativo:** 6.91e-06 segundos
*   **Python Recursivo:** 17.07407259941101 segundos

Estos resultados se pueden encontrar en el archivo `performance_results.txt`.

### Gráfico de Rendimiento

![Gráfico de Rendimiento](https://private-us-east-1.manuscdn.com/sessionFile/Rv20TatwadLv54Zz5c6v6i/sandbox/1hd9JWhP33SzOemZnFLr2P-images_1755821590733_na1fn_L2hvbWUvdWJ1bnR1L2NvbXBhcmFjaW9uX2NvbXBpbGFkb3Jlc19pbnRlcnByZXRlcy9wZXJmb3JtYW5jZV9jaGFydA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvUnYyMFRhdHdhZEx2NTRaejVjNnY2aS9zYW5kYm94LzFoZDlKV2hQMzNTek9lbVpuRkxyMlAtaW1hZ2VzXzE3NTU4MjE1OTA3MzNfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyTnZiWEJoY21GamFXOXVYMk52YlhCcGJHRmtiM0psYzE5cGJuUmxjbkJ5WlhSbGN5OXdaWEptYjNKdFlXNWpaVjlqYUdGeWRBLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5ODc2MTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=QoFjhEJfeQQw7EqozIzGfyfeV80qLRX4ip-rjU-Qpd1xG0wluRbt5Ha4pLvxS5SrcFrTHqHJz~Wg0G4WJNOpptSXQ6AzudnKZQuKgU~8B7sU3wnuN9UYS5KnJJr8Ip2HUd4r-POypkVeVNTkrbL2lqunZsYpwfFAXHZ-NEy78gCxLCk-IJ1IGAGsMPP-EDEeyj-bg0vzkQ-WkkydK-shCPj9XOfv26MZPgf32Fox0-adFSUFKR4F4bFexf7FFD5ySMPGRWtSFk5ECBU3fv2T0hhUlnJSqIBjY8GXmGZR4dMC6Q739QWDENQNVRKQvaDgX1WY~VhEgbcVXnXOiQEiYA__)

## Análisis de los Resultados

Como se puede observar en los resultados y el gráfico, existen diferencias significativas en el rendimiento:

1.  **C++ vs Python:** En general, C++ demuestra ser considerablemente más rápido que Python para ambas implementaciones. Esto se debe a que C++ es un lenguaje compilado que se traduce directamente a código máquina, lo que permite una ejecución más eficiente. Python, al ser interpretado, requiere un intérprete que procese el código en tiempo de ejecución, lo que introduce una sobrecarga.

2.  **Iterativo vs Recursivo:** Dentro de cada lenguaje, la implementación iterativa es drásticamente más rápida que la recursiva. Esto es especialmente evidente en el caso de la recursión de Fibonacci, que sufre de una gran cantidad de cálculos redundantes (problema de superposición de subproblemas). La implementación iterativa evita esta redundancia al almacenar los resultados intermedios.

3.  **Impacto de la Recursión en Python:** La diferencia de rendimiento entre la versión iterativa y recursiva es mucho más pronunciada en Python que en C++. Esto se debe a la sobrecarga adicional de las llamadas a funciones en Python, que es mayor que en C++.

## Conclusión

Este estudio reafirma que los lenguajes compilados como C++ ofrecen un rendimiento superior para tareas computacionalmente intensivas en comparación con los lenguajes interpretados como Python. Además, destaca la importancia de elegir el algoritmo adecuado; las soluciones iterativas suelen ser más eficientes que las recursivas para problemas como el de Fibonacci, especialmente cuando la recursión implica cálculos repetidos. Para aplicaciones donde el rendimiento es crítico, la elección de un lenguaje compilado y la optimización algorítmica son factores clave.

## Cómo Ejecutar el Proyecto

1.  **Clonar el Repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd comparacion_compiladores_interpretes
    ```

2.  **Compilar C++:**
    ```bash
    cd cpp
    g++ fibonacci_iterative.cpp -o fibonacci_iterative
    g++ fibonacci_recursive.cpp -o fibonacci_recursive
    cd ..
    ```

3.  **Ejecutar y Recopilar Datos (C++):**
    ```bash
    cd cpp
    ./fibonacci_iterative > iterative_cpp_results.txt
    ./fibonacci_recursive > recursive_cpp_results.txt
    cd ..
    ```

4.  **Ejecutar y Recopilar Datos (Python):**
    ```bash
    cd python
    python3 fibonacci_iterative.py > iterative_python_results.txt
    python3 fibonacci_recursive.py > recursive_python_results.txt
    cd ..
    ```

5.  **Analizar y Graficar Resultados:**
    ```bash
    python3 analyze_results.py
    python3 plot_results.py
    ```

Esto generará el archivo `performance_results.txt` con los tiempos y `performance_chart.png` con el gráfico.


