% Suyash Bhutada
%2014ME20767    
%Assignment 1
%Problem 5
function L = cholesky(A)
%it takes the input a matrix and finds the lower trialgular matrix of LLt
[n n] = size (A);
%finds size of matrix A
L= zeros(n,n);
%initializes L by zero matrix of n*n
C=eig(A);
%finds eigen value to check matrix is SPD or not.
if (min(C)>0)
    %goes ahead if matrix is SPD 
for(i = 1:n-1)
    L(i,i) = sqrt (A(1,1));
    %finds value of diagonal element of L by square root of A(1,1) value of A matrix
    L(i+1:n , i) = A(2:n-i+1, 1) / L(i,i);
    %find value of other values in L martix for the same column.
    A = A(2:n-i+1,2:n-i+1)- (L(i+1:n,1)* (L(i+1:n,1))');
    %Changes the A matrix by n*n dimension to n-1*n-1 dimension 
end;
L(n,n) = sqrt(A(1,1)+L(n,:)*L(n,:)');
%finds value of last element of L matrix
else 
    %fprintf('it is not SPD haha')
    L='It is not SPD haha';
    return
    %comes out of function if matrix is not SPD
end
    fprintf('L is \n');
    %prints L matrix 
end
   
