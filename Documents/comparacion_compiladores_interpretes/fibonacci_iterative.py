import time

def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    n = 40 # Puedes cambiar este valor para probar diferentes entradas

    start_time = time.time()
    result = fibonacci_iterative(n)
    end_time = time.time()

    print(f"Fibonacci iterativo({n}) = {result}")
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")


