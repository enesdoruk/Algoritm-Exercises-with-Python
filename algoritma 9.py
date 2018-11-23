# -*- coding: utf-8 -*-
"""


@author: ENES DORUK
"""

t1 = 1
t2 = 2

for i in range(1,5,3):
    
    t1 = i
    for j in range(4,1,-3):
        t1=t1-i
        
        if i>j:
            t1=t1+j
        else:
            t2=t2+j
            
        t2=t2*i


t1 = 2*t1
t2= t2/2

print('t1 is    {}  , t2 is   {}  '.format(t1,t2))            