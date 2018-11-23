# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 20:39:54 2018

@author: user
"""

a = int(input('sayiyi gir:    '))

x= input("""

1. mm
2. cm 
3. dm
4. m


seciniz
""")



if x ==1:
    b=1000*a
    
if x==2:
    b=100*a

if x==3:
    b=10*a
else:
    b=a/1000

print('son deger:   {} '.format(b))    