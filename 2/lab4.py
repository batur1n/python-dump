import sys
s = str(sys.argv[1])
s = s.lower()
s = s.replace(' ', '')
i = 0
print(s)

while i != len(s):
      if s[i] == s[-(i+1)]:
          check = 'YES'
      else:
          check = 'NO' 
      i = i + 1
print(check)
