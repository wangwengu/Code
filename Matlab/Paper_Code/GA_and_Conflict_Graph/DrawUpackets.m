%% 引入常量
[Np, ~, D, eta, x, T, S] = Constant();
taskNum = size(T, 1);
sequLatency = zeros(1, 10);
sequFailure = zeros(1, 10);
paraLatency = zeros(1, 10);
paraFailure = zeros(1, 10);
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
    [Ls, Ps] = Sequential(Np, eta, x, T, S, D, k);
    sequLatency(1, U / 200) = Ls;
    sequFailure(1, U / 200) = Ps;
    [Lp, Pp] = Parallel(Np, eta, x, T, S);
    paraLatency(1, U / 200) = Lp;
    paraFailure(1, U / 200) = Pp;
%     fprintf("Ps = %f, Pp = %f\n", Ps, Pp);
end
%% 画图
% 卸载延迟图
figure(1);
pointA_x = 200 : 200 : 2000;
pointA_y = sequLatency;
pointB_x = 200 : 200 : 2000;
pointB_y = paraLatency;
plot(pointA_x, pointA_y, '-*b', pointB_x, pointB_y, '-or');
axis([200, 2000, 0, 110]);
set(gca, 'XTick', 200 : 200 : 2000);
set(gca, 'YTick', 0 : 10 : 110);
legend('Optimum solution - sequential offloading', 'Optimum solution - parallel offloading', 'Location', 'northwest');
xlabel('U(packets)');
ylabel('Latency(ms)');
% 卸载失败率图
figure(2);
pointA_x = 200 : 200 : 2000;
pointA_y = sequFailure;
pointB_x = 200 : 200 : 2000;
pointB_y = paraFailure;
plot(pointA_x, pointA_y, '-*b', pointB_x, pointB_y, '-or');
axis([200, 2000, 0, 2 * 1e-4]);
set(gca, 'XTick', 200 : 200 : 2000);
set(gca, 'YTick', 0 : 0.2 * 1e-4 : 2 * 1e-4);
legend('Optimum solution - sequential offloading', 'Optimum solution - parallel offloading', 'Location', 'northwest');
xlabel('U(packets)');
ylabel('Task offloading failure probability');