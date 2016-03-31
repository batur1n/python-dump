def count_holes(n):
	c = 0
	nums = ['0', '4', '6', '9']
	if isinstance(n, int):
		for i in str(n):
			if i in nums:
				c += 1
			elif i == '8':
				c += 2
		return c
	elif isinstance(n, float):
		return 'ERROR'
	else:
		return 0

print(count_holes('123'))
print(count_holes(906))
print(count_holes('001'))
print(count_holes(-8))
print(count_holes(-8.0))
