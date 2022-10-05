[Np, U, D, ~, x, T, S] = Constant();
eta_para = [
    [0 0 0 0 1 0]
    [1 0 0 0 0 0]
    [0 1 0 0 0 0]
    [0 0 1 0 0 0]
    [0 0 0 1 0 0]
    [0 0 0 0 0 1]
];
[Ls, Ps] = Parallel(Np, eta_para, x, T, S);
fprintf("最优解:\n, 延迟: %f, 失败率: %f\n", Ls, Ps);
eta_sequ = [
    [0 0 0 0 1 0]
    [0 0 0 0 0 0]
    [0 1 0 1 0 1]
    [1 0 1 0 0 0]
    [0 0 0 0 0 0]
    [0 0 0 0 0 0]
];
k = 3;
[Ls, Ps] = Sequential(Np, eta_sequ, x, T, S, D, k);
fprintf("最优解:\n, 延迟: %f, 失败率: %f\n", Ls, Ps);