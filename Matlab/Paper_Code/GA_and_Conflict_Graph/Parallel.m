function [Lp, Pp] = Parallel(Np, eta, x, T, S)
    %% 计算Du
    % 步骤1: 计算du
    du = zeros(size(S, 1), size(T, 1));
    for i = 1 : size(S, 1)
        for j = 1 : size(T, 1)
            du(i, j) = T(j, 1) * Np / S(i, 1) * 1000;
        end
    end
    % 步骤2: 计算Du
    Du = zeros(1, size(T, 1));
    for j = 1 : size(T, 1)
        for i = 1 : size(S, 1)
            if eta(i, j) == 0
                continue;
            end
            Du(1, j) = eta(i, j) * du(i, j);
        end
    end
    
    %% 计算Dc
    % 步骤1: 计算dc
    dc = zeros(size(S, 1), size(T, 1));
    for i = 1 : size(S, 1)
        for j = 1 : size(T, 1)
            dc(i, j) = T(j, 2) / S(i, 3) * 1000;
        end
    end
    % 步骤2: 计算Dc
    Dc = zeros(1, size(T, 1));
    for j = 1 : size(T, 1)
        for i = 1 : size(S, 1)
            if eta(i, j) == 0
                continue;
            end
            Dc(1, j) = eta(i, j) * dc(i, j);
        end
    end
    
    %% 计算Dhp
    Dhp = zeros(1, size(T, 1));
    for i = 1 : size(T, 1)
        for j = 1 : i - 1
            if x(j, i) == 0
                continue;
            end
            Dhp(1, i) = x(j, i) * (Du(1, j) + Dhp(j) + Dc(j) - Du(i));
        end
        Dhp(1, i) = max(0, max(Dhp(1, i)));
    end
    
    %% 计算Dd
    % 步骤1: 计算dd
    dd = zeros(size(S, 1), size(T, 1));
    for i = 1 : size(S, 1)
        for j = 1 : size(T, 1)
            dd(i, j) = T(j, 3) * Np / S(i, 2) * 1000;
        end
    end
    % 步骤2: 计算Dd
    Dd = zeros(1, size(T, 1));
    for j = 1 : size(T, 1)
        for i = 1 : size(S, 1)
            if eta(i, j) == 0
                continue;
            end
            Dd(1, j) = eta(i, j) * dd(i, j);
        end
    end
    
    %% 计算Dp
    Dp = zeros(1, size(T, 1));
    for i = 1 : size(T, 1)
        Dp(1, i) = Du(1, i) + Dc(1, i) + Dhp(1, i) + Dd(1, i);
    end
    
    %% 计算总延迟
    Lp = max(Dp);
%     disp("总延迟");
%     fprintf("%.8f\n", Lp);
    
    %% 计算卸载失败率
    % 计算子任务上行链路传输失败率
    Pu = zeros(1, size(T, 1));
    for j = 1 : size(T, 1)
        for i = 1 : size(S, 1)
            if eta(i, j) == 0
                continue;
            end
            Pu(1, j) = vpa(1 - vpa(1 - S(i, 4), 8) ^ (eta(i, j) * T(j, 1)), 8);
        end
    end
    % 计算子任务下行链路传输失败率
    Pd = zeros(1, size(T, 1));
    for j = 1 : size(T, 1)
        for i = 1 : size(S, 1)
            if eta(i, j) == 0
                continue;
            end
            Pd(1, j) = vpa(1 - vpa(1 - S(i, 5), 8) ^ (eta(i, j) * T(j, 3)), 8);
        end
    end
    % 计算子任务传输失败率
    P = zeros(1, size(T, 1));
    for i = 1 : size(T, 1)
        P(i) = Pu(i) + (1 - Pu(i)) * Pd(i);
    end
    % 计算任务的传输失败率
    Pp = 1;
    for i = 1 : size(T, 1)
        Pp = Pp * (1 - P(i));
    end
    Pp = 1 - Pp;
%     disp("任务的失败率");
%     fprintf("%.8f\n", Pp);
end










