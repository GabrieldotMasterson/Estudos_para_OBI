import sys

# Leitura da entrada
lin, col = map(int, sys.stdin.readline().split())
M = [sys.stdin.readline().split() for i in range(lin + 1)]

# Separação das somas das linhas e colunas
somas_linhas = list(map(int, [M[linha].pop() for linha in range(lin)]))
somas_colunas = list(map(int, M.pop()))
quantas_vars = len({var for linha in M for var in linha})
conhecidos = {}

# Função para encontrar variáveis que aparecem sozinhas em uma linha ou coluna
def achar_repetido():
    # Verifica linhas
    for i in range(lin):
        if len(set(M[i])) == 1:
            conhecidos[M[i][0]] = somas_linhas[i]
            return
    
    # Verifica colunas
    for y in range(col):
        coluna = [M[linha][y] for linha in range(lin)]
        if len(set(coluna)) == 1:
            conhecidos[coluna[0]] = somas_colunas[y]
            return

# Função para resolver o passatempo
def pense():
    while len(conhecidos) < quantas_vars:
        # Resolvi linhas
        for index_lin, linha in enumerate(M):
            if any(var in conhecidos for var in linha):
                soma_restante = somas_linhas[index_lin] - sum(conhecidos.get(var, 0) for var in linha)
                novas_vars = [var for var in linha if var not in conhecidos]
                if len(novas_vars) == 1:
                    conhecidos[novas_vars[0]] = soma_restante

        # Resolvi colunas
        for index_col in range(col):
            coluna = [M[linha][index_col] for linha in range(lin)]
            if any(var in conhecidos for var in coluna):
                soma_restante = somas_colunas[index_col] - sum(conhecidos.get(var, 0) for var in coluna)
                novas_vars = [var for var in coluna if var not in conhecidos]
                if len(novas_vars) == 1:
                    conhecidos[novas_vars[0]] = soma_restante

# Processo de solução
achar_repetido()
pense()

# Impressão das variáveis conhecidas
for var, valor in conhecidos.items():
    print(f'{var}: {valor}')
