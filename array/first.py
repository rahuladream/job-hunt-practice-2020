"""
Objective is to learn
1. append()
2. insert()
"""

import array
# Importing "array" for array operations
arr = array.array('i', [1,2,3])

#Initializing array with values 
for i in range(0,3):
    print(arr[i], end=" ")
print("\r")

arr.append(4)
#appending new value at the end

for i in range(0,4):
    print(arr[i], end=" ")
print("\r")


arr.insert(2,5)
#inserting 5 at 2nd position

for i in range(0,5):
    print(arr[i], end=" ")
print("\r")