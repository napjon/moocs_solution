function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

%size(X)
a1 = [ones(m,1) X];
%size(a1)
z2 = a1 * Theta1';
a2 = [ones(m,1) sigmoid(z2)];
z3 = a2 * Theta2';
a3 = sigmoid(z3);

h_x = a3;

%j = ((-y) .*log(h_x)) - ((1 .- y).*log( 1 .- h_x));
K = ones(m,1);
j = ones(num_labels,1);
ytemp = zeros(num_labels,1);
for i=1:m
	ytemp = zeros(num_labels,1);
	ytemp(y(i)) = 1;
	j =  ( ((-ytemp) .* log(h_x(i,:)')) - ((1 .- ytemp).*log(1.-h_x(i,:)')) );
	%size(j)
	K(i) = sum(j);
	endfor;

J = sum(K)/m;
rgl_theta1 = Theta1;
rgl_theta2 = Theta2;

rgl_theta1(:,1) = 0;
rgl_theta2(:,1) = 0;
reg_term = (lambda/(2*m))*(sum(sum(rgl_theta1.^2)) + sum(sum(rgl_theta2.^2))); 
J +=  reg_term;

for i=1:m
%Step 1
	a1 = [1; X(i,:)'];
	z2 = Theta1 * a1;
	%size(z2)
	a2 = [1;sigmoid(z2)];
	z3 = Theta2 * a2;
	a3 = sigmoid(z3);
%Step 2y
	vector_y = zeros(num_labels,1);
	vector_y(y(i)) = 1;
	%size(a3)
	delta_3 = a3 - vector_y;
%Step 3
	delta_2 = Theta2(:,2:end)' * delta_3 .* sigmoidGradient(z2);
%Step 4
	%delta_2 = delta_2(2:end);
	%size(delta_2)
	%size(a1)
	Theta1_grad += delta_2*a1';
	Theta2_grad += delta_3*a2';
%Step 5, Cost Function
%	h_x = a3;
%	ytemp = zeros(num_labels,1);
%	ytemp(y(i)) = 1;
%	j =   ((-ytemp) .* log(h_x) - ((1 .- ytemp).*log(1.-h_x)) );
	%size(j)
%	K(i) = sum(j);
	endfor;

Theta1_grad = (Theta1_grad+lambda.*rgl_theta1)/m;
Theta2_grad = (Theta2_grad+lambda.*rgl_theta2)/m;






















% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
