 #include <stdio.h>
// // parece hard
// // prefix sum?


// int main() {
// // percorrer a lista de alunos verificando qual é dificil por cada complexidade bem alt

//     int qtd;
//     scanf("%d", qtd);

//     for(int i; i < qtd; i = i+1){
//         int passo;
//         if (passo > 365){
//             passo = passo % 365;
//         }

        
//         for(int passo; i < qtd; i = i+1){
            
//         }

//     }
    

// }

#include <stdio.h>
// os numeros quadrados perfeitos são impares
// math issue
int main() {
    int qtd;
    scanf("%d", &qtd);

    for (int i = 1; i * i <= qtd; i++) {
        printf("%d ", i * i);
    }

    return 0;
}

