#include <iostream>
using namespace std;
typedef long long LL;
const int N = 33010, INF = 1e9;
int n, idx, root;
int g[N];
struct Tree {
    int l, r, key, val;
}tr[N];
int get_node(int key) {
    tr[++ idx].key = key;
    tr[idx].val = rand();
    return idx;
}
void zig(int &p) {
    int q = tr[p].l;
    tr[p].l = tr[q].r, tr[q].r = p, p = q;
    return;
}
void zag(int &p) {
    int q = tr[p].r;
    tr[p].r = tr[q].l, tr[q].l = p, p = q;
    return;
}
void build() {
    get_node(-INF);
    get_node(INF);
    root = 1;
    return;
}
void insert(int &u, int x) {
    if (!u) u = get_node(x);
    else if (x < tr[u].key) {
        insert(tr[u].l, x);
        if (tr[tr[u].l].val > tr[u].val) zig(u);
    }
    else if (x > tr[u].key) {
        insert(tr[u].r, x);
        if (tr[tr[u].r].val > tr[u].val) zag(u);
    }
    return;
}
int get_prev(int u, int x) {
    if (!u) return -INF;
    if (x <= tr[u].key) return get_prev(tr[u].l, x);
    return max(tr[u].key, get_prev(tr[u].r, x));
}
int get_next(int u, int x) {
    if (!u) return INF;
    if (x >= tr[u].key) return get_next(tr[u].r, x);
    return min(tr[u].key, get_next(tr[u].l, x));
}
int main() {
    scanf("%d", &n);
    build();
    for (int i = 1; i <= n; i ++ ) {
        scanf("%d", &g[i]);
        insert(root, g[i]);
    }
    LL res = 0;
    for (int i = 1; i <= n; i ++ ) {
        if (i == 1) res += g[i];
        else {
            res += min(g[i] - get_prev(root, g[i]), get_next(root, g[i]) - g[i]);
        }
    }
    printf("%lld\n", res);
    return 0;
}
