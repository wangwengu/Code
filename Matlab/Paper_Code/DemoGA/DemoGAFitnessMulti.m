function Fitness = DemoGAFitnessMulti(translateResult)
    Fitness = zeros(size(translateResult, 1), 1);
    for i = 1 : size(translateResult, 1)
        Fitness(i, 1) = translateResult(i, 1) + translateResult(i, 2);
    end
end