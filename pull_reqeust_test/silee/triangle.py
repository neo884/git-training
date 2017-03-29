# -*- coding: cp949 -*-

print 'drawing triangle\n'
d = float(raw_input('length: '))

for i in range(int(d)+1):
    print('* ' * i)

area = float((d ** 2) / 2)
print('area : %s' % area)

raw_input()
