% Suyash Bhutada
%2014ME20767    
%Assignment 1
%Problem 3
function [x] = gauss_elim ( A, b )
%This is the function to calculate solution to linear system via guassian
%elimination method taking inputs as coeficient matrix and solution to
%equations.
[nrow ncol] = size ( A );
%finding size of matrix A   
if (nrow ~= ncol)
    fprintf('Matrix is not square')
    return ;
%check if matrix is square or not
else
    if (det (A) == 0 )
        fprintf('Matrix is not invertible')
        return;
%check if matrix is invertible or not via checking the determinant
    else
for i = 1 : nrow - 1
    %starting for loop for i=1 continue till n-1
    for j = i+1 : nrow
        %changing values of each row by multiplying it with factor and
        %substracting in A matrix as weel as B matrix
	    m = -A(j,i) / A(i,i);
		A(j,i) = 0;
		A(j, i+1:nrow) = A(j, i+1:nrow) + m * A(i, i+1:nrow);
		b(j) = b(j) + m * b(i);
    end;
end;
    end;
end;
%finding value of last variable in given equations 
x(nrow) = b(nrow) / A(nrow, nrow);
for i = nrow - 1 : -1 : 1
    %back substitution of variables to calculate its values
    x(i) = ( b(i) - sum ( x(i+1:nrow) .* A(i, i+1:nrow) ) ) / A(i,i);
    
end;    