import sys
input = sys.stdin.read 
data = input().strip().split('\n') # pega todos os inputs e coloca em uma lista

N = int(data[0])
results = []

for i in range(1, N + 1):
    line = data[i]
    space_index = line.find(' ')
    T = int(line[:space_index])
    S = line[space_index + 1:]
    
    L = len(S)
    d = T % L
    new_string = S[d:] + S[:d]
    results.append(new_string)

for result in results:
    print(result)