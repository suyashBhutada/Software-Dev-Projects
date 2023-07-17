% Suyash Bhutada
%2014ME20767    
%Assignment 1
%Problem 9
function [ V ] = pli1( X, Y, U )
%newton piecewise 
A=sortrows([X Y]);
%sorts only matrix X in ascending order along with corresponding values of
%Y in a 2 column matrix A
X=A(:,1);
Y=A(:,2);
%Storing first column of A into X which has the ascending values of X
%And storing the second column of A in Y which has the corresponding values
%of Y against the ascending X
slope=diff(Y)./diff(X);
%finding difference in consecutive values of Y and dividing the by the
%corresponding consecutive values of x equivalent to the slopes
[n,~]=size(U);
%Finding length of array U
j=0;
U1=zeros(n, 1);
V1=zeros(n, 1);
%initialising two arrays of size U
slope1=zeros(n,1);

for k=1:n
    while(X(j+1)<U(k))
        j=j+1;
    end
    U1(k)=X(j);
    V1(k)=Y(j);
    slope1(k)=slope(j);
    %This while loop is checking whether which u is coming in between which
    %twovalue of x. it stores the just small value of x before u in the
    %array u1 and also its corresponding value of y in array v1. Also slope
    %is stored between those two values.
    
    j = 0;
end
V=V1+slope1.*(U-U1);
%Here array ofV is filled by corresponding values in array u1 and v1
%using y-y1=m*(x-x1) we calculate V
return

