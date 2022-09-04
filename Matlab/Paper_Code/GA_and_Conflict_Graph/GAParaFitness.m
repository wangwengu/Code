function [Lp, Pp, Fitness, eta] = GAParaFitness(nPop)
    [Np, ~, ~, ~, x, T, S] = Constant(); % 导入所需的常量
    [n, m] = size(nPop);
    Lp = zeros(1, n);
    Pp = zeros(1, n);
    Fitness = zeros(1, n);
    eta = zeros(n * m , m);
    for i = 1 : n
        for j = 1 : m
            eta((i - 1) * m + nPop(i, j), j) = 1;
        end
        [Lp(1, i), Pp(1, i)] = Parallel(Np, eta, x, T, S); % 调用并行计算的方法
        Fitness(1, i) = 1 / Lp(1, i) / Pp(1, i);
    end
end