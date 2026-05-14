import math

def F(n):
    if n == 1:
        return 2
    return 2 * F(n - 1) + n**2

def F_fechada(n):
    soma = 0
    for k in range(2, n + 1):
        soma += (k**2) / (2**k)
    return (2**n) * (2 + soma)

n = int(input("Digite um valor para n: "))

if n < 1:
    print("Por favor, digite um inteiro positivo.")
else:
    resultado = F(n)
    
print(f"F({n}) (fechada) = {F_fechada(n)}")
print(f"F({n}) = {resultado}")