#include <iostream>

using namespace std;

int main() {

    int M;
    cin >> M;

    cout << M/60 << endl;
    M = M - ((M/60)*60);
    cout << M%60;


}