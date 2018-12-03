# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:14:53 2018

@author: user
"""

n = int(input('n sayisini giriniz'))
a=[]
g=[]


for i in range(1,n,1):
   a.append(i)
   
degisim =1

if degisim ==1:
    degisim=0
    for i in range(1,n-1,2):
        if a[i+1]<a[i]:
            g =a[i]
            a[i]=a[i+1]
            a[i+1]=g
            degisim=1

    for i in range(2,n-1,2):
        if a[i+1] < a[i]:
            g=a[i]
            a[i]=a[i+1]
            a[i+1]=g
            degisim=1
            
for i in range(1,n,1):
    print('a[{}]== {} '.format(i,a[i]))            
            