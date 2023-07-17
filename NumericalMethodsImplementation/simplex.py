from __future__ import print_function 
import numpy as np  
from fractions import Fraction 

  
# inputs 
# only consider maximization problems 
eps = 0.0001
l_ne = -1000 
# A will contain the coefficients of the constraints 
#A = np.array([[1, 1, 1, 0], [2, 1, 0, 1]])
#A = np.array([[1,1,1,0,0], [1,1,0,-1,1]]) 
##actual 10, positive slack 10, neg slack 10, artificial 10
A = np.array([
    [1,0,0,0,0,0,0,0,0,0,    1,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0],
    [eps,1,0,0,0,0,0,0,0,0,  0,1,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0],
    [0,eps,1,0,0,0,0,0,0,0,  0,0,1,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0],
    [0,0,eps,1,0,0,0,0,0,0,  0,0,0,1,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0],
    [0,0,0,eps,1,0,0,0,0,0,  0,0,0,0,1,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,eps,1,0,0,0,0,  0,0,0,0,0,1,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,eps,1,0,0,0,  0,0,0,0,0,0,1,0,0,0,    0,0,0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,eps,1,0,0,  0,0,0,0,0,0,0,1,0,0,    0,0,0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,eps,1,0,  0,0,0,0,0,0,0,0,1,0,    0,0,0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,eps,1,  0,0,0,0,0,0,0,0,0,1,    0,0,0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0],


    [1,0,0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,    -1,0,0,0,0,0,0,0,0,0,     1,0,0,0,0,0,0,0,0,0],
    [-1*eps,1,0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,0,0,    0,-1,0,0,0,0,0,0,0,0,     0,1,0,0,0,0,0,0,0,0],
    [0,-1*eps,1,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,0,0,    0,0,-1,0,0,0,0,0,0,0,     0,0,1,0,0,0,0,0,0,0],
    [0,0,-1*eps,1,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,0,0,    0,0,0,-1,0,0,0,0,0,0,     0,0,0,1,0,0,0,0,0,0],
    [0,0,0,-1*eps,1,0,0,0,0,0,  0,0,0,0,0,0,0,0,0,0,    0,0,0,0,-1,0,0,0,0,0,     0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,-1*eps,1,0,0,0,0,  0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,-1,0,0,0,0,     0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,-1*eps,1,0,0,0,  0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,-1,0,0,0,     0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,-1*eps,1,0,0,  0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,-1,0,0,     0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,-1*eps,1,0,  0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,-1,0,     0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,-1*eps,1,  0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,-1,     0,0,0,0,0,0,0,0,0,1]
    ])
# b will contain the amount of resources  
b = np.array([1,1,1,1,1,1,1,1,1,1,   eps,0,0,0,0,0,0,0,0,0])            

# c will contain coefficients of objective function Z       
c = np.array([0,0,0,0,0,0,0,0,0,1,   0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   l_ne,l_ne,l_ne,l_ne,l_ne,l_ne,l_ne,l_ne,l_ne,l_ne])
#c = np.array([1, 1, 0, 0,-1000])              
  
# B will contain the basic variables that make identity matrix  
B = np.array([[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[30],[31],[32],[33],[34],[35],[36],[37],[38],[39]])
#B = np.array([[2], [4]])           

# cb contains their corresponding coefficients in Z    
cb = np.array([c[10],c[11],c[12],c[13],c[14],c[15],c[16],c[17],c[18],c[19],c[30],c[31],c[32],c[33],c[34],c[35],c[36],c[37],c[38],c[39]])
#cb = np.array([c[2],c[4]])
cb = np.vstack((cb))   

xb = np.transpose([b])                  
# combine matrices B and cb 
table = np.hstack((B, cb))              
table = np.hstack((table, xb))          
table = np.hstack((table, A))          
table = np.array(table, dtype ='float')  
# inputs end 
  

MIN = 0
  
print("Iteration:  0") 
print("B \tCB \tXB ")
for row in table: 
    for el in row: 
                # limit the denominator under 100 
        print(Fraction(str(el)).limit_denominator(100), end ='\t')  
    print() 
print()  
  
# when optimality reached it will be made 1 
reached = 0     
itr = 1
unbounded = 0
alternate = 0
  
while reached == 0: 
  
    print("Iteration: ", end =' ') 
    print(itr) 
    print("B \tCB \tXB ")
    for row in table: 
        for el in row: 
            print(Fraction(str(el)).limit_denominator(100), end ='\t') 
        print() 
  
    # calculate Relative profits-> cj - zj for non-basics 
    i = 0
    rel_prof = [] 
    while i<len(A[0]): 
        rel_prof.append(c[i] - np.sum(table[:, 1]*table[:, 3 + i])) 
        i = i + 1
  
    print("rel profit: ", end =" ") 
    for profit in rel_prof: 
        print(Fraction(str(profit)).limit_denominator(100), end =", ") 
    print() 
    i = 0
      
    b_var = table[:, 0] 
 
    flag = 0
    for profit in rel_prof: 
        if profit>0: 
            flag = 1
            break
        # if all relative profits <= 0 
    if flag == 0: 
        print("All profits are <= 0, optimality reached") 
        reached = 1
        break
  
    # kth var will enter the basis 
    k = rel_prof.index(max(rel_prof)) 
    min = 999999
    i = 0; 
    r = -1
    # min ratio test (only positive values) 
    while i<len(table): 
        if (table[:, 2][i]>0 and table[:, 3 + k][i]>0):  
            val = table[:, 2][i]/table[:, 3 + k][i] 
            if val<min: 
                min = val 
                r = i     # leaving variable 
        i+= 1
  
        # if no min ratio test was performed 
    if r ==-1: 
        unbounded = 1
        print("Case of Unbounded") 
        break
  
    print("pivot element index:", end =' ') 
    print(np.array([r, 3 + k])) 
  
    pivot = table[r][3 + k] 
    print("pivot element: ", end =" ") 
    print(Fraction(pivot).limit_denominator(100)) 
          
        # perform row operations 
    # divide the pivot row with the pivot element 
    table[r, 2:len(table[0])] = table[ r, 2:len(table[0])] / pivot 
              
    # do row operation on other rows 
    i = 0
    while i<len(table): 
        if i != r: 
            table[i, 2:len(table[0])] = table[i, 2:len(table[0])] - table[i][3 + k] * table[r, 2:len(table[0])] 
        i += 1
  
      
    # assign the new basic variable 
    table[r][0] = k 
    table[r][1] = c[r] 
      
    print() 
    print() 
    itr+= 1
      
  
print() 
  
print("***************************************************************") 
if unbounded == 1: 
    print("UNBOUNDED LPP") 
    exit() 
  
print("optimal table:") 
print("B \tCB \tXB ") 
for row in table: 
    for el in row: 
        print(Fraction(str(el)).limit_denominator(100), end ='\t') 
    print() 
print() 
print("value of Z at optimality: ", end =" ") 
  
basis = [] 
i = 0
sum = 0
while i<len(table): 
    sum += c[int(table[i][0])]*table[i][2] 
    temp = "x"+str(int(table[i][0])+1) 
    basis.append(temp) 
    i+= 1
# if MIN problem make z negative 
if MIN == 1: 
    print(-Fraction(str(sum)).limit_denominator(100)) 
else: 
    print(Fraction(str(sum)).limit_denominator(100)) 
print("Final Basis: ", end =" ") 
print(basis) 
  
print("Simplex Finished...") 
print() 