%% 常量
n = 30;
m = 4 * 2; % 4种选择
mutationR = 0.005;
MaxIt = 20;

%% 主函数
while true
    % 生成初代种群
    nPop = randi([0, 1], n, m);
    % 翻译DNA
    translateDNAResult = GAParaTranslateDNA(nPop);
    % 合格的种群
    checkResult = GAParaCheck(translateDNAResult);
    if size(checkResult, 1) >= 1
        break;
    end
end
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
%     newPopulation = [nPop; newPop];
%     % 翻译DNA
%     translateDNAResult = GAParaTranslateDNA(newPopulation);
%     % 合格的种群
%     checkResult = GAParaCheck(translateDNAResult);
%     disp(checkResult);
%     % 计算适应度
%     [Lp, Pp, get_fitness, eta] = GAParaFitness(checkResult);
%     [~, index] = sort(get_fitness, "descend");
%     nPop = newPopulation(index(1 : n), :);
%     if get_fitness(1, 1) > Max_get_fitness
%         Max_get_fitness = get_fitness(1, 1);
%         Min_Lp = Lp(1, 1);
%         Min_Pp = Pp(1, 1);
%         Best_matrix = eta(1 : 4, :);
%     end
%     fprintf("并行卸载延迟:\n%f\n", Min_Lp);
%     fprintf("并行卸载失败率:\n%f\n", Min_Pp);
%     fprintf("适应度函数:\n%f\n", Max_get_fitness);
%     fprintf("卸载矩阵:\n");
%     disp(Best_matrix);
%     fprintf("第%d代已经迭代结束\n", i);
end