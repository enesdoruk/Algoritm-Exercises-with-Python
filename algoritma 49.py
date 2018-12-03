# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 19:52:57 2018

@author: user
"""

n = int(input('n sayisi giriniz'))

a = []
g = []


for i in range(1,n,1):
    a.append(i)
    
i = 2

if i<=n:
    if i==1 or a[i-1]<=a[i]:
        i=i+1
    else:
        g = a[i-1]
        a[i-1]= a[i]
        a[i]=g
        i=i-1
        
        
for i in range(1,n,1):
    print('a[{}] == a{}'.format(i,a[i]))
        