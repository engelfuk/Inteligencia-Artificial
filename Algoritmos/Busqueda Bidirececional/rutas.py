# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:04:53 2018

@author: Oscar Sandoval
"""
from collections import deque
#Encuentra la ruta
def ruta(nodo):
    r = deque()
    r.append(nodo)
    while nodo.parent is not None:
        nodo = nodo.parent
        r.append(nodo)
    r.reverse()
    return list(r)
        