%% 引入常量
[Np, ~, D, eta, x, T, S] = Constant();
% 最优解
eta_sequ = [
    [0 0 0 1 0 0]
    [0 0 0 0 0 0]
    [0 1 0 0 0 1]
    [1 0 1 0 1 0]
    [0 0 0 0 0 0]
    [0 0 0 0 0 0]
];
% 最优解
eta_para = [
    [0 0 0 0 0 1]
    [1 0 0 0 0 0]
    [0 0 0 1 0 0]
    [0 0 1 0 0 0]
    [0 1 0 0 0 0]
    [0 0 0 0 1 0]
];
% 迭代五百次
eta_sequ_GA = [
    [0 1 0 0 0 1]
    [0 0 0 0 0 0]
    [1 0 0 1 0 0]
    [0 0 1 0 1 0]
    [0 0 0 0 0 0]
    [0 0 0 0 0 0]
];
% 迭代五百次
eta_para_GA = [
    [0 0 0 0 1 0]
    [1 0 0 0 0 0]
    [0 1 0 0 0 0]
    [0 0 1 0 0 0]
    [0 0 0 1 0 0]
    [0 0 0 0 0 1]
];
taskNum = size(T, 1);
optSequLatency = zeros(1, 10);
optSequFailure = zeros(1, 10);
optParaLatency = zeros(1, 10);
optParaFailure = zeros(1, 10);
GASequLatency = zeros(1, 10);
GASequFailure = zeros(1, 10);
GAParaLatency = zeros(1, 10);
GAParaFailure = zeros(1, 10);
%% 获取数据
% 设置不同的U大小
for U = 200 : 200 : 2000
    % 随机生成taskNum个随机数
    randNum = randi([U - 200, U], 1, taskNum);
    % 归一化
    randNum = U * randNum / sum(randNum);
    % 四舍五入
    randNum = floor(randNum);
    % 修正最后一个数
    randNum(1, taskNum) = randNum(1, taskNum) + U - sum(randNum);
    % 将数值赋给T
    for j = 1 : taskNum
        T(j, 1) = randNum(1, j);
    end
    % 统计不同大小的包对于串行卸载的延迟
    k = 3; % 3号服务器被选作源服务器
    % 最优算法
    [Ls, Ps] = Sequential(Np, eta_sequ, x, T, S, D, k);
    optSequLatency(1, U / 200) = Ls;
    optSequFailure(1, U / 200) = Ps;
    [Lp, Pp] = Parallel(Np, eta_para, x, T, S);
    optParaLatency(1, U / 200) = Lp;
    optParaFailure(1, U / 200) = Pp;
    % 遗传算法
    [Ls, Ps] = Sequential(Np, eta_sequ_GA, x, T, S, D, k);
    GASequLatency(1, U / 200) = Ls;
    GASequFailure(1, U / 200) = Ps;
    [Lp, Pp] = Parallel(Np, eta_para_GA, x, T, S);
    GAParaLatency(1, U / 200) = Lp;
    GAParaFailure(1, U / 200) = Pp;
end
%% 画图
% 卸载延迟图
figure(1);
pointOptSequ_x = 200 : 200 : 2000;
pointOptSequ_y = optSequLatency;
pointOptPara_x = 200 : 200 : 2000;
pointOptPara_y = optParaLatency;
pointGASequ_x = 200 : 200 : 2000;
pointGASequ_y = GASequLatency;
pointGAPara_x = 200 : 200 : 2000;
pointGAPara_y = GAParaLatency;
plot( ...
    pointOptSequ_x, pointOptSequ_y, '-*r', ...
    pointGASequ_x, pointGASequ_y, '-*b' ...
);
hold on;
plot( ...
    pointOptPara_x, pointOptPara_y, '--or', ...
    pointGAPara_x, pointGAPara_y, '--ob' ...
);
axis([200, 2000, 0, 110]);
set(gca, 'XTick', 200 : 200 : 2000);
set(gca, 'YTick', 0 : 10 : 110);
legend( ...
    'Optimum solution - sequential offloading', ...
    'Genetic algorithm - sequential offloading', ...
    'Optimum solution - parallel offloading', ...
    'Genetic algorithm - parallel offloading', ...
    'Location', 'northwest' ...
);
xlabel('U(packets)');
ylabel('Latency(ms)');
% 卸载失败率图
% figure(2);
% pointA_x = 200 : 200 : 2000;
% pointA_y = optSequFailure;
% pointB_x = 200 : 200 : 2000;
% pointB_y = optParaFailure;
% plot(pointA_x, pointA_y, '-*b', pointB_x, pointB_y, '-or');
% axis([200, 2000, 0, 5 * 1e-3]);
% set(gca, 'XTick', 200 : 200 : 2000);
% set(gca, 'YTick', 0 : 5 * 1e-4 : 5 * 1e-3);
% legend('Optimum solution - sequential offloading', 'Optimum solution - parallel offloading', 'Location', 'northwest');
% xlabel('U(packets)');
% ylabel('Task offloading failure probability');