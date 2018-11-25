# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:54:58 2018

@author: user
"""

a = int(input('istediğiniz haneli a sayisini giriniz'))

c = []

for i in range(1,a,1):
    if a % i ==0:
        c.append(i)
        
if len(c) >2:

    print('asal sayi değil')
    
else:
    print('sayi asal')
        