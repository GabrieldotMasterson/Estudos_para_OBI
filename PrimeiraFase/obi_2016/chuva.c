#include <stdio.h>
#include <stdlib.h>

int main() {
    int *piscina;
    int qtd;
    scanf("%d", &qtd );
    piscina = (int*)malloc(qtd*sizeof(int));

    for (int i = 0 ; i < qtd; i++)
    {
        scanf("%d", &piscina[i]);
    }

    int result;
    int borda;
    for (int i = 0 ; i < qtd; i++)
    {

    }
}