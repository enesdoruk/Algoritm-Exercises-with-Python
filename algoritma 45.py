# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 22:59:56 2018

@author: user
"""

n = int(input('n sayisini giriniz:   '))
a = []


for i in range(0,n):
    
    a.append(int(input('sayi gir')))
    
    
ilk = 0
son = n-1
degisim = 1

if degisim == 1:
    degisim = 0
    ilk = ilk+1
    for i in range(ilk,son,1):
        if a[i+1] < a[i]:
            g= a[i]
            a[i] = a[i+1]
            a[i+1] = g
            
        else: 
            degisim= 0
            son = son-1
            for i in range(son,ilk,-1):
                if a[i+1] < a[i]:
                    g = a[i]
                    a[i] = a[i+1]
                    a[i+1] = g
                    degisim =1
            
for i in range(0,n,1):
    print(a[i])


            
            
            
            
            
            
            
    