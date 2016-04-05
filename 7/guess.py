import sys
x = int(input('Number: '))
n = int(input('Maximum number: '))
sets = list()

def input_set():
	return set(int(i) for i in input('Enter a set: ').split())

def check_set(q):
	if x in q and len(q) > 0 and isinstance(q, set):
		print('YES')
		return q
	else:
		print('NO')
		return None

q1 = check_set(input_set())

if q1 is not None:
	sets.append(q1)
else:
	q1 = set()

ask = str(input('Would you like to check another set? (y/n): '))
while ask == 'y':
	q1 = check_set(input_set())
	if q1 is not None:
		sets.append(q1)
	else:
		q1 = set()
	ask = str(input('Would you like to check another set? (y/n): '))

if len(sets) > 0:
	print(set.intersection(*sets))
else:
	print('No matching numbers :(')
