#include <iostream>
using namespace std;
int n = 4;
int cols[10];
int graph[10][10];
void dfs(int row) {
    if (row >= n) {
        cout << "[\n";
        for (int i = 0; i < n; i ++ ) {
            cout << "    ";
            for (int j = 0; j < n; j ++ )
                cout << " " << graph[i][j];
            cout << ";" << endl;
        }
        cout << "];" << endl;
        return;
    }
    for (int i = 0; i < n; i ++ )
        if (!cols[i]) {
            cols[i] = true;
            graph[row][i] = 1;
            dfs(row + 1);
            graph[row][i] = 0;
            cols[i] = false;
        }
    return;
}
int main() {
    dfs(0);
    return 0;
}