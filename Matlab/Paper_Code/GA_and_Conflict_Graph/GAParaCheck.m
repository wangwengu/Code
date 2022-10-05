function [checkResult, nPop] = GAParaCheck(translateDNAResult, nPop)
    [n, m] = size(translateDNAResult);
    checkResult = zeros(n, m);
    k = 1; % 符合条件子代的下标
    index = zeros(1, n);
    for i = 1 : n
        flag = true;
        hash = zeros(1, m);
        for j = 1 : m
            gene = translateDNAResult(i, j);
            if gene > m
                flag = false;
                break;
            end
            % 判断任何俩任务不可分配到同一服务器
            hash(gene) = hash(gene) + 1;
            if hash(gene) > 1
                flag = false;
                break;
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