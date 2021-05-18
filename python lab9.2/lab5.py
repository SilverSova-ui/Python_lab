def SwapColumns(A, i, j):
    for q in range(len(A)):
        A[q][i], A[q][j] = A[q][j], A[q][i]
 
n, m = [int(i) for i in input('количество столбцов и строк - ').split()]
A = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input('замена столбцов -').split()]
SwapColumns(A, i, j)
for row in A:
    print(' '.join([str(A) for A in row]))