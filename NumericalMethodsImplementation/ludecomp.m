% Suyash Bhutada
%2014ME20767    
%Assignment 1
%Problem 4
function [L,U,P] = ludecomp (A)
%This is function that finds lower triangular upper triangular and
%permutation matrix for the matrix
[nrow, ncol] = size ( A );
%finding size of matrix A
P = eye(nrow);
%initializing permutation matrix by identity matrix of n*n
L = zeros(nrow,nrow);
%initializing lower triangular matrix by zero matrix of n*n
if (nrow ~= ncol)
    fprintf('Matrix is not square')
    return ;
    %checking whether number of row is equal to number of column
else
    if (det (A) == 0 )
        fprintf('Matrix is not invertible')
        return;
        %checking whether matrix is invertibe
    else
        
        for i = 1 : nrow - 1
            %initializing value of row from 1 to n-1.
            [m,k] = max(A(i:nrow,i));
            %to pivot this step finds maximum value m in given column A and also find its row number k
            %it then checks whether it is on top or not 
            k = k+i-1;
            %this then changes value of k to (k+i-1) for all the pivots   
            if (k ~= i)
                C = A(i,1:nrow);
                A(i,1:nrow) = A(k,1:nrow);
                A(k,1:nrow) = C;
                %this interchanges the row in A matrix during pivot 
                D = P(i,1:nrow);
                 P(i,1:nrow) = P(k,1:nrow);
                P(k,1:nrow) = D;
                %this interchanges the row in permutation matrix 
                
              
                E = L(i,1:nrow);
                 L(i,1:nrow) = L(k,1:nrow);
                L(k,1:nrow) = E;
                %this interchanges the row in L matrix
                
            end
            L(i,i) = 1;
            %assigns the diagonal matrix entries = 1
        for j = i+1 : nrow
            %initializes value of column from i+1 ton
	    m = -A(j,i) / A(i,i);
        %finds the factor to divide
		A(j, i:nrow) = A(j, i:nrow) + m * A(i, i:nrow);
        %changes each value in A matrix
        L(j , i) = -m;
        %changes values in L matrix equal to ratio
        L(i, j:ncol) = 0;
        %assigns value of upper triangular values equal to 0
        end;
       
        end;
    end;
    L(nrow,ncol) = 1;
    U(1:nrow,1:ncol) = A(1:nrow,1:ncol);
    fprintf('Upper triangular is \n');
    disp (U);
     fprintf('permutation matrix is \n');
    disp (P);
     fprintf('lower triangular is \n');
     %prints all the matrices L U and P
end;

        