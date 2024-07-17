def encontre(N, matriz):
    pos_x, pos_y = -1, -1
    for i in range(N):
        for j in range(N):
            if matriz[i][j] == 0:
                pos_x, pos_y = i, j
                break

    # Determinar a soma mágica usando uma linha ou coluna que não contenha o número ilegível
    for i in range(N):
        if i != pos_x:
            soma_magica = sum(matriz[i])
            break
    
    # Calcular a soma da linha e coluna que contêm o número ilegível
    soma_linha = sum(matriz[pos_x])

    # Calcular o valor do número ilegível
    valor_ilegivel = soma_magica - soma_linha

    # Imprimir os resultados
    print(valor_ilegivel)
    print(pos_x + 1)
    print(pos_y + 1)

# Exemplo de uso:
N = int(input())
matriz = [list(map(int, input().split())) for _ in range(N)]
encontre(N, matriz)
