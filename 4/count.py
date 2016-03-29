def counterr(a, b):
	c = 0
	new = []
	for i in str(b):
		if i in str(a) and i not in new:
			c += 1
			new.append(str(i))
	return c

print(counterr(12345, 567))
print(counterr(1233211, 12128))
print(counterr(123, 45))
