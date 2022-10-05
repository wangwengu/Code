function translateDNAResult = GAParaTranslateDNA(nPop)
    [n, m] = size(nPop);
    % 子任务的数量
    taskNum = 6;
    % 子任务的数量的二进制个数(向上取整)
    bitNum = ceil(log2(taskNum));
    translateDNAResult = zeros(n, taskNum);
    for i = 1 : n
        index = taskNum;
        exp = 0;
        for j = m : -1 : 1
            if nPop(i, j) == 1
                translateDNAResult(i, index) = translateDNAResult(i, index) + 2 ^ exp;
            end
            exp = exp + 1;
            if exp == bitNum
                exp = 0;
                index = index - 1;
            end
        end
    end
    % 将0~2 ^ n - 1变成1~2 ^ n
    translateDNAResult = translateDNAResult + 1;
end