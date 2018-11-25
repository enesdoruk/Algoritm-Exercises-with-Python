# -*- coding: utf-8 -*-
"""

@author: enes doruk
"""

n = int(input('n sayisini giriniz'))

a=[]
b=[]
c=[]


for i in range(1,n,1):
    
    a[i] += a[i]
    
    
for i in range(1,n,1):
    
    b[i] += b[i]
    
    
for i in range(1,n,1):

    c[i] += a[i] + b[i]


for i in range(1,n,1):
    
    print(c[i])
    print('\n')    