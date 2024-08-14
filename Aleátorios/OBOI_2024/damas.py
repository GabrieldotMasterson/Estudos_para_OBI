import sys

damas = sys.stdin.read().splitlines() 
damas.pop(0)
print(damas)

"""
criar matriz 8 8
colocar damas la
pra cada dama na matriz verificar se tem outra dama na sua linha, coluna ou diagonaç
"""

matriz = [[0 for _ in range(8)] for _ in range(8)]
for i in damas:
    i = i.split(" ")
    print(i)
    l = int(i[0])
    c = int(i[1])
    matriz[l][c] = 1

for i in damas:
    i = i.split(" ")
    l = int(i[0])
    c = int(i[1])

    for j in range(8):
        for i in range(8):
            if c != i:
                if damas[j][i] == 1:
                    
