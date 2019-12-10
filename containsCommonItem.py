import datetime
"""
Checking from the array the items contain into array or not

For example
array1 = ['a', 'b', 'c', 'd']
array2 = ['z', 'y', 'w']
"""

def containCommonItem(array1, array2):
	"""
	Two possibility to solve problem 
	1. Standard method looping each array by (i, j) and checking 
	the item exists or not
	2. Using the python standard code to find out
	"""
	a = datetime.datetime.now()
	for i in range(0, len(array1)):
		for j in range(0, len(array2)):
			if array1[i] == array2[j]:
				return True
		else:
			return False
	

def containCommonItem2(arr1, arr2):
	"""
	This will be the approach 2 
	using standard method of python
	"""
	for val in arr1:
		if val in arr2:
			print(True)
			break
		else:
			print(False)


if __name__ == '__main__':
	arr1 = ['a', 'b', 'c', 'd', 's', 'q', 'x']
	arr2 = ['z', 'y', 'w', 'a']
	a = datetime.datetime.now()
	print(containCommonItem(arr1, arr2))
	print( datetime.datetime.now() - a)