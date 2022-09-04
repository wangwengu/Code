function translateResult = DemoGATranslateDNAMulti(x, y)
    translateResult = zeros(size(x, 1), 2);
    [n, m] = size(x);
    for i = 1 : n
        for j = m : -1 : 1
            if (x(i, j) == 1)
                translateResult(i, 1) = translateResult(i, 1) + 2 ^ (m - j);
            end
            if (y(i, j) == 1)
                translateResult(i, 2) = translateResult(i, 2) + 2 ^ (m - j);
            end
        end
    end
end