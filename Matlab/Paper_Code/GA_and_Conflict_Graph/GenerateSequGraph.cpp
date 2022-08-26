#include <iostream>
using namespace std;
int n = 3;
int cols[10];
int graph[10][10];
void dfs(int x, int y, int s) {
    if (y == n) x ++, y = 0;
    if (x == n) {
        if (s == n) {
            cout << "[" << endl;
            for (int i = 0; i < n; i ++ ) {
                cout << "    ";
                for (int j = 0; j < n; j ++ ) {
                    cout << " " << graph[i][j];
                }
                cout << ";" << endl;
            }
            cout << "];" << endl;
        }
        return;
    }
    // 不放
    dfs(x, y + 1, s);
    // 放
    if (!cols[y] && (!y || !graph[x][y - 1])) {
        cols[y] = true;
        graph[x][y] = 1;
        dfs(x, y + 1, s + 1);
        cols[y] = false;
        graph[x][y] = 0;
    }
    return;
}
int main() {
    dfs(0, 0, 0);
    return 0;
}