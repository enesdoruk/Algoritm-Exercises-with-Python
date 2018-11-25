# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""
import numpy as np

n = int(input('n sayisini gir:   '))

a0 = 0
t = 0

a = []

for i in range(1,n,1):
    a.append(i)
    a0 = a[i]+a0
    
a0 = a0/n

for i in range(1,n,1):

    t = t+pow(a[i-ao],2)

v = t/n
s = pow(v,.5)

print('s:  {},  v:  {}'.format(s,v))    