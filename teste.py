import sys

temp = open('test.txt', 'w')
a = 1
b = 2
for i in range (100):
    temp.write ('%03d\n' %i)


temp.close()
