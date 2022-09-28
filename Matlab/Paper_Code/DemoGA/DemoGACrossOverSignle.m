function [son1, son2] = DemoGACrossOverSignle(p1, p2)
    % 单点交叉
    index = randi(size(p1, 2) - 1);
    son1 = [p1(1, 1 : index) p2(1, index + 1 : size(p1, 2))];
    son2 = [p2(1, 1 : index) p1(1, index + 1 : size(p2, 2))];
end