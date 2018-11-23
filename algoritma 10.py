# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""

a=5
b=1

for i in range(1,6,4):
    a = i
    for j in range(5,0,-4):
        if i>j:
            a=a+i
        elif i<j:
            b=b+j
        b=a-i
        
        
print('a is   {}, b is  {}   '.format(a,b)) 