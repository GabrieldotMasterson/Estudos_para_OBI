#include <stdio.h>

int essigna(int v[10], int x){
    for (int i = 0; i < 10; i = i +1){
        if (x == v[i]) {
            printf("SIM");
            return 0;
        }
    }
    printf ("NAO");
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