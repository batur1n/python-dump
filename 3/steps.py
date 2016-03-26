import sys

n, i = int(sys.argv[1]), 1 
s = ''

if 0 < n <= 9:
	print('1')
	while i != n:
		s = s + str(i)
		print(s+str(i+1))
		i += 1
else:
	print('Error. Please enter a positive integer which is less than 9.')
