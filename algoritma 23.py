# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:06:50 2018

@author: user
"""

s = int(input('sayiyi giriniz:   '))

for i in range(0,s,1):
    
    for j in range(0,s,1):
        
        if pow(i,2)+pow(j,2)==s:
            print('i :  {}. j:  {}'.format(i,j))
            
            