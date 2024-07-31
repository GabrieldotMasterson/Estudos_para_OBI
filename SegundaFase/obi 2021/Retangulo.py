import sys

# Leitura da entrada
n_arvores = int(sys.stdin.readline().strip())
distancias = list(map(int, sys.stdin.readline().strip().split()))

# Calcular a circunferência total
circunferencia_total = sum(distancias)

# Construir prefix sums
prefix_sums = [0] * (len(distancias) + 1)
for i in range(len(distancias)):
    prefix_sums[i + 1] = prefix_sums[i] + distancias[i]

# Função para calcular a soma de um subarray circular
def soma_subarray(l, r):
    if l <= r:
        return prefix_sums[r + 1] - prefix_sums[l]
    else:
        return prefix_sums[len(distancias)] - prefix_sums[l] + prefix_sums[r + 1]

# Função principal para verificar se é possível formar o retângulo
def trabalhe():
    half_circumference = circunferencia_total // 2
    n = len(distancias)
    for i in range(n):
        for j in range(i + 1, n):
            if j - i >= 2:
                lado1 = soma_subarray(i, j - 1)
                lado2 = soma_subarray(j, (i + n//2) % n - 1)
                if lado1 == lado2 == half_circumference // 2:
                    return "S"
    return "N"

print(trabalhe())
