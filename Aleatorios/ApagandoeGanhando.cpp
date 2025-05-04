#include <iostream>
#include <stack>
#include <string>
#include <algorithm> 

using namespace std;

int main() 
{
    int n, d;
    string initial_number;

    while (cin >> n >> d)
    {
        if (n == 0 && d == 0) break;

        stack<int> s;
        cin >> initial_number;

        for (char c : initial_number) {
            int digit = c - '0'; 
            
            while (!s.empty() && d > 0 && s.top() < digit) {
                s.pop();
                d--;
            }

            s.push(digit); 
        }

        while (d > 0) {
            s.pop();
            d--;
        }

        string ans = "";
        while (!s.empty()) {
            ans += to_string(s.top());
            s.pop();
        }
        reverse(ans.begin(), ans.end());
        cout << ans << '\n';
    }
}
