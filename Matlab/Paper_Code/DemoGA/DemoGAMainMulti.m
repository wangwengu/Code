%% 初始化常量
n = 30;
m = 10 * 2; % 共2个变量, 每个变量的二进制占10位
MaxIt = 1000; % 最大迭代次数
mutationR = 0.003; % 变异概率

%% 主函数
% 初始化种群
nPop = randi([0, 1], n, m);
% 计算适应度
% 分离变量
x = nPop(:, 1 : 10);
y = nPop(:, 11 : 20);
translateResult = DemoGATranslateDNAMulti(x, y);
get_fitness = DemoGAFitnessMulti(translateResult);
%% 迭代
for i = 1 : MaxIt
    newPop = zeros(n + 1, m);
    for j = 1 : 2 : n
        % 选择
        [p1, p2] = DemoGASelectMulti(nPop);
        % 交叉
        [newPop(j, :), newPop(j + 1, :)] = DemoGACrossOverMulti(p1, p2);
        % 变异
        newPop(j, :) = DemoGAMutationMulti(newPop(j, :), mutationR);
        newPop(j + 1, :) = DemoGAMutationMulti(newPop(j + 1, :), mutationR);
    end
    % 新种群
    newPopulation = [nPop; newPop];
    % 分离变量
    x = newPopulation(:, 1 : 10);
    y = newPopulation(:, 11 : 20);
    translateResult = DemoGATranslateDNAMulti(x, y);
    get_fitness = DemoGAFitnessMulti(translateResult);
    [~, index] = sort(get_fitness, "descend");
    nPop = newPopulation(index(1 : n), :);
    translateResult = DemoGATranslateDNAMulti(nPop(1, 1 : 10), nPop(1, 11 : 20));
    x = translateResult(1, 1);
    y = translateResult(1, 2);
    fprintf("第%d代已经繁殖完毕, x = %d, y = %d, f(x, y) = x + y = %d\n", i, x, y, x + y);
end