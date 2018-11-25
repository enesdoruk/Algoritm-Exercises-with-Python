# -*- coding: utf-8 -*-
"""

@author: enes doruk
"""

a = int(input('a sayisi giriniz'))

if a ==1:
    bölen =1
    
else:
    bölen =int(a/2)

if bölen>1 and a%bölen >0:
    bölen =bölen-1

else:
    print('bölen:  ',bölen)    