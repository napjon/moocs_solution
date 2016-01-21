function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);


size(X)
size(y)
n = size(theta)

num_iters



g = zeros(size(X));
temp  = zeros(size(theta));



for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %

    %for i = 1:m


     %   n = ((X*theta) - y)*X(i);

     %   grad(i) = sum(n)/length(n); 

        %temp = theta - alpha*theta*computeCost(X,y,theta);

        %size(grad(i))
      %  temp = theta - alpha*grad(i);
        %theta = temp
    %endfor

    


    for i = 1:n
        g(:,i) = ((X*theta) - y).*X(:,i);


        total = sum(g(:,i))/length(g(:,i));
        temp(i) = theta(i) - alpha*total;
    endfor

    theta = temp;


    





    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta)


    kl = size(n)

end

end
