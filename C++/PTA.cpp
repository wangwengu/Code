#include <iostream>
#include <cstring>
#include <unordered_set>
using namespace std;
typedef long long LL;
const int N = 100010, M = 2000010;
int n, m, mod, idx, timestamp, top, scc_cnt;
int h[N], hs[N], e[M], ne[M], dfn[N], low[N], stk[N], in_stk[N], id[N], scc_size[N], f[N], g[N];
unordered_set<LL> hx;
void add(int h[], int a, int b) {
    e[idx] = b;
    ne[idx] = h[a];
    h[a] = idx ++;
    return;
}
void tarjan(int u) {
    dfn[u] = low[u] = ++ timestamp;
    stk[ ++ top] = u, in_stk[u] = true;
    for (int i = h[u]; i != -1; i = ne[i]) {
        int j = e[i];
        if (!dfn[j]) {
            tarjan(j);
            low[u] = min(low[u], low[j]);
        }
        else if (in_stk[j]) low[u] = min(low[u], dfn[j]);
    }
    if (dfn[u] == low[u]) {
        int y;
        ++ scc_cnt;
        do {
            y = stk[top -- ];
            in_stk[y] = false;
            id[y] = scc_cnt;
            scc_size[scc_cnt] ++;
        } while (y != u);
    }
    return;
}
int main() {
    scanf("%d%d%d", &n, &m, &mod);
    memset(h, -1, sizeof h);
    memset(hs, -1, sizeof hs);
    for (int i = 0; i < m; i ++ ) {
        int a, b;
        scanf("%d%d", &a, &b);
        add(h, a, b);
    }
    for (int i = 1; i <= n; i ++ )
        if (!dfn[i])
            tarjan(i);
    for (int i = 1; i <= n; i ++ )
        for (int j = h[i]; j != -1; j = ne[j]) {
            int k = e[j];
            int a = id[i], b = id[k];
            LL t = a * 1000000ll + b;
            if (a != b && !hx.count(t)) {
                add(hs, a, b);
                hx.insert(t);
            }
        }
    for (int i = scc_cnt; i; i -- ) {
        if (!f[i]) {
            f[i] = scc_size[i];
            g[i] = 1;
        }
        for (int j = hs[i]; j != -1; j = ne[j]) {
            int k = e[j];
            if (f[i] + scc_size[k] > f[k]) {
                f[k] = f[i] + scc_size[k];
                g[k] = g[i];
            }
            else if (f[i] + scc_size[k] == f[k])
                g[k] = (g[k] + g[i]) % mod;
        }
    }
    int maxf = -1, sum = 0;
    for (int i = 1; i <= scc_cnt; i ++ )
        if (f[i] > maxf) {
            maxf = f[i];
            sum = g[i];
        }
        else if (f[i] == maxf) sum = (sum + g[i]) % mod;
    printf("%d\n%d\n", maxf, sum);
    return 0;
}
