#include <iostream>
using namespace std;

int main() {
    double matriz[12][12]; 
    int coluna;
    cin >> coluna;
    char opr;
    cin >> opr;

    for (int i = 0; i < 12; i++) {
        for (int j = 0; j < 12; j++) {
            cin >> matriz[i][j];
        }
    }

    float soma = 0.0; 
    for (int i = 0; i < 12; i++) {
        soma += matriz[i][coluna];
    }

    if (opr == 'S') {
        cout << soma;
    } else if (opr == 'M') {
        float media = soma / 12; // Divisão com ponto flutuante
        cout << media;
    }

    return 0;
}
