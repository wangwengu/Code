%% 导入所需要的变量
[Np, U, D, ~, x, T, S] = Constant();
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