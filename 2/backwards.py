import sys
i = 0 
c = ''
s = str(sys.argv[1])
s1 = s.split(' ')
while i != len(s1):
      c = c + (s1[-(i+1)]) + ' '
      i = i + 1
print(c)
