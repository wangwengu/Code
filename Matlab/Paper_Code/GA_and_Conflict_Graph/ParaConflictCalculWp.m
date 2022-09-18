function calculateResult = ParaConflictCalculWp(T, S, Np)
    n = size(S, 1);
    m = size(T, 1);
    % 计算du
    du = zeros(n, m);
    dc = zeros(n, m);
    dd = zeros(n, m);
    pu = zeros(n, m);
    pd = zeros(n, m);
    wp = zeros(n, m);
    for i = 1 : n
        for j = 1 : m
            du(i, j) = T(j, 1) * Np / S(i, 1) * 1000;
            dd(i, j) = T(j, 3) * Np / S(i, 2) * 1000;
            dc(i, j) = T(j, 2) / S(i, 3) * 1000;
            pu(i, j) = vpa(vpa(1 - S(i, 4), 8) ^ T(j, 1), 8);
            pd(i, j) = vpa(vpa(1 - S(i, 5), 8) ^ T(j, 3), 8);
            wp(i, j) = vpa((du(i, j) + dc(i, j) + dd(i, j)) * vpa(1 - pu(i, j) * pd(i, j), 8), 8);
        end
    end
    calculateResult = wp;
end