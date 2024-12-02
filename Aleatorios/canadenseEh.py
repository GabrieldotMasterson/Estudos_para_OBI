frase = input()

if frase[len(frase)-3:len(frase)] == "eh?":
    print("Canadian!")
else:
    print("Imposter!")