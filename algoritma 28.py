# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:55:48 2018

@author: user
"""

n = int(input('n sayisi gir:\n'))

for i in range(1,n,1):
    s=0
    
    for j in range(1,j,1):
        
        if i%j ==0:
            s = s+1
            
        if i%s == 0:
            print(i)