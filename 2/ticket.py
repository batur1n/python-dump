import sys
a, b = str(sys.argv[1]), str(sys.argv[2])
c = 0

while len(a) != 6:
	a = '0' + a
while len(b) != 6:
    b = '0' + b

for i in range( int(a[3:]), int(b[3:])+1 ):
	if sum(int(x) for x in str(i)) == sum(int(y) for y in a[:3]):
		c += 1
	elif (i == 0):
		c = 1
print(c)
