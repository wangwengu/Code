#include <iostream>
#include <fstream>
using namespace std;
int n = 6, cnt = 0;
int cols[10];
int graph[10][10];
ofstream outFile;
void dfs(int x, int y, int s) {
    if (y == n) x ++, y = 0;
    if (x == n) {
        if (s == n) {
            outFile << "        [" << endl;
            for (int i = 0; i < n; i ++ ) {
                outFile << "           ";
                for (int j = 0; j < n; j ++ ) {
                    outFile << " " << graph[i][j];
                }
                outFile << ";" << endl;
            }
            outFile << "        ];" << endl;
            cnt ++;
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
    outFile.open("/Users/wangyaping/Code/Matlab/Paper_Code/GA_and_Conflict_Graph/GenerateSequGraph.m", ios::out | ios::trunc);
    outFile << "%% 生成串行卸载图(每行每列只能有一个皇后)" << endl;
    outFile << "function ParaGraph = GenerateSequGraph()" << endl;
    outFile << "    ParaGraph = [" << endl;
    dfs(0, 0, 0);
    outFile << "    ];" << endl;
    outFile << "end" << endl;
    outFile.close();
    return 0;
}