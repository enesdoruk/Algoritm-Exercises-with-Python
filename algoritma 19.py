# -*- coding: utf-8 -*-
"""

@author: enes doruk
"""

a = int(input('a sayisini gir'))

if a == 0:
    print('sıfıra bölüm olamaz')
    
else:
    b= int(input('b sayisini gir'))
    c= int(input('c sayisini gir'))
    
    x = (c-b)/a
    
    print('sonuc =     {}'.format(x))