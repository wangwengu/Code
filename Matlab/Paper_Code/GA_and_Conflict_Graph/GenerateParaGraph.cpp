#include <iostream>
#include <fstream>
using namespace std;
int n = 6;
int cols[10];
int graph[10][10];
ofstream outFile;
void dfs(int row) {
    if (row >= n) {
        outFile << "        [" << endl;
        for (int i = 0; i < n; i ++ ) {
            outFile << "           ";
            for (int j = 0; j < n; j ++ ) {
                outFile << " " << graph[i][j];
            }
            outFile << ";" << endl;
        }
        outFile << "        ];" << endl;
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
    outFile.open("/Users/wangyaping/Code/Matlab/Paper_Code/GA_and_Conflict_Graph/GenerateParaGraph.m", ios::out | ios::trunc);
    outFile << "%% 生成并行卸载图(每行每列只能有一个皇后)" << endl;
    outFile << "function ParaGraph = GenerateParaGraph()" << endl;
    outFile << "    ParaGraph = [" << endl;
    dfs(0);
    outFile << "    ];" << endl;
    outFile << "end" << endl;
    outFile.close();
    return 0;
}