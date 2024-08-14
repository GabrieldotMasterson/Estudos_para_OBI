## Aprendido com: https://www.youtube.com/watch?v=CVwjTXXEl1E

def fibonnachi(valor, memo=None): # 
    if memo is None: memo = {}
    if valor in memo: return memo[valor]
    if valor <= 1: return 1

    memo[valor] = (fibonnachi(valor-1, memo) + fibonnachi(valor-2, memo)) # função chama a si mesmo para construir a memória

    return memo[valor]
    
import sys
n = int(sys.stdin.readline())

print(fibonnachi(n))