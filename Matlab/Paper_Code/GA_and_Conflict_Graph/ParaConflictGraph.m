function graph = ParaConflictGraph(n, m)
    points = n * m;
    Task = zeros(1, points);
    Server = zeros(1, points);
    graph = zeros(points, points);
    for i = 1 : n
        for j = 1 : m
            Server(1, (i - 1) * m + j) = i;
            Task(1, (i - 1) * m + j) = j;
        end
    end
    %% 建图
    % 横轴
    for i = 1 : n
        for j = 1 : m
            x = (i - 1) * m + j;
            for k = 1 : m - j
                y = x + k;
                graph(x, y) = 1;
                graph(y, x) = 1;
            end
        end
    end
    % 纵轴
    for j = 1 : m
        for i = 1 : n
            x = j + (i - 1) * n;
            for k = 1 : n - i
                y = x + k * m;
                graph(x, y) = 1;
                graph(y, x) = 1;
            end
        end
    end
%     for i = 1 : points
%         for j = 1 : points
%             if graph(i, j) == 1
%                 fprintf("(%d, %d) ", i, j);
%             end
%         end
%         fprintf("\n");
%     end
end