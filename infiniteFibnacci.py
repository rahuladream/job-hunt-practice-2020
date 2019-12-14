def getNthFib(i):
	if i <= 1:
		return i
	else:
		return (getNthFib((i-1) + getNthFib(i-2)))

if __name__ == '__main__':
	for i in range(n):
		print(getNthFib(i))