# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""

m = int(input('m sayisi gir'))

n = int(input('n sayisi gir'))

t = pow(n+1,m)

for i in range(1,n,1):
    f1=1
    f2=1
    f3=1
    
    for k in range(1,m+1,1):
        f1*=k
        
    for k in range(1,i,1):
        f2*=k
        
    for k in range(1,m+1-i,1):
        f3*=k
        
    c = f1/(f2*f3)
    
    t=t+pow(-1,i)*c*(pow(n+1-i,m))
    
    
print('t sayisi:   {}'.format(t))