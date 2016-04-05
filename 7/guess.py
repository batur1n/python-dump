import sys
x = int(input('Number: '))
n = int(input('Maximum number: '))
result = int()

def input_set():
    q = set()
    s = str(input('Enter a set: ').split(' '))
    print(s)
    for i in s:
        q.add(i)
    print(q)
    return(q)

while result != x:
    a = input_set()
    if x in a:
        print('YES') 
        new = s.intersection(x)
	print(new)
    else:
       print('NO')
