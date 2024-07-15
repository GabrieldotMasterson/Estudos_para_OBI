vogais = ["a", "e", "i", 'o', 'u']
risada = input()
risadaVogais = []
for riso in risada: 
    if riso in vogais:
        risadaVogais.append(riso)
print(risadaVogais)
if risadaVogais == risadaVogais[::-1]:
    print("S")
else:
    print("N")