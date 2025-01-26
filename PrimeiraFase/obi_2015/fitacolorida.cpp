#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main() {
    vector<int> fita;
    int qtd;
    cin >> qtd ;

    int nn;
    for(int i = 0; i < qtd; i++)
    {
        cin >> nn;
        fita.push_back(nn);
    }

    for (int i = 0; i < qtd; i++)
    {
        int menesq= INT_MAX;
        for (int j = i ; j >= 0 ; j--)
        {
            if (fita[j] == 0){
                menesq = i-j;
                break;

            }
            
        }

        int mendir = INT_MAX;
        for (int j = i ; j < qtd ; j++)
        {
            if (fita[j] == 0){
                mendir = j-i;
                break;

            }
            
        }

        if (mendir > menesq) {fita[i] = menesq;} else {fita[i] = mendir;}
    }

    for(int i = 0; i < qtd; i++)
    {
        cout << fita[i];
        if ( i < qtd){
            cout << " ";
        }
    }
}