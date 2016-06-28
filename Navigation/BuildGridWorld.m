% buil the grid world
% global enviroment: row_number, col_number, S, A

function [grid, levels, k0] = BuildGridWorld()

global environment;

row_number = environment.row_number;
col_number = environment.col_number;

levels = 5; 
k0 = 3;                      % k0: neutral level k<k0(P) k>k0(N)

%randomized environment
% grid = ceil(rand(row_number,col_number)*(levels-1))+1; % rand 2~levels
% grid(row_number,col_number) = 1; % goal level = 1;
grid = [3,3,3,3,3;
        5,4,5,3,4;
        4,2,5,3,4;
        2,2,4,3,4;
        2,2,4,2,1];



end
     
 
