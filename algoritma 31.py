# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""


import random

x = random.randint(1,100)

s = 0
a = 0
while a != x:
    
    a = int(input('0-100 arasında sayı giriniz'))
    
    if a < x:
        print('daha büyük bir sayi girin')
        
    if a > x:
        print('daha kücük bir sayi girin')
        
    s = s+1
    
print('tebrikler buldunuz sayı: {},  {} tahminde bulundunuz'.format(x,s))