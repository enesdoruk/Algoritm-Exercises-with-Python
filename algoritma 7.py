# -*- coding: utf-8 -*-
"""


@author: enes doruk 
"""

T1= 1
T2 = 2

for I in range(1,4,2):
    T1= I
    
    for J in range(1,5,1):
        if I%2 ==0:
            T2 = T2+I+J
        else:
            T1 = T1+2*J
            
        T2= T1+T2-I
        
T1 = 2*T1
       
print('T1 İS   {}  AND T2 İS   {}'.format(T1,T2))        