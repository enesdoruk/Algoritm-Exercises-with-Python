# -*- coding: utf-8 -*-
"""


@author: enes doruk
"""
import math

kenar1 = int(input('kenar1 giriniz:    '))

kenar2 = int(input('kenar2 giriniz:    '))

aci = float(input('aci degerini giriniz:     '))

alan = pow(kenar1,2) + pow(kenar2,2) -2*kenar1*kenar2*math.cos(aci)

print('alan:     {}'.format(alan))