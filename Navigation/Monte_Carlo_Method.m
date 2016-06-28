function [s] = Monte_Carlo_Method(prob)
n = rand(1);
sum = 0;
for i = 1:length(prob)
    sum = sum + prob(i);
    if sum >= n
        s = i;
        break;
    end
end
    
end

