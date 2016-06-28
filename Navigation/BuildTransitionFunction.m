% build the transition function
% T -- transition probability T{a}(s,s')
function [ T ] = BuildTransitionFunction()


global environment;
col = environment.col_number;
row = environment.row_number;
A = environment.A;
S = environment.S;

T = cell(1,A);
a = 1;
T{a} = zeros(S,S);
for i = 1:row
    for j = 1:col
        s = i + row*(j-1);
        if j == col
            T{a}(s,s) = 1.0; % reach the right wall
        elseif i == 1
            T{a}(s,s+row) = 0.9;
            T{a}(s,s+row+1) = 0.1;
        elseif i == row
            T{a}(s,s+row) = 0.9;
            T{a}(s,s+row-1) = 0.1;
        else 
            T{a}(s,s+row) = 0.8; % move to the right 
            T{a}(s,s+row+1) = 0.1;
            T{a}(s,s+row-1) = 0.1;
        end
    end
end
a = 2;
T{a} = zeros(S,S);
for i = 1:row
    for j = 1:col
        s = i + row*(j-1);
        if i == row
            T{a}(s,s) = 1.0; % reach the bottom
        elseif j == 1
            T{a}(s,s+1) = 0.9; 
            T{a}(s,s+1+row) = 0.1;
        elseif j == col
            T{a}(s,s+1) = 0.9;
            T{a}(s,s+1-row) = 0.1;
        else 
            T{a}(s,s+1) = 0.8; % move down
            T{a}(s,s+1+row) = 0.1;
            T{a}(s,s+1-row) = 0.1;
        end
    end
end
a = 3;
T{a} = zeros(S,S);
for i = 1:row
    for j = 1:col
        s = i + row*(j-1);
        if j == 1
            T{a}(s,s) = 1.0; % reach the left wall 
        elseif i == 1
            T{a}(s,s-row) = 0.9; 
            T{a}(s,s-row+1) = 0.1;
           
        elseif i == row
            T{a}(s,s-row) = 0.9;
            T{a}(s,s-row-1) = 0.1;  
        else
            T{a}(s,s-row) = 0.8; % move to the left
            T{a}(s,s-row+1) = 0.1;
            T{a}(s,s-row-1) = 0.1;
        end
    end
end
a = 4;
T{a} = zeros(S,S);
for i = 1:row
    for j = 1:col
        s = i + row*(j-1);
        if i == 1
            T{a}(s,s) = 1.0; % reach the ceiling 
        elseif j == 1
            T{a}(s,s-1) = 0.9; 
            T{a}(s,s-1+row) = 0.1;
        elseif j == col
            T{a}(s,s-1) = 0.9;
            T{a}(s,s-1-row) = 0.1;
        else
            T{a}(s,s-1) = 0.8; % move up
            T{a}(s,s-1+row) = 0.1;
            T{a}(s,s-1-row) = 0.1;
        end
    end
end
    
% for a = 1:A
%     T{a}(S,:) = 0;
%     T{a}(S,1) = 1.0; % move back to start point
% end
for a = 1:A
    T{a}(S,:) = 0;
    T{a}(S,S) = 1.0; % absorbing state
end

end