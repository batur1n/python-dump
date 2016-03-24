import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

if x > 0:
   dash = ('-')
else:
   dash = ('')

l = ('la')
k = l+(x-1)*(dash+l)
space = (' ')

if (z == 1):
   end = ('!')
else: 
   end = ('.')

print( "Everybody sing a song:"+(space+k)*y + end )
