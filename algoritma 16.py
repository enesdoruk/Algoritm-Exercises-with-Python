# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""

sayi = int(input('sayi giriniz:   '))

c = []

for i in range(1,sayi):
    
    if sayi % i == 0:
        c.append(i)
        
    
       
print(c) 
    