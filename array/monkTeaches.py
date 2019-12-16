"""
Monk Teaches Palindrom

INPUT
3
abc
abba
aba

OUTPUT
NO
YES EVEN
YES ODD
"""

def monkTeaches():
    """
    Inital function to check palindrome
    To check palindrome 
    0th character in the char array, string1 is same as 4th character in the same string.
    """
    n = int(input())
    for i in range(n):
        value = input()
        if value[0] == value[len(value) - 1] and len(value) % 2 == 0:
            print('YES EVEN')
        elif value[0] == value[len(value) - 1] and len(value) % 2 != 0:
            print('YES ODD')
        else:
            print("NO")

if __name__ == '__main__':
    monkTeaches()