# -*- coding: utf-8 -*-
"""

@author: enes doruk
"""

import math

yaricap = int(input('yaricapı giriniz:  '))

alan =math.pi*pow(yaricap,2)

cevre = math.pi*2*yaricap


print('alan  {}  ve cevre   {}  '.format(alan,cevre))