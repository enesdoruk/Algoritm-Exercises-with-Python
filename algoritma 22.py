# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""

b = int(input('sayiyi giriniz:   '))
x=[]


for a in range(1,99,1):
    if pow(a,3)-pow(a,2)==b:
        x.append(a)
        
        
print('liste:   {}'.format(x))        