%% 生成并行卸载图(每行每列只能有一个皇后)
function ParaGraph = generateParaGraph()
    ParaGraph = [
        [
             1 0 0 0;
             0 1 0 0;
             0 0 1 0;
             0 0 0 1;
        ];
        [
             1 0 0 0;
             0 1 0 0;
             0 0 0 1;
             0 0 1 0;
        ];
        [
             1 0 0 0;
             0 0 1 0;
             0 1 0 0;
             0 0 0 1;
        ];
        [
             1 0 0 0;
             0 0 1 0;
             0 0 0 1;
             0 1 0 0;
        ];
        [
             1 0 0 0;
             0 0 0 1;
             0 1 0 0;
             0 0 1 0;
        ];
        [
             1 0 0 0;
             0 0 0 1;
             0 0 1 0;
             0 1 0 0;
        ];
        [
             0 1 0 0;
             1 0 0 0;
             0 0 1 0;
             0 0 0 1;
        ];
        [
             0 1 0 0;
             1 0 0 0;
             0 0 0 1;
             0 0 1 0;
        ];
        [
             0 1 0 0;
             0 0 1 0;
             1 0 0 0;
             0 0 0 1;
        ];
        [
             0 1 0 0;
             0 0 1 0;
             0 0 0 1;
             1 0 0 0;
        ];
        [
             0 1 0 0;
             0 0 0 1;
             1 0 0 0;
             0 0 1 0;
        ];
        [
             0 1 0 0;
             0 0 0 1;
             0 0 1 0;
             1 0 0 0;
        ];
        [
             0 0 1 0;
             1 0 0 0;
             0 1 0 0;
             0 0 0 1;
        ];
        [
             0 0 1 0;
             1 0 0 0;
             0 0 0 1;
             0 1 0 0;
        ];
        [
             0 0 1 0;
             0 1 0 0;
             1 0 0 0;
             0 0 0 1;
        ];
        [
             0 0 1 0;
             0 1 0 0;
             0 0 0 1;
             1 0 0 0;
        ];
        [
             0 0 1 0;
             0 0 0 1;
             1 0 0 0;
             0 1 0 0;
        ];
        [
             0 0 1 0;
             0 0 0 1;
             0 1 0 0;
             1 0 0 0;
        ];
        [
             0 0 0 1;
             1 0 0 0;
             0 1 0 0;
             0 0 1 0;
        ];
        [
             0 0 0 1;
             1 0 0 0;
             0 0 1 0;
             0 1 0 0;
        ];
        [
             0 0 0 1;
             0 1 0 0;
             1 0 0 0;
             0 0 1 0;
        ];
        [
             0 0 0 1;
             0 1 0 0;
             0 0 1 0;
             1 0 0 0;
        ];
        [
             0 0 0 1;
             0 0 1 0;
             1 0 0 0;
             0 1 0 0;
        ];
        [
             0 0 0 1;
             0 0 1 0;
             0 1 0 0;
             1 0 0 0;
        ];
    ];
end