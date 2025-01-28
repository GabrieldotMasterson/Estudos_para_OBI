#include <stdio.h>

int essigna(int v[10], int x){
    int apar = 0;
    int ind[] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
    for (int i = 0; i < 10; i = i +1){
        if (x == v[i]) {
            ind[apar] = i;
            apar = apar + 1;
        }
    }
    if (apar==0){
        printf("Mia X");
    }else{
        printf("%d\n", apar);
        for (int i = 0; i < 10; i++){
            if (ind[i] != -1){
                printf("%d ",ind[i]);
            }
        }
    }
    return 0;
}

int main() {
    int v[10];
    int x;
    for (int i = 0; i < 10; i = i +1){
        scanf("%d", &v[i]);
    } 
    scanf("%d", &x);
    essigna(v, x);
    
}