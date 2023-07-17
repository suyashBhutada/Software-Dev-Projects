import numpy as np


n = 2
m = 2

c0 = [-4.0 , 0]
D = [[2.0, -2.0], [-2.0, 4.0]]
A1 = [[2, 1.0], [1, -4.0]]
b = [6.0, 0]
D = np.transpose(D)

def tran(A):
	return np.transpose(A)

A = tran(A1)
diagonal = [[0] * m] * m
for i in range(m):
    diagonal[i] = [0] * i + [1] + [0] * (m - i - 1)

F = np.concatenate(([b], np.concatenate((np.concatenate((diagonal, A1)), diagonal))))
F = np.transpose(F)

c3 = [0] + [1] * m + [0] * (m + n)


for i in range(m):
    if F[i][0] < 0:
        print()
        F[i] = list(np.array(F[i]) * -1)
        F[i][i + 1] = 1



for i in range(m):
    c3 = list(np.array(c3) - c3[i + 1] * np.array(F[i]))


while not all(x >= 0 for x in c3[1:]):
    j = np.argmin(c3[1:]) + 1

    for i in range(m):

        if F[i][j] > 0:
            min = i
            break

    for i in range(m):

        if F[i][j] > 0 and F[i][0] / F[i][j] < F[min][0] / F[min][j]:
            min = i


    F[min] = list(np.array(F[min]) / F[min][j])

    for k in range(1, m):
        F[(min + k) % m] = list(np.array(F[(min + k) % m]) - F[(min + k) % m][j] * np.array(F[min]))

    c3 = list(np.array(c3) - c3[j] * np.array(F[min]))


if c3[0] < 0:
    print('Solution is infeasable')
    exit()



T = [[0] * (2 + 3 * n + 2 * m)] * (m + n)



for i in range(m):
    T[i] = [0] + [b[i]] + list(A[i]) + [0] * (m + n) + [0] * i + [1] + [0] * (m + n - i - 1)


for i in range(n):


    T[i + m] = [-1] + [- c0[i]] + list(D[i]) + list(A1[i]) + [0] * i + [-1] + [0] * (n - i - 1) +  \
           [0] * (i + m) + [1] + [0] * (n - i - 1)



for i in range(m + n):
    if T[i][1] < 0:
        print('Solution is unbounded')
        exit()


c = [0] * 2 * (1 + m + n) + [-1] * n

sums = [0] * 2 * (1 + m + n) + [-1] * n

vars = [0] * (m + n)

for i in range(m + n):
    vars[i] = i + 2 + 2 * n + m

def calculate_sums():
    for i in range(2, 2 + 3 * n + 2 * m):
        s = 0

        for j in range(m + n):

            s += T[j][i] * T[j][0]
        sums[i] = s - c[i]


def conflict(x, y):
    if x >= 2 * (1 + m + n) or y >= 2 * (1 + m + n):
        return False
    elif abs(x - y) != n + m:
        return False
    else:
        return True

def check(x):
    for i in range(m + n):
        if conflict(x, vars[i]):
            return False
    return True


def entering_var():

    array = np.argsort(sums)

    for i in range(len(array)):
        if check(array[i]):
            return array[i]

def leaving_var(j):
    for i in range(m + n):
        if T[i][j] > 0:
            min = i
            break

    for i in range(m + n):
        if T[i][j] > 0 and T[i][1] / T[i][j] < T[min][1] / T[min][j]:
            min = i
    return min

def pivot(i, j):
    T[i] = list(np.array(T[i]) / T[i][j])
    for k in range(1, m + n):
        T[(i + k) % (m + n)] = list(np.array(T[(i + k) % (m + n)]) - T[(i + k) % (m + n)][j] * np.array(T[i]))

    vars[i] = j
    for k in range(m + n):
        if vars[k] < 2 * (1 + m + n):
            T[k][0] = 0
        else:
            T[k][0] = -1

calculate_sums()

count = 0

while not all(x >= 0 for x in sums[2:]):

    j = entering_var()

    i = leaving_var(j)

    pivot(i, j)

    calculate_sums()


for i in range(m + n):
    if T[i][1] < 0:
        print('Solution is Unbounded')
        exit()

x = [0] * (2 + 3 * n + 2 * m)
for i in range(m + n):
    x[vars[i]] = round(T[i][1], 2)

X = np.array(x[2:n + 2])

C = np.array(c0)
D = np.array(D)
S = X.dot(C) + 0.5 * (X.dot(D)).dot(X)
print('Optimal value: ' + str(S))
print('Optimal solution: ' + str(x[2:n + 2]))




