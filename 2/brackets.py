import sys
s = str(sys.argv[1])
i, c = 0, 0

while i != len(s):
      if s[i] == '(':
            c = c + 1
      elif s[i] == ')':
            c = c - 1
      i = i + 1

if s[0] == ')':
   c = 1

if c != 0:
   print('NO')
else:
   print('YES') 
