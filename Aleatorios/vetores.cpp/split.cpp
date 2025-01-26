#include <iostream>
#include <vector>
#include <climits> // Para usar INT_MIN
using namespace std;

int main() {
    int qtd;
    cin >> qtd; 

    vector<int> numos;
    int newnum;
    for (int i = 0 ;  i< qtd ; i++){
        cin >> newnum;
        numos.push_back(newnum);
    }

    int maior = INT_MIN;
    int maior_pos;
    for( int i = 0; i < qtd ; i++) {
        if (numos[i] > maior){
            maior = numos[i];
            maior_pos = i;
        }
    }

    int somaesq = 0;
    for (int i = 0; i < maior_pos; i++){
        somaesq += numos[i];
    }

    int somadir = 0;
    for (int i = 1; i <= qtd - (maior_pos+1); i++) {
        somadir += numos[i+maior_pos];
    }

    cout << somaesq << "\n" << somadir;
}   