function [ V ] = NewtonDD( X, Y, U )
%NEWTONDD Summary of this function goes here
%   Detailed explanation goes here
n=length(X);
%gives the length of X ie number of points given
matrix=zeros(n,n);
%initializing a matrix with all zeros
%this will be used to find the values of the constants in the divided
%difference method LO
%the resulted matrix will be a lower triangular matrix with every right
%element as the difference of the two left consecutive elements
matrix(:,1)=Y;
%according to the protocol of the method the first column would be the
%values of the function ie the values of the column matrix Y
for a=2:n
    %a implying the column numbers of matrix which should span from 2 to n
  for b=a:n
      %b implies the rows of the column a from a to n forming a lower
      %triangular matrix
      matrix(b,a) = (matrix(b,a-1)-matrix(b-1,a-1))/(X(b)-X(b-a+1));
      %taking every two consecutive elements of column a and taking
      %theirdifference divided by the corresponding difference in X matrix
      %storing the result in next column and the same row as the bottom
      %element among the two
  end
end
E=diag(matrix);
%extracting diagonal elements from matrix and storing it in E as these
%elements would yield the constants of the divided difference method

for j=1:length(U)
%calculation of every value of V corresponding every value of U
%j here spans all the elements in column matrix U
V(j)=E(n)*(U(j)-X(n-1))+E(n-1);
%we begin with the last term from the following term
%pn(x) ?= c0+c1(x?x0)+c2(x?x0)(x?x1)+...+cn(x?x0)(x?x1)...(x?xn?1)
%initialising the last term with last coeff from E multiplies by (x?xn?1)
%plus coeff of the last second term from E
%V(j) gives the value of interpolated function corresponding to jth value
%of x in matrix U
    for i=n-2:-1:1
    V(j)=V(j)*(U(j)-X(i))+E(i);
    %multiplying V in every loop with x-xr hence we end up with a function
    %like pn with every loop
    %the resulted column matrix V results in the value of function at point
    %provided in U
end
end
return

