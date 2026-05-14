import time
import sys

"""Importando time para gravar o tempo de execução da função.

Importando sys para aumentar o limite de recursão.
"""
sys.setrecursionlimit(1001)

def find_factorial(number):
    """Função recursiva para calcular fatorial."""
    if number <= 1:
        return 1
    else:
        return number * find_factorial(number-1)

"""Cálculo da fatorial e marcação de tempo desse cálculo."""
number = int(input("Insira um número: "))

initial_time = time.perf_counter()

factorial = find_factorial(number)

time_elapsed = time.perf_counter() - initial_time

print(f"O fatorial de {number} é {factorial}.")
print(f"Tempo de execução: {time_elapsed:.10f} segundos.")

"""Tempos de execução do algoritmo:
n = 10:
    Tempo de execução: 0.0000072000 segundos.
n = 100:
    Tempo de execução: 0.0000160000 segundos.
n = 500:
    Tempo de execução: 0.0001086000 segundos.
n = 1000:
    Tempo de execução: 0.0005248000 segundos.

find_factorial(1) -> return 1 |1 chamada
find_factorial(2) -> return 2 * find_factorial(1) |
                                        |         |
                                        v         |
                                    return 1      |2 chamadas
find_factorial(3) -> return 3 * find_factorial(2)            |
                                        |                    |
                                        v                    |
                                return 2 * find_factorial(1) |
                                                    |        |
                                                    v        |
                                                return 1     |3 chamadas

eventualmente, find_factorial(n) -> n chamadas, 
portanto find_factorial tem O(n)
"""