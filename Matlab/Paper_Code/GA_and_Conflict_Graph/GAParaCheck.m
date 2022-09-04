function checkResult = GAParaCheck(translateDNA)
    [n, m] = size(translateDNA);
    checkResult = zeros(n, m);
    index = 1; % 符合条件子代的下标
    for i = 1 : n
        flag = true;
        hash = zeros(1, m);
        for j = 1 : m
            gene = translateDNA(i, j);
            % 判断任何俩任务不可分配到同一服务器
            hash(gene) = hash(gene) + 1;
            if hash(gene) > 1
                flag = false;
                break;
            end
        end
        if flag
            checkResult(index, :) = translateDNA(i, :);
            index = index + 1;
        end
    end
    % 干掉所有零行
    checkResult(all(checkResult == 0, 2), :) = [];
end