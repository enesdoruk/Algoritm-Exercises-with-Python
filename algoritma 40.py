# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""

n = int(input(' n sayisini gir:  '))

a = []

for i in range(1,n,1):
    a.append(i)
    
enb = a[1]
enk = a[1]
enbyer =1
enkyer =1

for i in range(2,n,1):

    if a[i]>enb:
        enb = a[i]
        enbyer = i
    if a[i]<enk:
        enk = a[i]
        enk = i
        
print('enb {}, enbyer {}, enk {}, enkyer {} '.format(enb,enbyer,enk,enkyer))        
                