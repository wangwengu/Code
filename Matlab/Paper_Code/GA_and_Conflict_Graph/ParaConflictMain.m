% 引入常量
[Np, ~, ~, ~, x, T, S] = Constant();
[n, m] = deal(size(S, 1), size(T, 1));
% 引入并行冲突图
graph = ParaConflictGraph(n, m);
% 计算Wp
Wp = ParaConflictCalculWp(T, S, Np);
fprintf("Wp:\n");
for i = 1 : n
    for j = 1 : m
        fprintf("%.8f ", Wp(i, j));
    end
    fprintf("\n");
end

%% 初始化
% 计算Delta
Delta = zeros(1, m);
for i = 1 : m
    Delta(1, i) = Wp(1, i);
end
for i = 1 : m
    fprintf("%.8f\n", Delta(1, i));
end
% 计算K
K = zeros(1, m);
for i = 1 : m
    for j = 1 : m
        K(1, i) = K(1, i) + x(i, j) * Delta(1, j);
    end
end
for i = 1 : m
    fprintf("%.8f\n", K(1, i));
end
% % 混合排序
mixed = Delta + K;
fprintf("Delta:\n");
fprintf("%.8f\n", Delta);
fprintf("K:\n");
fprintf("%.8f\n", K);
fprintf("mixed:\n");
fprintf("%.8f\n", mixed);
[~, index] = sort(mixed, "descend");
fprintf("index:\n");
fprintf("%d\n", index);
%% 主程序
Result = zeros(m, 2);
for i = 1 : m
    v = 0x3f3f3f3f;
    idx = 0;
    for j = 1 : n
        if v > Wp(j, index(i))
            vertex_1 = (j - 1) * m + index(i);
%             fprintf("vertex_1 = %d\n", vertex_1);
            flag = true;
            for k = 1 : i - 1
                vertex_2 = (Result(k, 1) - 1) * m + Result(k, 2);
%                 fprintf("vertex_2 = %d\n", vertex_2);
                if graph(vertex_1, vertex_2) == 1
                    flag = false;
                    break;
                end
            end
            if flag == true
                v = Wp(j, index(i));
                idx = j;
            end
        end
    end
%     fprintf("v(%d, %d)\n", idx, index(i));
    Result(i, :) = [idx, index(i)];
end
disp(Result);



