#include <iostream>
#include <cstring>
#define x first
#define y second
using namespace std;
typedef pair<int, int> PII;
const int N = 110;
int n, m;
int dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1};
int g[N][N], st[N][N];
PII match[N][N];
bool dfs(int x, int y) {
    for (int i = 0; i < 4; i ++ ) {
        int tx = x + dx[i];
        int ty = y + dy[i];
        if (tx < 1 || tx > n || ty < 1 || ty > m || !g[tx][ty] || st[tx][ty]) continue;
        st[tx][ty] = true;
        PII t = match[tx][ty];
        if (t.x == -1 || dfs(t.x, t.y)) {
            match[tx][ty] = {x, y};
            return true;
        }
    }
    return false;
}
int main() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; i ++ ) {
        int x, y;
        scanf("%d%d", &x, &y);
        g[x][y] = true;
    }
    memset(match, -1, sizeof match);
    int res = 0;
    // 枚举每一个奇数格子
    for (int i = 1; i <= n; i ++ ) {
        for (int j = 1; j <= n; j ++ ) {
            if ((i + j) & 1 && !g[i][j]) {
                memset(st, 0, sizeof st);
                if (dfs(i, j)) res ++;
            }
        }
    }
    cout << res << endl;
    return 0;
}
