valores = list(map(int, input().split()))

if valores.count(1) == 1:
    if valores[0] == 1: print("A")
    if valores[1] == 1: print("B")
    if valores[2] == 1: print("C")

elif valores.count(0) == 1:
    if valores[0] == 0: print("A")
    if valores[1] == 0: print("B")
    if valores[2] == 0: print("C")

else: print("*")