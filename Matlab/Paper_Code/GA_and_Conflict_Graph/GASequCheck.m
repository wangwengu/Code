function [checkResult, nPop] = GASequCheck(translateDNAResult, nPop, sinkServer)
    [n, m] = size(translateDNAResult);
    checkResult = zeros(n, m);
    k = 1; % 符合条件子代的下标
    index = zeros(1, n);
    for i = 1 : n
        flag = true;
        hash = zeros(1, m);
        if translateDNAResult(i, m) ~= sinkServer
            continue;
        end
        for j = 1 : m
            gene = translateDNAResult(i, j);
            % 判断是否越界
            if gene > m
                flag = false;
                break;
            end
            % 判断任何连续的两个子任务不可分配到同一个服务器
            hash(gene) = hash(gene) + 1;
            if hash(gene) > 1
                if and(j > 1, translateDNAResult(i, j - 1) == gene)
                    flag = false;
                    break;
                end
            end
        end
        if flag
            checkResult(k, :) = translateDNAResult(i, :);
            index(1, k) = i;
            k = k + 1;
        end
    end
    index(index == 0) = [];
    nPop = nPop(index, :);
    % 干掉所有零行
    checkResult(all(checkResult == 0, 2), :) = [];
end