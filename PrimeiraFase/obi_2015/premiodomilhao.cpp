#include <iostream>

using namespace std;

int main(){

    int n, montante, novo_valor, result;

    cin >> n;

    for (int i = 1; i < n; ++i){
        cin >> novo_valor;
        montante += novo_valor;
        if (montante >= 1000000) {
            if ( i == 0 ){
                result = 1;
            }else{
            result = i;
            }

        }
    }

    cout << result;

}