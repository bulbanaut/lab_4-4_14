#! /usr/bin/python3
import math
a, b, h = int(input('a:')), int(input('b:')), int(input('h:'))
for x in range(a, b +1, h):
    y = 2*math.tan(x/2) +1
    print('', '_'*(len(str(y)) +6) , '\n', '|', x, '|', y)