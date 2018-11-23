# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""

t1 = 0 
f1= 1

for i in range(1,5,3):
    t1 =i
    for j in range(4,1,-2):
        
        if i>j:
            t1=t1+j
        else:
            f1 = f1*j
    
        t1 = t1-i
        f1= f1/i


t1= 2*t1
f1= f1/2

print('T1 İS   {} ,  T2 İS   {}'.format(t1,f1))          