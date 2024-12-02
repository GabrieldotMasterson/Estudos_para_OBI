texto = input().split()
letras = input().strip()
achou = 0
for i in range(len(texto)):
    for j in letras:  
        if j in [x for x in texto[i]]:
            achou+=1
            break



print(achou)
            
        

