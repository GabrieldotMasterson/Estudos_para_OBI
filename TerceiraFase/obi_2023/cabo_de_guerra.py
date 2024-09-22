from itertools import combinations

# Lê as forças dos participantes
forcas = list(map(int, input().split()))
indexes = list(range(6))

def verificar():
    # Gera todas as combinações possíveis de 3 jogadores entre 6
    for time1 in combinations(indexes, 3):
        time2 = [f for f in indexes if f not in time1]

        time1 = [forcas[x] for x in time1 ]
        time2 = [forcas[x] for x in time2 ]
        
        # Verifica se a soma das forças dos dois times é igual
        if sum(time1) == sum(time2):
            return "S"
    return "N"

# Imprime o resultado
print(verificar())
