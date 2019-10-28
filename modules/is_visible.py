# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:18:32 2019

@author: ulipa
"""
from numba import jit

@jit(nopython=True, cache=True)
def my_func(vals):
    def is_visible (y ,a ,b ):
        isit = True
        c = a +1
        while isit and c < b:
            isit = y[c]<y[b]+(y[a]-y[b])*((b-c)/float(b -a ))
            c = c +1
        return isit
    
    eds = []
    for a in range(len(vals)):
        for b in range(a+1,len(vals)):
            if is_visible(vals,a,b):
                eds.append((a,b))
    return(eds)