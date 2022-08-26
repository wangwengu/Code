%% 常量
Np = 20;
U = 1000;
D = 200;

%% 初始化
% 定义卸载决策矩阵
eta = [
    [0 0 0 0]
    [0 0 0 0]
    [0 1 0 1]
    [1 0 1 0]
];
% 定义依赖矩阵
x = [
    [0 1 0 0]
    [0 0 1 0]
    [0 0 0 1]
    [0 0 0 0]
];
% 定义子任务属性
T = [
    [112 0.85 * 1e7 23]
    [162 2.48 * 1e7 33]
    [589 7.05 * 1e7 116]
    [137 1.13 * 1e7 28]
];
% 定义服务器属性
S = [
    [4.3 * 1e6 5.2 * 1e6 7.1 * 1e9 0.16 * 1e-6 1.0 * 1e-7]
    [3.9 * 1e6 4.8 * 1e6 2.0 * 1e9 7.18 * 1e-6 1.2 * 1e-7]
    [5.5 * 1e6 6.5 * 1e6 3.6 * 1e9 0.10 * 1e-6 0.3 * 1e-7]
    [6.4 * 1e6 6.4 * 1e6 7.2 * 1e9 0.07 * 1e-6 0.4 * 1e-7]
];
%% 生成并行计算图和并行计算图
n = 4; % 正方形图边长
Min_Lp = 0x3f3f3f3f;
Min_Pp = 0x3f3f3f3f;
Min_Lp_eta = zeros(n, n);
Min_Ls = 0x3f3f3f3f;
Min_Ps = 0x3f3f3f3f;
Min_Ls_eta = zeros(n, n);
ParaGraph = GenerateParaGraph();
SequGraph = GenerateSequGraph();
for i = 1 : n : size(ParaGraph, 1)
    eta_para = ParaGraph(i : i + n - 1, :);
    eta_sequ = SequGraph(i : i + n - 1, :);
    [Lp, Pp] = Parallel(Np, eta_para, x, T, S);
    [Ls, Ps] = Sequential(Np, eta_sequ, x, T, S, D);
    if Lp < Min_Lp
        Min_Lp = Lp;
        Min_Pp = Pp;
        Min_Lp_eta = eta_para;
    end
    if Ls < Min_Ls
        Min_Ls = Ls;
        Min_Ps = Ps;
        Min_Ls_eta = eta_sequ;
    end
end
fprintf("并行卸载延迟:\n%f\n", Min_Lp);
fprintf("并行卸载失败率:\n%f\n", Min_Pp);
fprintf("并行卸载矩阵:\n");
disp(Min_Lp_eta);
fprintf("串行卸载延迟:\n%f\n", Min_Ls);
fprintf("串行卸载失败率:\n%f\n", Min_Ps);
fprintf("串行卸载矩阵:\n");
disp(Min_Ls_eta);