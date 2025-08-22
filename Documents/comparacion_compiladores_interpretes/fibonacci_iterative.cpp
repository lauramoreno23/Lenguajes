#include <iostream>
#include <chrono>

long long fibonacci_iterative(int n) {
    if (n <= 1) return n;
    long long a = 0, b = 1, c;
    for (int i = 2; i <= n; ++i) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int main() {
    int n = 40; // Puedes cambiar este valor para probar diferentes entradas

    auto start = std::chrono::high_resolution_clock::now();
    long long result = fibonacci_iterative(n);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> duration = end - start;

    std::cout << "Fibonacci iterativo(" << n << ") = " << result << std::endl;
    std::cout << "Tiempo de ejecución: " << duration.count() << " segundos" << std::endl;

    return 0;
}


