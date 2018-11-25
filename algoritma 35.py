# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""

def fonk(x):
    
    3*pow(x,2)+2*x
    return 9

a = int(input('a sayisi gir:   '))
b = int(input('b sayisi gir:   '))
n = int(input('n sayisi gir:   '))

m = int(n/2)
h=(b-a)/n

t1=0
t2=0

for i in range(1,m,1):
    
    t1=t1+fonk(a+(2*i-1)*h)
    
for i in range(1,m-1,1):
    
    t2=t2+fonk(a+2*i*h)

t= (b-a)/(6*m)*(fonk(a)+4*t1+2*t2+fonk(b))

print('t degeri:   {}'.format(t))

    