# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""

T1= 1
T2 = -1

for I in range(-5,5,6):
    T1 = T1+2*I
    for J in range(5,1,-3):
        T1 = T1- 2*J
        T2 = T2-I
     
    T2 = T2+I


print('T1 is   {} , T2 is   {}'.format(T1,T2))    