%   min f1(X) = x1.^2  +  x2.^2  + ... + x5.^2,     x1...x5  \in [-10,10]

popsize = 50;% poplulation size
mutation_rate = 0.05; % mutation rate
d = 5;

gen_index = 1; 
gen_max = 200;

% generate a population
for i = 1 : popsize
    pop(i).chrome = rand(1,d) * 20 - 10;
    pop(i).fitness = prob(pop(i).chrome);
end

while gen_index <= gen_max  % run GA (Genetic algorithm)
    gen_index = gen_index + 1;
    seq = randperm(popsize);    
    % crossover 
    for i = 1 : 2 : popsize
        pop(i).chrome;
        pop(i+1).chrome;
        
        decide = rand(1,d);
        child(i).chrome =  (decide > 0.5).* pop(seq(i)).chrome + (decide <= 0.5).* pop(seq(i+1)).chrome;
        child(i+1).chrome =  (decide > 0.5).* pop(seq(i+1)).chrome + (decide <= 0.5).* pop(seq(i)).chrome;
        
        child(i).fitness = prob(child(i).chrome);
        child(i+1).fitness = prob(child(i+1).chrome);
    end
    
   % mutation
   for i = 1 : popsize %父代变异
       decide = rand(1,d);
       pop(i).chrome = pop(i).chrome .* (decide > mutation_rate)  +  (rand(1,d)*20-10).*(decide < mutation_rate);
                                      % 随机数（0~1）> 变异率（0.01）
       pop(i).fitness = prob(pop(i).chrome);
   end
   
   for i = 1 : popsize %子代变异
       decide = rand(1,d);
       child(i).chrome = child(i).chrome .* (decide > mutation_rate)  +  (rand(1,d)*20-10).*(decide < mutation_rate);
                                      % 随机数（0~1）> 变异率（0.01）
       child(i).fitness = prob(child(i).chrome);
   end      
   
   fit = [];
   % selection
   for i = 1 : popsize
       fit = [fit pop(i).fitness];
   end  %收集父辈的fitness
   for i = 1 : popsize
       fit = [fit child(i).fitness];
   end  %收集子辈的fitness
   % fit = [ 8 6 9 | 4 0 7]
   % [~,index] = sort(fit);
   %得到index = 5     4     2     6     1     3
   
   [~,index] = sort(fit);
   for i = 1 : popsize
       if index(i) <= popsize
           newpop(i).chrome = pop(index(i)).chrome;
           newpop(i).fitness = pop(index(i)).fitness;
       else      
           newpop(i).chrome = child(index(i)- popsize).chrome;
           newpop(i).fitness = child(index(i)- popsize).fitness;
       end          
   end
   
   pop = newpop;  
   pop(1).fitness
end


function result = prob(x)
    result = sum(x.^2);
return
end



