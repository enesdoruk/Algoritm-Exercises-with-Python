# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""


sayi = int(input('sayiyi giriniz:    '))

if sayi < 0:
    sayi = sayi*-1


if sayi%2 == 0:
    print('sayi cift')
    
else:
    print('sayi tek')    