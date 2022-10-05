#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int N = 100010;
int n, idx;
int g[N];
vector<int> points;
struct Tree {
    int l, r, cnt;
}tr[N * 4];
int find(int x) {
    return lower_bound(points.begin(), points.end(), x) - points.begin();
}
int build(int l, int r) {
    int u = ++ idx;
    if (l >= r) return u;
    int mid = l + r >> 1;
    tr[u].l = build(l, mid);
    tr[u].r = build(mid + 1, r);
    return u;
}
void insert(int u, int l, int r, int x) {
    if (l == r) {
        tr[u].cnt ++;
        return;
    }
    int mid = l + r >> 1;
    if (x <= mid) insert(tr[u].l, l, mid, x);
    else insert(tr[u].r, mid + 1, r, x);
    tr[u].cnt = tr[tr[u].l].cnt + tr[tr[u].r].cnt;
    return;
}
int query(int u, int l, int r, int k) {
    if (l >= r) return r;
    int mid = l + r >> 1;
    if (tr[tr[u].l].cnt >= k) return query(tr[u].l, l, mid, k);
    return query(tr[u].r, mid + 1, r, k - tr[tr[u].l].cnt);
}
int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i ++ ) {
        scanf("%d", &g[i]);
        points.push_back(g[i]);
    }
    sort(points.begin(), points.end());
    points.erase(unique(points.begin(), points.end()), points.end());
    build(0, points.size() - 1);
    for (int i = 1; i <= n; i ++ ) {
        insert(1, 0, points.size() - 1, find(g[i]));
        if (i & 1) printf("%d\n", g[query(1, 0, points.size() - 1, i + 1 >> 1)]);
    }
    return 0;
}
