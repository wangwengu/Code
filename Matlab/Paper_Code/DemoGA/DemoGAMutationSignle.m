function mutationResult = DemoGAMutationSignle(son, mu)
    index = randi(size(son, 2));
    if rand() < mu % 变异
        son(1, index) = xor(son(1, index), 1);
    end
    mutationResult = son;
end