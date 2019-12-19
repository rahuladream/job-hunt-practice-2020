"""
find out the number of inversion in the matrix M.
defined as the number of unordered pairs of cells
{(i,j), (p,q)} such that M[i][j] & i <=p & j<=q

2 => no of testcase
3 => 3 * 3 matrix input
1 2 3
4 5 6
7 8 9
2 => 2 * 2 matrix input
4 3 
1 4

"""

t = input()
for t in range(int(t)):
    n = int(input())
    no_of_rc = []
    ct = 0
    for i in range(0,n):
        no_of_rc.append([int(j) for j in input().split()])
    for i in range(0,n):
        for k in range(0,n):
            for in range(0,n):
                if(i<=k and j<=l and a[i][j] > a[k][l]):
                    ct=ct+1

