import sys

x = float(sys.argv[1]) #initial
p = float(sys.argv[2]) #rate
y = float(sys.argv[3]) #final
c = 0

while x < y:
	x = round( (x + x*(float(p)/100)), 2 )
	c += 1
print(c)
