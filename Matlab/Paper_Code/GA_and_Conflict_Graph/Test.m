%% 导入所需要的变量
[Np, U, D, ~, x, T, S] = Constant();
%% 生成并行计算图和并行计算图
[n, m] = deal(size(S, 1), size(T, 1));
Min_Lp = 0x3f3f3f3f;
Min_Pp = 0x3f3f3f3f;
Min_Lp_eta = zeros(n, m);
ParaGraph = GenerateParaGraph();
for i = 1 : n : size(ParaGraph, 1)
    eta_para = ParaGraph(i : i + n - 1, :);
    [Lp, Pp] = Parallel(Np, eta_para, x, T, S);
    if Lp < Min_Lp
        Min_Lp = Lp;
        Min_Pp = Pp;
        Min_Lp_eta = eta_para;
    end
end
fprintf("并行卸载延迟:\n%f\n", Min_Lp);
fprintf("并行卸载失败率:\n%f\n", Min_Pp);
fprintf("并行卸载矩阵:\n");
disp(Min_Lp_eta);
k = 3; % 3号服务器被选作源服务器
Min_Ls = 0x3f3f3f3f;
Min_Ps = 0x3f3f3f3f;
Min_Ls_eta = zeros(n, n);
SequGraph = GenerateSequGraph();
for i = 1 : n : size(SequGraph, 1)
    eta_sequ = SequGraph(i : i + n - 1, :);
    if eta_sequ(k, m) ~= 1
        continue;
    end
    [Ls, Ps] = Sequential(Np, eta_sequ, x, T, S, D, k);
    if Ls < Min_Ls
        Min_Ls = Ls;
        Min_Ps = Ps;
        Min_Ls_eta = eta_sequ;
    end
end
fprintf("串行卸载延迟:\n%f\n", Min_Ls);
fprintf("串行卸载失败率:\n%f\n", Min_Ps);
fprintf("串行卸载矩阵:\n");
disp(Min_Ls_eta);