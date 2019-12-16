"""
Monk and Welcome Problem
C[i] = A[i] + B[i]

5
1 2 3 4 5
4 5 3 2 10

5 7 6 6 15
"""

def monkWelcome():
    n = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(0, len(a)):
        c.append(a[i] + b[i])
    print(*c)
    


if __name__ == '__main__':
    monkWelcome()