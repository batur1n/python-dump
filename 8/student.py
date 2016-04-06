class Student:

	def __init__(self, name, conf):
		self.name = name
		self.conf = conf
		self.labs = [0] * conf.get('lab_num')
		self.exam = int()

	def make_lab(self, m, n = None):
		if m > self.conf.get('lab_max'):
			m = self.conf.get('lab_max')
		if n == None:
			self.labs[next(x for x, i in enumerate(self.labs) if i == 0)] = m
		else:
			self.labs[n] = m

	def make_exam(self, m):
		if m > self.conf.get('exam_max'):
			m = self.conf.get('exam_max')
		self.exam = m

	def is_certified(self):
		if (sum(self.labs) + self.exam)/100 >= self.conf.get('k'):
			return ( (sum(self.labs) + self.exam), True )
		else:
			return ( (sum(self.labs) + self.exam), False )

#Testing:

conf = {'exam_max' : 30, 'lab_max' : 7, 'lab_num' : 10, 'k' : 0.61 }
oleg = Student('Oleg', conf)
oleg.make_lab(1)
print(oleg.labs)
oleg.make_lab(8, 0)
print(oleg.labs)
oleg.make_lab(1)
print(oleg.labs)
oleg.make_lab(10,7)
print(oleg.labs)
oleg.make_lab(4,1)
print(oleg.labs)
oleg.make_lab(5)
print(oleg.labs)
oleg.make_lab(6.5)
print(oleg.labs)
oleg.make_exam(32)
print(oleg.is_certified())
oleg.make_lab(7,1)
print(oleg.is_certified())
