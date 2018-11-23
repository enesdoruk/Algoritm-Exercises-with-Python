# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""

t1=0
t2=0
t3=0
n =100

for i in range(1,n,1):
    t1= t1+i
    
    
for i in range(1,n,2):
    t2= t2+i
    
    
for i in range(2,n,2):
    t3= t3+i

print('t1 {}  t2  {}   t3  {}  '.format(t1,t2,t3))    