#include <stdio.h>

int main() {
    printf("%d n %d", 4, 5);
    /* 
        \n nove linha
        \t tabulaçao
        \\ Barra invertida

        Definir preisao
        %.[x]f
        %o octal
        %x hexadecimal
        #X hexadecimal maisculu

    */
   printf("%d n %d\n", 4, 5);
   printf("%d n\t%d\n", 4, 5);
   printf("%d \\ %d\n", 4, 5);
   printf("%d %% %d\n", 4, 5);
   printf("[%-3d][%3d][%03d]\n", 4, 5, 6);
   printf("%.7f\n", 1.030349499393939);

   return 0;
}