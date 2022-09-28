% 点A的横坐标, 即A(x, y)中的x值
pointA_x = 200 : 200 : 1000;
% 点A的纵坐标, 即A(x, y)中的y值
pointA_y = [203.024, 113.857, 256.259, 244.888, 293.376];
% 点B的横坐标, 即B(x, y)中的x值
pointB_x= 200 : 200 : 1000;
% 点B的纵坐标, 即B(x, y)中的y值
pointB_y = [
    334.4, 143.2, ... % 一行写不下, 分多行写, 使用三个点(...)
    297.4, 487.2, 596.2
];
% 画折线图, 点, 颜色, 标记
plot(pointA_x, pointA_y, '-*b', pointB_x, pointB_y, '-or');
% 确定坐标系x轴和y轴的范围
axis([200, 1000, 0, 700]);
% 设置x轴的起始值, 间隔值, 终止值
set(gca, 'XTick', 200 : 200 : 1000);
% 设置y轴的起始值, 间隔值, 终止值
set(gca, 'YTick', 0 : 100 : 700);
% 图标注, 选定位置即可
legend('Depth', 'Time', 'Location', 'NorthWest');
% x轴描述
xlabel('深度');
% y轴描述
ylabel('时间');