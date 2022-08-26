%% 初始化常量
n = 30; % 染色体的个数(矩阵的行)
m = 10; % 每条染色体上的基因的个数(矩阵的列); 采用二进制编码, 则其能表示的范围是[0~1024]
MaxIt = 200; % 迭代(繁殖)代数
crossoverR = 0.8; % 交叉概率
mutationR = 0.003; % 变异概率

%% 主函数
nPop = repmat(randi([0, 1], 1, m), n, 1); % 种群
for i = 1 : 1
    % 计算适应度
    translateResult = DemoGATranslateDNA(nPop);
    get_fitness = DemoGAFitness(translateResult);
    for j = 1 : 1
        % 选择
        [p1, p2] = DemoGASelect(nPop);
        % 交叉
    end
    % 变异
    
    fprintf("第%d代已经迭代(繁殖)结束\n", i);
end