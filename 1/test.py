import math
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
x0 = math.sqrt( a * b )
x1 = ( (math.e**a)*b )
x2 = ( math.exp( (2*a)/b ) )
x3 = ( a * x2 )
x =  ( ( x0/x1 ) + x3 )
print(x)
