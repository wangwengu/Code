%% 初始化常量
n = 30; % 染色体的个数(矩阵的行)
m = 10; % 每条染色体上的基因的个数(矩阵的列); 采用二进制编码, 则其能表示的范围是[0~1024]
MaxIt = 500; % 迭代(繁殖)代数
mutationR = 0.003; % 变异概率

%% 主函数
nPop = repmat(randi([0, 1], 1, m), n, 1); % 种群
% 初始化种群
translateResult = DemoGATranslateDNASignle(nPop);
get_fitness = DemoGAFitnessSignle(translateResult);
% 迭代
for i = 1 : MaxIt % 迭代次数
    newPop = zeros(n + 1, m);
    for j = 1 : 2 : n
        % 选择
        [p1, p2] = DemoGASelectSignle(nPop);
        % 交叉
        [newPop(j, :), newPop(j + 1, :)] = DemoGACrossOverSignle(p1, p2);
        % 变异
        newPop(j, :) = DemoGAMutationSignle(newPop(j, :), mutationR);
        newPop(j + 1, :) = DemoGAMutationSignle(newPop(j + 1, :), mutationR);
    end
    newPopulation = [nPop; newPop];
    translateResult = DemoGATranslateDNASignle(newPopulation);
    get_fitness = DemoGAFitnessSignle(translateResult);
    [~, index] = sort(get_fitness, "descend");
    nPop = newPopulation(index(1 : n), :);
    x = DemoGATranslateDNASignle(nPop(1, :));
    y = DemoGAFitnessSignle(x);
    fprintf("第%d代已经迭代(繁殖)结束, x = %d, y = %d\n", i, x, y);
end