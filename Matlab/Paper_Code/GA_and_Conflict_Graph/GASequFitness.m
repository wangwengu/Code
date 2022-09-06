function [Lp, Pp, Fitness, Totaleta] = GASequFitness(nPop)
    [Np, ~, D, ~, x, T, S] = Constant(); % 导入所需的常量
    [n, m] = size(nPop);
    Lp = zeros(1, n);
    Pp = zeros(1, n);
    Fitness = zeros(1, n);
    Totaleta = zeros(n * m , m);
    for i = 1 : n
        for j = 1 : m
            Totaleta((i - 1) * m + nPop(i, j), j) = 1;
        end
        eta = Totaleta((i - 1) * m + 1 : i * m, :);
        [Lp(1, i), Pp(1, i)] = Sequential(Np, eta, x, T, S, D); % 调用并行计算的方法
        Fitness(1, i) = 1 / Lp(1, i) / Pp(1, i);
    end
end