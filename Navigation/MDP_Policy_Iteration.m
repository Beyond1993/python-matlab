function [V, P, iter, iter1] = MDP_Policy_Iteration(S, A,  R, T, gamma, sigma)
%--------------------------------------------------------------------------
% S -- number of states
% A -- number of actions
% P -- Policy P(s) = one of the action (deterministic)
% R -- reward function R{a}(s,s')
% T -- transition probability T{a}(s,s')
% gamma -- discount rate
% sigma -- stopping criterion
% V -- value function V(s)
%--------------------------------------------------------------------------

% Policy initialization
P = ones(S,1);

policy_stable = 0; %false 
iter = 0;

% Policy Evaluation
%while iter <500
while policy_stable == 0
    iter = iter + 1;
%     if iter > 300
%         break;
%     end
   
    %Initialize the Value fuction
    V = zeros(S,1);

    
    deta = sigma;
    iter1 = 0;
    
    while deta >= sigma      
        deta = 0;
        for s = 1:S
            v = V(s);
            debug = T{P(s)}(s,:); 
            V(s) = T{P(s)}(s,:) * (R{P(s)}(s,:)' + gamma*V);
            deta = max(deta, abs(v-V(s)));         
        end
        iter1 = iter1 + 1;
%         if iter1 > 300
%             break;
%         end
    end

    % Policy Improvement
    % warning: only doesn't change in two episodes may still not stable
    % should be unchangeable for several episodes
    policy_stable = 1; %true
    for s = 1:S
        b = P(s);
        maxV = T{1}(s,:)*(R{1}(s,:)'+gamma*V);
        maxA = 1;
        for a = 2:A
            if T{a}(s,:)*(R{a}(s,:)'+gamma*V) > maxV
                maxV = T{a}(s,:)*(R{a}(s,:)'+gamma*V);
                maxA = a;
            end
            
            
            
        end
        P(s) = maxA;
        if P(s)~= b
            policy_stable = 0; %false  
        end
    end
    
end

end





