import sys

q_perguntas, resposta_enzo, resposta_lobo, gabarito = sys.stdin.read().splitlines() 

resposta_lobo = list(resposta_lobo)
resposta_enzo = list(resposta_enzo)
gabarito = list(resposta_lobo)

score = [0,0] # 0 lobo 1 enzo
indefinidos = [0,0] # 0 lobo 1 enzo

for index, item in enumerate(gabarito):
    if item != "?":
        if item == resposta_lobo[index]:
            score[0] += 1
        if item == resposta_enzo[index]:
            score[1] += 1
        if resposta_lobo[index] == "?":
            indefinidos[0] += 1
        if resposta_enzo[index] == "?":
            indefinidos[1] += 1
    else:
        indefinidos[0] += 1
        indefinidos[1] += 1
        print(indefinidos)

indefine = [score[0]+indefinidos[0],score[1]+indefinidos[1]]
print(indefine)
if indefine[0] == indefine[1]:
    print('Indefinido')



