#include <iostream>
#include <chrono>

long long fibonacci_recursive(int n) {
    if (n <= 1) return n;
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

int main() {
    int n = 40; // Puedes cambiar este valor para probar diferentes entradas

    auto start = std::chrono::high_resolution_clock::now();
    long long result = fibonacci_recursive(n);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> duration = end - start;

    std::cout << "Fibonacci recursivo(" << n << ") = " << result << std::endl;
    std::cout << "Tiempo de ejecución: " << duration.count() << " segundos" << std::endl;

    return 0;
}


