import sys
reload(sys)
sys.setdefaultencoding('utf8')
def show_string(s):
    unicode(s)
    codes = ['utf-8','cp1251']
    for i in codes:
        print(s.encode(i))

print(show_string('чтиво было'))
