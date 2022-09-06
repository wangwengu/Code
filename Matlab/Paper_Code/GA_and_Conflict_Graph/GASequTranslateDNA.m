function translateDNAResult = GASequTranslateDNA(nPop)
    [n, m] = size(nPop);
    translateDNAResult = zeros(n, 4);
    for i = 1 : n
        index = 4;
        exp = 0;
        for j = m : -1 : 1
            if nPop(i, j) == 1
                translateDNAResult(i, index) = translateDNAResult(i, index) + 2 ^ exp;
            end
            exp = exp + 1;
            if exp == 2
                exp = 0;
                index = index - 1;
            end
        end
    end
    % 将0~2 ^ n - 1变成1~2 ^ n
    translateDNAResult = translateDNAResult + 1;
end