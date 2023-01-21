# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:02:09 2022

@author: remyh
"""

#%%
from ipycanvas import Canvas
c = Canvas(width=500,height=500)
c.fill_style='red'
c.fill_rect(100,100,50,50)
c

#%%
from matplotlib import pyplot as plt
import numpy as np
x = np.arange(10)
y = x*x
plt.plot(x,y)
plt.show()

