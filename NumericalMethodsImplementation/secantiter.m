% Suyash Bhutada
%2014ME20767    
%Assignment 1
%Problem 2
function [sol] = secantiter (func, guess0,guess1)
%This is the function to calculate solution through Secant iteration method
%taking inputs as function, first guess and second guess which gives solution to function. 
tol = 1e-10;
%Tolerance defined to check for difference between two consecutive values.
maxiter = 1000;
%Large number defined to check for convergence of the method whether it
%converges or not.
n = 0;
%initialising number of iterations.
x0 = guess0;
%asigning x0 to value of first guess given as input.   
x1 = guess1;
%asigning x1 to value of second guess given as input.   
l = func(x1) * (x1-x0)/(func(x1)-func(x0));
%Doing first iteration using first values of input guesses. 
while (abs(l)>tol && n<maxiter),
    x0 = x1;
    x1 = x1-l;
    l = func(x1) * (x1-x0)/(func(x1)-func(x0));
    n = n+1;
    fprintf('Iteration number %d\n',n)
    fprintf('Variable %d\n',x1)
    fprintf('\n')
end
% While loop that goes on till both the conditions are verified i.e. difference between consecutive numbers 
%greater than tolerance or number of iterations smaller than a fixed large number.
if (l<tol) 
    sol = x1
    fprintf('it is converging \n')
    fprintf('solution with secant method is \n')
    fprintf('%e',sol)
else 
    fprintf('it is diverging')
%if condition to say after function comes out of while loop i.e. if
%difference is small we got the solution else if iterations greater than fixed number
%than divergence of method.

end 