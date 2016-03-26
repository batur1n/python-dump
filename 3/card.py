import sys

print('N= ')
N, i, j = int(input()), 0, 0
a, b = list(), list()

for i in range(N-1):
	a.append(int(input()))
	i += 1

for j in range(N):
	b.append(j+1)
	j += 1

print(list(set(b)-set(a)))

