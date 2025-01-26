#include <iostream>
using namespace std;

int main ()
{
    int matriz[3][3];

    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            cin >> matriz[i][j];
        }
    }

    int maiorv;
    int maiorall = 0;
    for(int i = 0; i < 3; i++) {
        maiorv = 0;
        for(int j = 0; j < 3; j++) {
            if (matriz[i][j] > maiorv)
            {
                maiorv = matriz[i][j];
            }
        }
        if (maiorv > maiorall)
            {
                maiorall = maiorv;
            }

    }

    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if (matriz[i][j] == maiorall) {
                matriz[i][j] = -1;
            }
        }
    }

    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if (j > 0)
            {
                cout << " ";
            }
            cout << matriz[i][j];
        }
        if ( i < 2 )
        {
            cout << "\n";
        }
    }

}
