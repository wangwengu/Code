#include <iostream>
#include <cstring>
#define x first
#define y second
using namespace std;
typedef pair<int, int> PII;
const int N = 110;
int n, m, k;
int dx[] = {-2, -1, 1, 2, 2, 1, -1, -2};
int dy[] = {1, 2, 2, 1, -1, -2, -2, -1};
PII match[N];
int g[N][N], st[N][N];
bool dfs(int x, int y) {
    for (int i = 0; i < 8; i ++ ) {
        int tx = x + dx[i];
        int ty = y + dy[i];
        if (tx < 1 || tx > n || ty < 1 || ty > m || g[tx][ty] || st[tx][ty]) continue;
        st[tx][ty] = true;
        PII t = match[tx][ty];
        if (t.x == 0 || dfs(t.x, t.y)) {
            match[t.x][t.y] = {x, y};
            return true;
        }
    }
    return false;
}
int main() {
    scanf("%d%d%d", &n, &m, &k);
    for (int i = 0; i < k; i ++ ) {
        int a, b;
        scanf("%d%d", &a, &b);
        g[a][b] = 1;
    }
    int res = 0;
    for (int i = 1; i <= n; i ++ ) {
        for (int j = 1; j <= m; j ++ ) {
            if ((i + j) & 1 && g[i][j]) continue;
            memset(st, 0, sizeof st);
            if (dfs(i, j)) res ++;
        }
    }
    cout << n * m - k - res << endl;
    return 0;
}
