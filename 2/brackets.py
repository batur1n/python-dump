import sys
s = str(sys.argv[1])
i = 0
c = 0

while i != len(s):
      if s[i] == '(':
            c = c + 1
      elif s[i] == ')':
            c = c - 1
      else:
            c = c + 0           
      i = i + 1

if c != 0:
   print('NO')
else:
   print('YES') 
