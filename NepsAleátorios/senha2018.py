
achou = False
tentativas = 0
while achou == False:
    chute = input()
    if chute == "2018":
        achou = True
    else:
        tentativas += 1
print(tentativas)