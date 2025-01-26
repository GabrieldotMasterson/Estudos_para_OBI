#include <iostream>
using namespace std;
#include <vector>
int main() 
{

    vector<int> listapar;
    vector<int> listaimpa;

    int novoval;
    for (int i = 0; i < 10; i++)
    {
        cin >> novoval;
        if (novoval % 2 == 0)
        {
            listapar.push_back(novoval);
        }else
        {
            listaimpa.push_back(novoval);
        }
    }

    for (int i = 0; i < size(listapar); i++)
    {
        if (i>0){
            cout << " " << listapar[i];
        }else{
            cout << listapar[i];
        }
        
    }
    cout << "\n";
    for (int i = 0; i < size(listaimpa); i++)
    {
        if (i>0){
            cout << " " << listaimpa[i];
        }else{
            cout << listaimpa[i];
        }
        
    }
}