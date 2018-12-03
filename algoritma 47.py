# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 19:30:04 2018

@author: user
"""

n = int(input('n sayisi gir:   '))
a = [i]

for i in range(1,n,1):
    a.append(i)

for i in range(2,n,1):
    g = a[i]
    j=i-1
    if j>0 and a[i]>g:
        a[j+1] = a[j]
        j=j-1
        a[j+1]=g

for i in range(1,n,1):
    print('a[{}] ====  {}'.format(a[i]))
    
        
    
        
    