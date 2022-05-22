#include <iostream>
using namespace std;
string A, B;
string a, b;
int main() {
    cin >> A >> B;
    string t = A + B;
    sort(t.begin(), t.end(), [&](char c1, char c2) {
        return c1 > c2;
    });
    while (cin >> a >> b, a != "0" && b != "0") {
        if (a[0] == '0' || b[0] == '0') cout << "No" << endl;
        string t1 = a + b;
        sort(t1.begin(), t1.end(), [&](char c1, char c2) {
            return c1 > c2;
        })
        if (t1 != t) cout << "No" << endl;
        else cout << "Yes" << endl;
    }
    return 0;
}
