# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""

'''

NESTED THREE FOR LOOPS

'''

T=0
N=100

for I in range(1,N,1):
    
    for J in range(1,N,1):
        
        for F in range(1,N,1):
            
            T=T+F+J+I
            
print('T value is:   ',T)            