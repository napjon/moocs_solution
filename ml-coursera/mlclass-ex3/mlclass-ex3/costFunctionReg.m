function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta




h_x = sigmoid(X * theta);

j = ((-y) .*log(h_x)) - ((1 .- y).*log( 1 .- h_x));
rgl_theta =theta;
rgl_theta(1) = 0;
rgl = (lambda/(2*m)) * sum(rgl_theta.^2)            

J = sum(j)/length(j)+rgl;


for i = 1:size(theta)
	grad_vec = (h_x - y).*X(:,i);
	grad(i) = sum(grad_vec)/length(grad_vec);
endfor

for i = 1:size(theta)
	if (i>1)
		grad(i) += (lambda/m * theta(i));
	endif
endfor




% =============================================================

end
