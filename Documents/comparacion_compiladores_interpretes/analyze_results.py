import re

def extract_time(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    match = re.search(r'Tiempo de ejecución: (\d+\.?\d*(?:e[+-]?\d+)?) segundos', content)
    if match:
        return float(match.group(1))
    return None

cpp_iterative_time = extract_time('/home/ubuntu/comparacion_compiladores_interpretes/cpp/iterative_cpp_results.txt')
cpp_recursive_time = extract_time('/home/ubuntu/comparacion_compiladores_interpretes/cpp/recursive_cpp_results.txt')
python_iterative_time = extract_time('/home/ubuntu/comparacion_compiladores_interpretes/python/iterative_python_results.txt')
python_recursive_time = extract_time('/home/ubuntu/comparacion_compiladores_interpretes/python/recursive_python_results.txt')

results = {
    'C++ Iterativo': cpp_iterative_time,
    'C++ Recursivo': cpp_recursive_time,
    'Python Iterativo': python_iterative_time,
    'Python Recursivo': python_recursive_time
}

with open('/home/ubuntu/comparacion_compiladores_interpretes/performance_results.txt', 'w') as f:
    for key, value in results.items():
        f.write(f'{key}: {value}\n')

print('Resultados de rendimiento guardados en performance_results.txt')


