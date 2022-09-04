function mutationResult = GAParaMutation(son, mu)
    % 单点变异
    for i = 1 : 4
        index = randi([(i - 1) * 2 + 1, i * 2]);
        if rand() < mu
            son(1, index) = xor(son(1, index), 1);
        end
    end
    mutationResult = son;
end