import calendar
from datetime import date

def create_calendar_page(m, y):
	spaces = ''
	dates = ''
	header = ('-'*20) + '\n' + 'MO TU WE TH FR SA SU' + '\n' + ('-'*20) + '\n'
	c = calendar.Calendar()
	for i in c.itermonthdays(y, m):
		if i != 0:
			d = date(y, m, i)
			if i == 1:
				spaces = '   ' * d.weekday()
			if d.weekday() == 6 and i < 31:
				dates = dates + d.strftime('%d') + '\n'
			elif d.weekday() == 6 and i in range(27,32):
				dates = dates + d.strftime('%d')
			else:
				dates = dates + d.strftime('%d') + ' '
	dates = dates.rstrip()
	return header+spaces+dates

print(create_calendar_page(2,1993))
print(create_calendar_page(4,2016))
print(create_calendar_page(5,2016))
print(create_calendar_page(9,2016))
