#https://neps.academy/br/exercise/2436
total_estudantes, n_amigos, n_enimigos = map(int, input().split())

grupos = {'amigos': [], 'enimigos': []}


for _ in range(n_amigos):
    grupos['amigos'].append(list(map(int, input().split())))

for _ in range(n_enimigos):
    grupos['enimigos'].append(list(map(int, input().split())))

total_restricoes = 0
for _ in range(total_estudantes//3):
    grupo = list(map(int, input().split()))
    amigos = 1
    for i in grupos['amigos']:
        print(i)
        if i in grupo:
            amigos += 1
    if amigos < 2:
        total_restricoes += 1

print(total_restricoes)

