# -*- coding: utf-8 -*-
"""

@author: enes doruk
"""

for i in range(1,9,1):
    
    for j in range(0,9,1):
        
        for k in range(0,9,1):
            
            if 100*i+10*j+k==pow(i,3)+pow(j,3)+pow(k,3):
                print('armstong sayısı:   ',100*i+10*j+k)
                
            