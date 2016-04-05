# -*- coding: utf-8 -*-
import sys
reload(sys)
def show_string(s):
    unicode(s)
    codes = ['utf-8','cp1251']
    for i in codes:
        print(s.encode(i))

print(show_string('чтиво было'))
