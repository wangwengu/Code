function [son1, son2] = GAParaCrossOver(p1, p2, taskNum, bitNum)
    % 单点交叉
    for k = 1 : taskNum
        index = randi([(k - 1) * bitNum + 1, k * bitNum - 1]);
        son1 = [p1(1, 1 : (k - 1) * bitNum) p1(1, (k - 1) * bitNum + 1 : index) p2(1, index + 1 : k * bitNum) p1(1, k * bitNum + 1 : size(p1, 2))];
        son2 = [p2(1, 1 : (k - 1) * bitNum) p2(1, (k - 1) * bitNum + 1 : index) p1(1, index + 1 : k * bitNum) p2(1, k * bitNum + 1 : size(p2, 2))];
    end
end