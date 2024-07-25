#https://neps.academy/br/exercise/2438

n = int(input())
valores = []
for i in range(n):
    valores.append(int(input()))


intervalos = []
intervalo = 0
nums = []

for index in range(len(valores)):
    if valores[index] not in nums:
        intervalo += 1
        nums.append(valores[index])
    else:
        intervalos.append(intervalo)
        intervalo = 0

print(max(intervalos))