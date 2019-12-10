"""
Google Interview Question 
Asked some simple stuff
A given array and need to find out the sum given

arr1 = [1, 2, 3, 5] = 8
arr2 = [1, 3, 4, 4] = 8

Output will be True or false
"""

def hasPairWithSum(arr, sum):
	"""NAIVE Approach
		that first came to mind """
	for i in range(0, len(arr) - 1):
		for j in range(len(arr)):
			if arr[i] + arr[j] == sum:
				return True
	return False


def hasPairWithSumBetter(arr, sum):
	"""
	Better and specific approach
	"""
	mySet = set()
	for i in range(0, len(arr)):
		if arr[i] in mySet:
			return True
		mySet.add(sum - arr[i])
	return False


if __name__ == '__main__':
	arr2 = [1, 2, 3, 5]
	arr1 = [1,3,4,4]
	print(hasPairWithSumBetter(arr2, sum=8))