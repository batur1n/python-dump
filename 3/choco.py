from fractions import gcd

print("m = ")
m = input()
print("n = ")
n = input()
print("k = ")
k = input()

if m*n > k and gcd(m*n, k) > 1:
	print('YES')
else:
	print('NO')
