import sys

n = int(sys.argv[1])
i = 1 
a = 0 
b = 1

if b == 0:
   print('0')
else:
   while i < n:
         i = i + 1
         a, b = b, a + b
   print(b)
