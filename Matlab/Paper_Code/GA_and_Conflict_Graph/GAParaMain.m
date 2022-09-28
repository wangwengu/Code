%% 常量
n = 10;
m = 4 * 2; % 4种选择
mutationR = 0.8; % 变异概率
MaxIt = 200;

%% 主函数
while true
    % 生成初代种群
    nPop = randi([0, 1], n, m);
    % 翻译DNA
    translateDNAResult = GAParaTranslateDNA(nPop);
    % 合格的种群
    [checkResult, nPop] = GAParaCheck(translateDNAResult, nPop);
    if size(nPop, 1) >= 1
        break;
    end
end
while size(nPop, 1) < n
    nPop = repmat(nPop, 2, 1);
end
nPop = nPop(1 : n, :);
Max_get_fitness = 0;
% 迭代
for i = 1 : MaxIt
    newPop = zeros(n, m);
    % 繁衍子代
    for j = 1 : 2 : n
        % 选择
        [p1, p2] = GAParaSelect(nPop);
        % 交叉
        [newPop(j, :), newPop(j + 1, :)] = GAParaCrossOver(p1, p2);
        % 变异
        newPop(j, :) = GAParaMutation(newPop(j, :), mutationR);
        newPop(j + 1, :) = GAParaMutation(newPop(j + 1, :), mutationR);
    end
    newPopulation = [nPop; newPop];
    % 翻译DNA
    translateDNAResult = GAParaTranslateDNA(newPopulation);
    % 合格的种群
    [checkResult, newPopulation] = GAParaCheck(translateDNAResult, newPopulation);
    % 计算适应度
    [Lp, Pp, get_fitness, eta] = GAParaFitness(checkResult);
    [~, index] = sort(get_fitness, "descend");
    if get_fitness(1, 1) > Max_get_fitness
        Max_get_fitness = get_fitness(1, 1);
        Min_Lp = Lp(1, 1);
        Min_Pp = Pp(1, 1);
        Best_matrix = checkResult(index(1, 1), :);
    end
    nPop = newPopulation(index(1 : n), :);
    fprintf("第%d代已经迭代结束\n", i);
end
fprintf("适应度: %f\n卸载延迟: %f\n卸载失败率: %f\n", Max_get_fitness, Min_Lp, Min_Pp);
fprintf("卸载矩阵:\n");
disp(Best_matrix);