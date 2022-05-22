#include <iostream>
using namespace std;
const int N = 10010;
struct Node {
    int id, people, house, square;
    double avg_house, avg_square;
    bool operator < (const Node& W) const {
        if (W.avg_square != avg_square) {
            return W.avg_square < avg_square;
        }
        return W.id > id;
    }
}nodes[N];
int p[N], cnt[N], house[N], square[N];
int n;
int find(int x) {
    if (p[x] == x) return p[x];
    return p[x] = find(p[x]);
}
void merge(int a, int b) {
    if (a > b) swap(a, b);
    p[b] = a;
    cnt[a] += cnt[b];
    return;
}
int main() {
    for (int i = 0; i <= 9999; i ++ ) {
        p[i] = i;
        cnt[i] = 1;
    }
    scanf("%d", &n);
    for (int i = 0; i < n; i ++ ) {
        int c, a, b, k, h, s;
        scanf("%d%d%d%d", &c, &a, &b, &k);
        int pc = find(c);
        if (a != -1) {
            int pa = find(a);
            if (pa != pc) {
                merge(pa, pc);
            }
        }
        if (b != -1) {
            int pb = find(b);
            if (pb != pc) {
                merge(pb, pc);
            }
        }
        for (int j = 0, x; j < k; j ++ ) {
            int px = find(x);
            if (px != pc) {
                merge(px, pc);
            }
        }
        int t = find(c);
        scanf("%d%d", &h, &s);
        house[t] += h;
        square[t] += s;
    }
    f
    return 0;
}
