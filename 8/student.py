class Student:
#Google: python attributes
	exam, result, passed = int(), int(), bool()

	def __init__(self, name, conf):
		self.name = name
		self.conf = conf
		global labs
		labs = [0] * conf.get('lab_num')


	def make_lab(self, m, n = None):
		global labs
		if m > 7:
			m = 7
		if n == None:
			for i in labs:
				if labs[i] == 0:
					labs[i] = m
					break
				else:
					continue
					print('Continuing')
		elif n <= len(labs):
			labs[n] = m

	def make_exam(self, m):
		global exam
		if m in range(0,30) and m > 0:
			exam = m
		elif m > 30:
			exam = 30

	def is_certified(self):
		global labs, exam
		result = sum(labs) + exam
		if result/100 >= self.conf.get('k'):
			passed = True
		else:
			passed = False
		return (result, passed)


conf = {'exam_max' : 30, 'lab_max' : 7, 'lab_num' : 10, 'k' : 0.61 }
oleg = Student('Oleg', conf)
oleg.make_lab(1)
oleg.make_lab(8, 0)
oleg.make_lab(1)
oleg.make_lab(10,7)
oleg.make_lab(4,1)
oleg.make_lab(5)
oleg.make_lab(6.5)
print(labs)
oleg.make_exam(32)
print(oleg.is_certified())
oleg.make_lab(7,1)
print(oleg.is_certified())
