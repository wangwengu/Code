function [Ls, Ps] = sequential(Np, eta, x, T, S, D)
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

    %% 计算等待时间
    W = zeros(1, size(T, 1));
    for i = 1 : size(T, 1)
        for j = 1 : size(S, 1)
            for k = 1 : i - 1
                if eta(j, k) == 1 && eta(j, i) == 1
                    W(1, i) = W(1, i) + Du(1, k);
                end
            end
        end
    end
%     disp("等待时间");
%     disp(W);

    %% 计算Dhs
    Dhs = zeros(1, size(T, 1));
    for i = 1 : size(T, 1)
        for j = 1 : i - 1
            if x(j, i) == 0
                continue;
            end
            TDu = 0; % 临时变量
            for k = 1 : size(S, 1)
                for l = j + 1 : i
                    if eta(k, i) == 1 && eta(k, l) == 1
                        TDu = TDu + Du(1, l);
                    end
                end
            end
            Dhs(1, i) = x(j, i) * max(0, Dhs(1, j) + Dc(1, j) - TDu);
        end
    end
%     disp("持有时间");
%     disp(Dhs);

    %% 计算Ds
    Ds = zeros(1, size(T, 1));
    for i = 1 : size(T, 1)
        Ds(1, i) = W(1, i) + Du(1, i) + Dc(1, i) + Dhs(1, i);
    end
%     disp("子任务时间延迟");
%     disp(Ds);

    %% 计算Ls
    % 计算Dd
    k = 3; % 源服务器
    Dd = D * Np / S(k, 2) * 1000;
    Ls = max(Ds) + Dd;
%     disp("任务总延迟");
%     disp(Ls);

    %% 计算卸载失败率
    % 计算pu
    pu = zeros(1, size(T, 1));
    for j = 1 : size(T, 1)
        for i = 1 : size(S, 1)
            if eta(i, j) == 0
                continue;
            end
            pu(1, j) = vpa(1 - vpa(1 - S(i, 4), 8) ^ (eta(i, j) * T(j, 1)), 8);
        end
    end
    % 计算上传失败率Pu
    Pu = 1;
    for i = 1 : size(T, 1)
        for j = 1 : size(S, 1)
            if eta(j, i) == 0
                continue;
            end
            Pu = Pu * (1 - pu(1, i));
        end
    end
    Pu = 1 - Pu;
    % 计算下载失败率
    Pd = 1 - (1 - S(k, 5)) ^ D;
    % 计算总的卸载率
    Ps = Pu + (1 - Pu) * Pd;
%     disp("任务卸载失败率");
%     disp(Ps);
end














