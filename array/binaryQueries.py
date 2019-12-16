"""
INPUT
5 2
1 0 1 1 0
1 2
0 1 4

OUTPUT 
ODD
"""

def binaryQueries():
    n, q = map(int, input().split())
    l = input().split()
    for i in range(0,q):
        k = input().split()
        print(k)
        if k[0] == '0':
            if l[int(k[2])-1] == '1':
                print("ODD")
            else:
                print("EVEN")
        if k[1] == '1':
            if l[int(k[1]) - 1] == '0':
                l[int(k[1]) - 1] = '1'
            else:
                '0'

if __name__ == '__main__':
    binaryQueries()