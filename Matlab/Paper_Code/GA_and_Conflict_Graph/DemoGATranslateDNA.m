function translateResult = DemoGATranslateDNA(nPop)
    translateResult = zeros(1, size(nPop, 1));
    [n, m] = size(nPop);
    for i = 1 : n
        for j = m : -1 : 1
            if nPop(i, j) == 1
                translateResult(1, i) = translateResult(1, i) + bitshift(1, m - j);
            end
        end
    end
end