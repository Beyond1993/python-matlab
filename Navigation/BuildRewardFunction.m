function [ R, u, N ] = BuildRewardFunction(grid, T, P, traj, levels, k0)
% reward function R{a}(s,s')

global environment;
row_number = environment.row_number;
col_number = environment.col_number;
A = environment.A;
S = environment.S;

%% Standard Model[...3,2,1,0,-1,-2,-3...]
if strcmp(P,'null')&&strcmp(traj,'null')
    % equally spaced initialized
%     u = 1:levels;
%     u = (u-k0)*(-1);
%     u = u(:);
    % ground truth
      u = [5;1;0;-3;-4];
     
     R = cell(1,A);
    for a = 1:A
        R{a} = zeros(S,S);
        for r = 1:row_number
            for c = 1:col_number
                s = (c-1)*row_number + r;
                R{a}(:,s) = u(grid(r,c));
            end
        end
    end
    

end


    
end

