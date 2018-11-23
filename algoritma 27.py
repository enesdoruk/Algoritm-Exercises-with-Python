# -*- coding: utf-8 -*-
"""


@author: enes doruk

"""
ta = 0
tb = 0


a= int(input('a sayisi gir:    '))
b= int(input('b sayisi gir:    '))

for i in range(1,a-1,1):
    
    if a%i ==0:
        ta += i
        
for i in range(1,b-1,1):
    
    if b%i == 0:
        tb += i
        
if ta ==b and tb==a:

    print('dost sayilar')

else:
    
    print('dost sayi değil')        
        
        