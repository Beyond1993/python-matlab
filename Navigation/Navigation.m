% Navigation Problem
%--------------------------------------------------------------------------
% Initialize environment
%--------------------------------------------------------------------------
%clear;
global environment;
col_number = 5;
row_number = 5;

A = 4;                      % Action: 4 directions                    
S = col_number*row_number;  % State: 5 X 5  = 25 states

environment.S = S;    
environment.A = A;    
environment.row_number = row_number;
environment.col_number = col_number;
[grid, levels, k0] = BuildGridWorld();
T                  = BuildTransitionFunction();
%--------------------------------------------------------------------------
% Standard approach: Policy Iteration
%--------------------------------------------------------------------------

[R_std, u] = BuildRewardFunction(grid, T, 'null', 'null', levels, k0);
sigma = 0.01; % should be carefully set, otherwise cannot converge
gamma = 0.95;
[V, P] = MDP_Policy_Iteration(S, A, R_std, T, gamma, sigma);

%Visualize the optimal policy
fprintf('Std model solution:\n');
MDP_Policy_Visualization(P);
%normalization for V
V_norm = (V-min(V))/range(V); %range(V) the different bewteen max and min
Value_function_std = reshape(V_norm,row_number,col_number);

save('V.mat','V');
save('V_norm.mat','V_norm');
save('Value_function_std.mat','Value_function_std');

% get Trajectories
tn = 100;
Traj = cell(tn,1);

for i = 1:tn
    Traj{i} = getTraj(grid, T, P, 1, u);
end

save('randTraj100.mat','Traj');






