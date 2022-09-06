function [p1, p2] = GASequSelect(nPop)
    n = size(nPop, 1);
    index = randperm(n);
    p1 = nPop(index(1, 1), :);
    p2 = nPop(index(1, 2), :);
end