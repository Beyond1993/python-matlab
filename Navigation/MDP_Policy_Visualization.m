function MDP_Policy_Visualization(P)
global environment;
row_number = environment.row_number;
col_number = environment.col_number;

for i = 1:row_number
    for j = 1:col_number
        s = i+(j-1)*(row_number);
        if P(s) == 1 
            fprintf('-> ');
        end
        if P(s) == 2 
            fprintf('|_ ');
        end
        if P(s) == 3 
            fprintf('<- ');
        end
        if P(s) == 4 
            fprintf('^| ');
        end
    end
    fprintf('\n');
end