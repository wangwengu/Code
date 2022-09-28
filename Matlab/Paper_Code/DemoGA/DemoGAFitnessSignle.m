function fitnessResult = DemoGAFitness(translateResult)
    fitnessResult = zeros(1, size(translateResult, 2));
    for i = 1 : size(translateResult, 2)
        fitnessResult(1, i) = translateResult(1, i) ^ 2;
    end
end