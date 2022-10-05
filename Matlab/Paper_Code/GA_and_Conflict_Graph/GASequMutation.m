function mutationResult = GASequMutation(son, mu, taskNum, bitNum)
    % 单点变异
    for i = 1 : taskNum
        index = randi([(i - 1) * bitNum + 1, i * bitNum]);
        if rand() < mu
            son(1, index) = xor(son(1, index), 1);
        end
    end
    mutationResult = son;
end