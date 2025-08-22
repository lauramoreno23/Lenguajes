import time

def fibonacci_recursive(n):
    if n <= 1: return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    n = 40 # Puedes cambiar este valor para probar diferentes entradas

    start_time = time.time()
    result = fibonacci_recursive(n)
    end_time = time.time()

    print(f"Fibonacci recursivo({n}) = {result}")
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")


