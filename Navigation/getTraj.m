% get trajectories
function [ traj ] = getTraj(grid, T, P, s0, u)

global environment;
row = environment.row_number;
s = s0;
len = 25;
traj = zeros(len,4);
for i = 1:len
    % [s, a, r, s']
    traj(i,1) = s;  
    %traj(i,2) = P(s);
    action = randi([1,4],1,1)
    traj(i,2) = action;
    
    %calculate row and col from state
    r = mod(s,row);
    if r == 0;
        r = row;
    end
    c = ceil(s/row);
    
    traj(i,3) = u(grid(r,c));
    
    
    s = Monte_Carlo_Method(T{action}(s,:));%P is policy, T{action} create a new state
    traj(i,4) = s;
end


end