% Suyash Bhutada
%2014ME20767    
%Assignment 1
%Problem 1

function [sol] = newtoniter (func ,deri,guess)
%This is the function to calculate solution through newton iteration method taking inputs as function, derivative
%and guess and which gives solution to function.  
err = 1e-10;
%Error defined to check for difference between two consecutive iterations.
maxiter = 1000;
%Large number defined to check for convergence of the method whether it
%converges or not.
n = 0;
%initialising number of iterations.
x = guess;
%asigning x to value of guess given as input.   
l = func(x)/deri(x);
%Doing first iteration using first value of x. 
array(1) = func(x);
%Storing function values in an array to plot the graph.
while (abs(l)>err && n<maxiter),
    x = x-l;
    l = func(x)/deri(x);
    n = n+1;
    array(n+1) = func(x);
    fprintf('Iteration number %d\n',n)
    fprintf('Variable %d\n',x)
    fprintf('\n')
    
end
% While loop that goes on till both the conditions are verified i.e. difference greater than error or number 
%of iterations smaller than a fixed large number.   
if (l<err) 
    sol = x
    fprintf('solution with newton method is \n')
    fprintf('%e',sol)
else 
    fprintf('it is diverging')
end 
%if condition to say after function comes out of while loop i.e. if error
%is small we got the solution else if iterations greater than fixed number
%than divergence of number.
plot(array)
%plotting the function values that was being stored in the array
end


    