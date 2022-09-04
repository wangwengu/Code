function splitResult = GAParaSplit(p1, p2)
    splitResult = zeros(2, 4);
    index = 1;
    for i = 1 : 2 : size(p1, 2)
        splitResult(1, index) = p1(1, (i - 1) * 2 + 1 : i * 2);
        splitResult(2, index) = p2(1, (i - 1) * 2 + 1 : i * 2);
        index = index + 1;
    end
end