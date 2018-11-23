# -*- coding: utf-8 -*-
"""


@author: enes doruk

"""

n = int(input('n sayisi gir:   '))

s = 1

for i in range(1,n,1):
    
    for j in range(1,i,1):
        print('{},'.format(s))
        s = s+1
        print('\n')