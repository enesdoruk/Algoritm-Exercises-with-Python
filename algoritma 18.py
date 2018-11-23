# -*- coding: utf-8 -*-
"""



@author: enes doruk
"""

f1=1
f2=1
f3=1

n=int(input('n sayisini gir'))
r=int(input('r sayisini gir'))


for i in range(1,n,1):
    f1= f1*i
    if i<=r:
        f2=f2*i
    if i<=n-r:
        f3=f3*i
    
k = f1/(f2*f3)

print('faktoriyel degeri   {}'.format(k))    