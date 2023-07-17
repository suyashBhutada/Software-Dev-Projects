% Suyash Bhutada
%2014ME20767    
%Assignment 1
%Problem 6
function sol = sor(A,b,guess)
%function that takes input A matrix, solution matrix and initial guess. 
w =1.5;
%assigns rate of convergence to 1.5. Optimal can be found for some special
%matrices
[n,n] = size (A);
%finds size of matrix A 
i = 1;
%initializes value of iteration number from 1
tol = 1e-10;
%defines tolerance value
L = tril (A,-1);
%assigns L to lower trialngular A
D = tril (A,0)-L;
%assigns D to upper triangular D
E = L + D;
%assigns E tothe sum of L and D
M = w*((1-w)*D + w*E);
%finds value of M matrix whose inverse is easy to find rather than A
if (max (abs(eig(eye(n) - pinv(M) * A)))>=1)
    fprintf('spectral radius should be less than 1')
    return;
    %checks condition for spectral radius of matrix A for which SOR method will work 
else
r = b - A * guess;
%defining residual matrix(value) by putting first value of x as initial guess
sol = guess + pinv(M) * r;
%finds first iterative solution by the formula 
l =(sol- guess);
%finds the difference betweeen iteration 1 and guess
maxiter = 1000;
%assigns maxiter value to big large number for maximum iterations
while (max(abs(l)) > tol && i<maxiter )
    %while condition to check if error becomes less than some fixed value
    %or if number of iterationsbecome larger than fixed value
    guess = sol;
    %chnaging guess to found solution
    r = b - A*guess;
    %again finding residue from changed value of guess
    sol = guess +pinv(M) * r;
    %finding solution again from the formula
    i = i+1;
    %increasing iterationnumber
     
end
end
if (max(abs(l))<tol) 
    fprintf('it is converging \n');
    fprintf('solution with SOR is \n');
    fprintf('%e',sol);
   %if difference becomes less than solution than we got the solution
else 
    sol = 'it isdiverging'
    %for iterations reaching maximum number it shows diverging result
end