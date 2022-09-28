pointA_x = 200 : 200 : 2000;
pointA_y = [
    26.375000, 29.765808, 33.361717, 36.326263, 38.105354, ...
    41.799899, 46.063889, 51.517980, 56.808434, 62.139798
];
plot(pointA_x, pointA_y, '-*b');
axis([200, 2000, 0, 110]);
set(gca, 'XTick', 200 : 200 : 2000);
set(gca, 'YTick', 0 : 10 : 110);
legend('Genetic algorithm - parallel offloading', 'Location', 'NorthWest');
xlabel('U(packets)');
ylabel('Latency(ms)');