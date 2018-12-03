# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""

n = int(input('n sayisini giriniz:   '))

for i in range(1,n,1):
    a[i] = int(input('giriniz:   '))
   
for i in range(1,n,1):
    for j in range(1,n-1,1):
        
        if a[j+1] < a[j]:
            g = a[j]
            a[j] = a[j+1]
            a[j+1] = g
            
    
