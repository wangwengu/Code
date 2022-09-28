function [p1, p2] = DemoGASelectMulti(nPop)
    index = randperm(size(nPop, 1));
    p1 = nPop(index(1, 1), :);
    p2 = nPop(index(1, 2), :);
end