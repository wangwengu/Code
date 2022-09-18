function mutationResult = DemoGAMutationMulti(son, mu)
    index = randi(size(son, 2));
    if rand() < mu
        son(1, index) = xor(son(1, index), 1);
    end
    mutationResult = son;
end