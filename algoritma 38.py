# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""

n = int(input('n sayisini giriniz:   '))
k = int(input('k sayisini giriniz:   '))

a=[]
b=[]

for i in range(1,n,1):
    a.append(i)
    
for i in range(1,n,1):
    b[i] += k*a[i]
    
print(b)
    