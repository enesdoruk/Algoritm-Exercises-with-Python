# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:31:09 2018

@author: user
"""

for i in range(1,9,1):
    
    for j in range(0,9,1):
        
        for k in range(0,9,1):
            
            for l in range(0,9,1):
                
                if i+j == k+l:
                    
                    print('sayi:  {}'.format(1000*i+100*j+10*k+l))