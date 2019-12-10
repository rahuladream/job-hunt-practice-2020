"""
Pairing the number in the style of (a,a) (a,b) (a,c) so on

>> 
Big O => (1 + 2N)
"""

num = ['a', 'b', 'c', 'd']
for i in range(0, len(num)): # O(n)
	for j in range(0, len(num)): #O(n)
		print(num[i], num[j]) #O(1)
