#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int qtd;
    cin >> qtd;
    vector<int> v;

    int valormassa;
    for (int i = 0; i < qtd; i++)
    {
        cin >> valormassa;
        v.push_back(valormassa);
    }

    int maiorValor = -1;
    vector<int> maisApar;
    int novoValor;

    for (int i = 1; i <= 12; i++) 
    {
        novoValor = count(v.begin(), v.end(), i);

        if (novoValor > maiorValor) 
        {
            maiorValor = novoValor;
            maisApar.clear(); // Limpa os valores antigos
            maisApar.push_back(i);
        }
        else if (novoValor == maiorValor) 
        {
            maisApar.push_back(i);
        }
    }

    sort(maisApar.begin(), maisApar.end());
    for (int num : maisApar)
    {
        cout << num << " ";
    }

    return 0;
}
